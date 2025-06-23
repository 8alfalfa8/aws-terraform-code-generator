import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import ast

env = Environment(loader=FileSystemLoader('./templates'))

# Excelファイルパス
file_path = 'free_input.xlsx'
Path("output").mkdir(exist_ok=True)
Path("output/per_service").mkdir(exist_ok=True)  # シートごとの出力用ディレクトリ
name_prefix = "prd-"
name_suffix = "-01"
outputs = []
all_resources = []  # 全リソースをまとめる用

# EC2インスタンス定義
def process_ec2(df, combined_mode=False):
    ec2_outputs = []
    for _, row in df.iterrows():  # レコード毎
        if pd.isna(row['インスタンス名']):
            continue

        ebs_parts = str(row['EBS']).split()
        ebs_size = int(ebs_parts[0].replace('GB', ''))
        ebs_type = ebs_parts[1]

	    # タグ列（文字列辞書）を辞書に変換
        tags = ast.literal_eval(row['タグ']) if 'タグ' in row and pd.notna(row['タグ']) else {}
	        
        instance_render = env.get_template("EC2.tf.j2").render(
            instance_name=row['インスタンス名'],
            ami=row['AMI'],
            instance_type=row['インスタンスタイプ'],
            key_pair=row['キーペア'],
            ebs_size=ebs_size,
            ebs_type=ebs_type,
            security_group=row['セキュリティグループ'],
            subnet=row['サブネット'],
            tags=tags,
            user_data = row['ユーザーデータ'] if 'ユーザーデータ' in row and pd.notna(row['ユーザーデータ']) else ''
        )
        output_render = env.get_template("output.tf.j2").render(instance_name=row['インスタンス名'])
        outputs.append(output_render)
        ec2_outputs.append(instance_render)
        
    if not combined_mode:
        # EC2シートの全内容を1つのファイルに出力
        with open("output/per_service/ec2_resources.tf", 'w') as f:
            f.write("\n".join(ec2_outputs))
    
    if combined_mode:
        all_resources.extend(ec2_outputs)

# RDSインスタンス定義
def process_rds(df, combined_mode=False):
    rds_outputs = []
    for _, row in df.iterrows():  # レコード毎
        if pd.isna(row['RDS識別子']):
            continue

	    # タグ列（文字列辞書）を辞書に変換
        tags = ast.literal_eval(row['タグ']) if 'タグ' in row and pd.notna(row['タグ']) else {}
	        
        instance_render = env.get_template("RDS.tf.j2").render(
            identifier=row['RDS識別子'],
            engine=row['エンジン'],
            engine_version=row['エンジンバージョン'],
            instance_class=row['インスタンスクラス'],
            allocated_storage=row['ストレージ'],
            storage_type=row['ストレージタイプ'],
            db_name=row['DB名'],
            username=row['ユーザー名'],
            password=row['パスワード'],
            security_group=row['セキュリティグループ'],
            subnet_group_name=row['サブネットグループ名'],
            subnet_ids=row['サブネットID一覧'],
            publicly_accessible=row['パブリックアクセス'],
            tags=tags
        )

    if not combined_mode:
        # EC2シートの全内容を1つのファイルに出力
        with open("output/per_service/rds_resources.tf", 'w') as f:
            f.write("\n".join(rds_outputs))
    
    if combined_mode:
        all_resources.extend(rds_outputs)

# セキュリティグループ定義
def process_sg(df, combined_mode=False):
    sg_outputs = []
    sg_df = df.drop_duplicates(subset=['セキュリティグループ'])
    for _, row in sg_df.iterrows():
        if pd.isna(row['セキュリティグループ']):
            continue

        tags = ast.literal_eval(row['タグ']) if 'タグ' in row and pd.notna(row['タグ']) else {}
        sg_render = env.get_template("SG.tf.j2").render(
            security_group=row['セキュリティグループ'],
            tags=tags
        )
        
        sg_outputs.append(sg_render)
    
    if not combined_mode:
        # SGシートの全内容を1つのファイルに出力
        with open("output/per_service/sg_resources.tf", 'w') as f:
            f.write("\n".join(sg_outputs))
    
    if combined_mode:
        all_resources.extend(sg_outputs)

# サブネット定義
def process_subnet(df, combined_mode=False):
    subnet_outputs = []
    subnet_df = df.drop_duplicates(subset=['サブネット'])
    for _, row in subnet_df.iterrows():
        if pd.isna(row['サブネット']):
            continue

        tags = ast.literal_eval(row['タグ']) if 'タグ' in row and pd.notna(row['タグ']) else {}
        subnet_render = env.get_template("Subnet.tf.j2").render(
            subnet=row['サブネット'],
            cidr_block=row['CIDRブロック'],
            az=row['AZ'],
            tags=tags
        )
        
        subnet_outputs.append(subnet_render)
    
    if not combined_mode:
        # Subnetシートの全内容を1つのファイルに出力
        with open("output/per_service/subnet_resources.tf", 'w') as f:
            f.write("\n".join(subnet_outputs))
    
    if combined_mode:
        all_resources.extend(subnet_outputs)

# --- シート名と関数の対応関係を定義 ---

sheet_handlers = {
    "EC2": process_ec2,
    "RDS": process_rds,
    "SG": process_sg,
    "Subnet": process_subnet,
}

# Excelファイルを読み込み（シート一覧の取得用）
xls = pd.ExcelFile(file_path)

# 1. シートごとに1つのファイルとして出力
for sheet_name in xls.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    if sheet_name in sheet_handlers:
        sheet_handlers[sheet_name](df, combined_mode=False)
    else:
        print(f"処理対象外シート: {sheet_name}（スキップ）")

# 2. 全リソースを1つのファイルにまとめて出力
for sheet_name in xls.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    if sheet_name in sheet_handlers:
        sheet_handlers[sheet_name](df, combined_mode=True)

# Outputまとめ
with open("output/output.tf", 'w') as f:
    f.write("\n".join(outputs))

# 全リソースを1つのファイルに出力
with open("output/all_resources.tf", 'w') as f:
    f.write("\n".join(all_resources))

print("✅ 処理完了！")
print(" - シートごとの統合ファイル: output/per_service/ ディレクトリ")
print("   - EC2: ec2_resources.tf")
print("   - RDS: rds_resources.tf")
print("   - SG: sg_resources.tf")
print("   - Subnet: subnet_resources.tf")
print(" - 全リソース統合ファイル: output/all_resources.tf")
print(" - 出力定義ファイル: output/output.tf")

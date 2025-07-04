
# 🛠️Terraform Code Generator from Excel(for AWS) 

このリポジトリは、Excelで定義されたAWSインフラ構成情報(パラメータシート)から、Terraformコードを自動生成するためのツールです。

## ✅ 特長（特徴）

* **Excel定義書からTerraformコードを一括生成** 
  - インフラ構成をExcelで管理し、その内容をもとにTerraformコードを自動生成できます。

* **ソースコード・テンプレートを全て公開** 
  - Pythonスクリプトおよび入出力テンプレートはすべて公開されており、用途に応じて自由に修正・再利用可能です。

## 📦 構成ファイル

### 📦 無料公開版

```
aws-terraform-code-generator
├─ free.py                             ← Excelを読み取りTerraformコードを生成するPythonスクリプト
├─ input.xlsx                          ← Excelインフラ詳細設計書（パラメータシート）
├─ LICENSE                             ← ライセンス
├─ README                              ← 説明
├─ requirements.txt                    ← 必須パッケージ一覧
├─ .gitignore                          ← キャッシュ・生成ファイル除外用
├─doc/                                 ← ドキュメント
│  └─ …
├─templates/                           ← Terraformのテンプレート（Jinja2形式）
│  ├─ EC2.tf.j2                        ← EC2
│  ├─ SG.tf.j2                         ← セキュリティグループ
│  ├─ Subnet.tf                        ← サブネット
│  └─ …
│
└─output/                              ← 自動生成されるTerraformファイルの格納先
    ├─ all_resources.tf                ← 全シート統合
    ├─ output.tf                       ← outputブロックのみ
    └─ per_service/                    ← サービス毎
         ├─ ec2_resources.tf           ← EC2
         ├─ sg_resources.tf            ← セキュリティグループ
         ├─ subnet_resources.tf        ← サブネット
         └─ …

```

### 📦 商用非公開版（環境分離）

```
aws-terraform-code-generator
├─ prod.py                             ← Excelを読み取りTerraformコードを生成するPythonスクリプト
├─ input.xlsx                          ← Excelインフラ詳細設計書（パラメータシート）
├─ LICENSE                             ← ライセンス
├─ README                              ← 説明
├─ requirements.txt                    ← 必須パッケージ一覧
├─ .gitignore                          ← キャッシュ・生成ファイル除外用
├─doc/                                 ← ドキュメント
│  └─ …
├─templates/                           ← Terraformのテンプレート（Jinja2形式）
│  ├─ EC2.tf.j2                        ← EC2
│  ├─ SG.tf.j2                         ← セキュリティグループ
│  ├─ Subnet.tf                        ← サブネット
│  └─ …
│
└─output/                              ← 自動生成されるTerraformファイルの格納先
    ├─ all_resources.tf                ← 全シート統合
    ├─ output.tf                       ← outputブロックのみ
    ├─ dev/                            ← ◆開発環境(Terraform)格納先
    │   ├─ all_resources.tf            ← 全体統合
    │   ├─ output.tf                   ← outputブロックのみ
    │   └─ per_service/                ← サービス毎格納先
    │        ├─ ec2_resources.tf       ← EC2
    │        ├─ sg_resources.tf        ← セキュリティグループ
    │        ├─ subnet_resources.tf    ← サブネット
    │        └─ …
    ├─ stg/                            ← ◆検証環境(Terraform)格納先
    │   ├─ all_resources.tf            ← 全体統合
    │   ├─ output.tf                   ← outputブロックのみ
    │   └─ per_service/                ← サービス毎格納先
    │        ├─ ec2_resources.tf       ← EC2
    │        ├─ sg_resources.tf        ← セキュリティグループ
    │        ├─ subnet_resources.tf    ← サブネット
    │        └─ …
    ├─ prd/                            ← ◆本番環境(Terraform)格納先
    │   ├─ all_resources.tf            ← 全体統合
    │   ├─ output.tf                   ← outputブロックのみ
    │   └─ per_service/                ← サービス毎格納先
    │        ├─ ec2_resources.tf       ← EC2
    │        ├─ sg_resources.tf        ← セキュリティグループ
    │        ├─ subnet_resources.tf    ← サブネット
    │        └─ …
    └─ sby/                            ← ◆待機環境(Terraform)格納先
         ├─ all_resources.tf           ← 全体統合
         ├─ output.tf                  ← outputブロックのみ
         └─ per_service/               ← サービス毎格納先
              ├─ ec2_resources.tf      ← EC2
              ├─ sg_resources.tf       ← セキュリティグループ
              ├─ subnet_resources.tf   ← サブネット
              └─ …
```

## 📙 使用方法

### 1. 環境構築

```bash
git clone https://github.com/8alfalfa8/aws-terraform-code-generator.git
cd aws-terraform-code-generator

# 仮想環境 (任意)
python -m venv venv
source venv/bin/activate

# 必要パッケージのインストール
pip install -r requirements.txt
```

### 2. 使用
```
python free.py
python prod.py        # 商用非公開

```

## 🚀 今後の展望

* 今後は、**設計から構築（IaC）、さらにテスト・検証（セキュリティおよび監査）までを自動化**し、インフラ運用の効率化と品質向上を図ります。
* GitHub Actionsとの連携により、インフラ構築の全工程をCI/CDパイプラインに統合し、**より効率的かつ安定した運用体制**を実現します。
* また、対応クラウドをAWSだけでなく**GCPやAzureにも拡張**し、**マルチクラウド環境における柔軟なインフラ管理**を目指してまいります。

以下に「自分使用責任（自己責任）」に関する注意事項を追記した修正版を提示します。特に利用者の責任範囲や免責に関する情報を明確にすることで、利用時のトラブル回避に役立ちます。

## ⚠️ 自己責任に関する注意事項（Self Responsibility Disclaimer）

本ツール（Terraform Code Generator from Excel）は、ユーザーの利便性向上を目的として無償で提供されていますが、**ご利用に際してはすべて自己責任でお願いいたします。**

* 本ツールを利用して生成されたコードの**正確性・完全性・安全性**について、開発者および関連団体は一切の保証を致しません。
* ユーザーが本ツールを使用することによって生じた**いかなる損害・不具合・システム障害等に対しても、開発者および関連団体は責任を負いません**。
* 実際の運用環境に適用する際は、**必ずご自身の責任において十分な検証およびレビューを実施してください。**

安全な利用のために、以下を推奨します：

* 生成されたTerraformコードの**内容を確認した上での適用**。
* **バージョン管理やCI/CD環境での段階的適用**。
* 商用環境では**本番前のテスト環境での事前検証**。

## 🤝 商談歓迎

非公開版のご利用や環境構築のご支援をご希望の方は、下記までご連絡ください。
```
Colorful株式会社

〒151-0051
東京都渋谷区千駄ヶ谷3-51-10
PORTAL POINT HARAJUKU 607
info@colorful-inc.jp
```
https://colorful-inc.jp/

## 📝 ライセンス

本リポジトリは [MIT ライセンス](./LICENSE) のもとで公開されています。



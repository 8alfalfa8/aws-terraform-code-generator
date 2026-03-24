# 🎯 AWSでTerraformの動作環境構築

---

AWSでTerraformの動作環境を構築するには、大きく分けて以下の流れで作業します。

---

## ✅ 構築ステップ概要

1. **Terraformの実行環境（CLI）の準備**
2. **AWS IAMユーザー（アクセスキー）の準備**
3. **Terraform設定ファイル（.tf）の作成**
4. **Terraformの実行（init, plan, apply）**
5. **（任意）リモートステート（S3＋DynamoDB）による状態管理の設定**

---

## 🧰 1. Terraform CLIのインストール

### ローカル環境（Mac / Windows / Linux）

* [Terraform公式ダウンロードページ](https://developer.hashicorp.com/terraform/downloads)からOSに合ったバイナリを取得し、PATHを通します。

またはHomebrew（Mac）：

```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

### EC2（Linux）上にTerraformをインストールする場合

```bash
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform
terraform -version
```

---

## 🛡️ 2. AWS認証情報の準備（IAMユーザー＋アクセスキー）

1. AWS管理コンソールでIAMユーザーを作成（`AdministratorAccess`など必要に応じて付与）
2. アクセスキーIDとシークレットアクセスキーを発行
3. ローカルPCに設定

```bash
aws configure
# 対話形式で下記を入力
# AWS Access Key ID:
# AWS Secret Access Key:
# Default region name: ap-northeast-1 など
# Default output format: json
```

---

## 📁 3. Terraform設定ファイルを作成（例）

例：`main.tf`

```hcl
provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_s3_bucket" "example" {
  bucket = "my-terraform-bucket-example-12345"
  acl    = "private"
}
```

---

## ▶ 4. Terraform実行手順

```bash
terraform init        # 初期化（プラグインの取得など）
terraform plan        # 差分の確認
terraform apply       # 実行（リソース作成）
terraform destroy     # 削除（任意）
```

---

## 📦 5. （推奨）ステート管理のリモート化（S3＋DynamoDB）

チーム運用やCI/CDを行う場合は、`terraform.tfstate`をS3に保存＋DynamoDBでロックを管理します。

```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "dev/terraform.tfstate"
    region         = "ap-northeast-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

事前にS3バケットとDynamoDBテーブル（`LockID`をパーティションキーとする）を作成しておく必要があります。

---

## ✅ まとめ：最小構成で始めるには

| 項目                    | 必要？ | 補足                  |
| --------------------- | --- | ------------------- |
| Terraform CLI         | ✅   | ローカル or EC2上にインストール |
| AWS IAM認証情報           | ✅   | aws configure で設定   |
| `.tf`ファイル             | ✅   | provider＋リソース記述     |
| S3＋DynamoDB（リモートステート） | 任意  | チーム・本番用途で推奨         |

---
## 📝 推奨IaCツール(無料)

* Terraform Code Generator from Excel(for AWS)
  - Excelで定義されたAWSインフラ構成情報(パラメータシート)から、Terraformコードを自動生成するためのツールです。
  - https://github.com/8alfalfa8/aws-terraform-code-generator
---


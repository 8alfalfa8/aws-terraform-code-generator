
# 🛠️Terraform Code Generator from Excel(for AWS) 

本リポジトリは、Excelで定義されたAWSインフラ構成情報(パラメータシート)から、Terraformコードを自動生成するためのツールです。

---

## 閲覧準備：Markdown Viewer のインストール

本リポジトリのドキュメント（Markdown記法）をブラウザで正しく閲覧し、図解（Mermaid）を表示させるために、ブラウザ拡張機能 **「Markdown Viewer」** のインストールと設定を推奨しています。

### 1. インストール
お使いのブラウザに合わせて、以下のリンクからインストールしてください。

* **Chrome / Edge**: [Markdown Viewer (Chrome Web Store)](https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcedbflnpeebnljnphakjden)
* **Firefox**: [Markdown Viewer (Firefox Add-ons)](https://addons.mozilla.org/en-US/firefox/addon/markdown-viewer/)

### 2. ローカルファイルへのアクセス許可（必須）
PC上のファイルをブラウザで開くために、以下の設定を行ってください。

1. ブラウザの拡張機能アイコン（パズルマーク）から **[Markdown Viewer]** > **[詳細]**（または拡張機能の管理）を開きます。
2. **「ファイルの URL へのアクセスを許可する」** を **ON** にします。

### 3. Mermaid（図解）の有効化
ドキュメント内のチャートを表示するために必要です。

1. Markdown Viewer のオプション（⚙アイコン）を開きます。
2. 左メニューの **[Compiler]** を選択します。
3. **[Mermaid]** の項目にチェックを入れます。

設定完了後、この `README.md` ファイルをブラウザにドラッグ＆ドロップすることで、整形されたレイアウトで閲覧可能になります。

---

## ✅ 本ツールの特長（特徴）

* **Excel定義書からTerraformコードを一括生成** 
  - インフラ構成をExcelで管理し、その内容をもとにTerraformコードを自動生成できます。

* **ソースコード・テンプレートを全て公開** 
  - Pythonスクリプトおよび入出力テンプレートはすべて公開されており、用途に応じて自由に修正・再利用可能です。

---

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

---

## 🚀 今後の展望

* 今後は、**設計から構築（IaC）、さらにテスト・検証（セキュリティおよび監査）までを自動化**し、インフラ運用の効率化と品質向上を図ります。
* GitHub Actionsとの連携により、インフラ構築の全工程をCI/CDパイプラインに統合し、**より効率的かつ安定した運用体制**を実現します。
* また、対応クラウドをAWSだけでなく**GCPやAzureにも拡張**し、**マルチクラウド環境における柔軟なインフラ管理**を目指してまいります。

---

## 📝 【資料】

* [IaCに関する技術](https://github.com/8alfalfa8/Tec-Doc/tree/main/04_%E3%82%A4%E3%83%B3%E3%83%95%E3%83%A9/01_IaC)
* [CICDに関する技術](https://github.com/8alfalfa8/Tec-Doc/tree/main/04_%E3%82%A4%E3%83%B3%E3%83%95%E3%83%A9/02_CICD)

---

## ⚠️ 自己責任に関する注意事項（Self Responsibility Disclaimer）

本ツール（Terraform Code Generator from Excel）は、ユーザーの利便性向上を目的として無償で提供されていますが、**ご利用に際してはすべて自己責任でお願いいたします。**

* 本ツールを利用して生成されたコードの**正確性・完全性・安全性**について、開発者および関連団体は一切の保証を致しません。
* ユーザーが本ツールを使用することによって生じた**いかなる損害・不具合・システム障害等に対しても、開発者および関連団体は責任を負いません**。
* 実際の運用環境に適用する際は、**必ずご自身の責任において十分な検証およびレビューを実施してください。**

安全な利用のために、以下を推奨します：

* 生成されたTerraformコードの**内容を確認した上での適用**。
* **バージョン管理やCI/CD環境での段階的適用**。
* 商用環境では**本番前のテスト環境での事前検証**。

---

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

---

## 📝 ライセンス

本リポジトリは [MIT ライセンス](./LICENSE) のもとで公開されています。

---



<!-- START_TREE -->
## プロジェクト構成  
├── [LICENSE](LICENSE)  
├── [README.md](README.md)  
├── [free.py](free.py)  
├── [free_input.xlsx](free_input.xlsx)  
├── [index.html](index.html)  
├── man/  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── [AWS対応Terraform動作環境構築.md](man/AWS%E5%AF%BE%E5%BF%9CTerraform%E5%8B%95%E4%BD%9C%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89.md)  
├── [requirements.txt](requirements.txt)  
└── templates/  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── [EC2.tf.j2](templates/EC2.tf.j2)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── [RDS.tf.j2](templates/RDS.tf.j2)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── [SG.tf.j2](templates/SG.tf.j2)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── [Subnet.tf.j2](templates/Subnet.tf.j2)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── [output.tf.j2](templates/output.tf.j2)  

2 directories, 12 files  
<!-- END_TREE -->

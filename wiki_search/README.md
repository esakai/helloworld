# Wikipedia Search Demo with LangChain and GPT-3.5

## 実装計画

### 1. 基本構造
- `wiki_search.py`: メインの実装ファイル
  - Wikipedia APIを使用して記事を検索
  - LangChainを使用してテキストを処理
  - GPT-3.5を使用して質問応答を実装

### 2. 主要機能
- Wikipediaからの記事取得と前処理
  - 記事の取得（日本語対応）
  - テキストの分割（ChunkSize=1000）
  - ベクトル化とインデックス作成（FAISS）

- 質問応答システム
  - ユーザーからの質問受付
  - 関連コンテキストの抽出
  - GPT-3.5による回答生成

### 3. エラーハンドリング
- APIキー未設定時のエラー処理
- Wikipedia記事が見つからない場合の処理
- API制限やネットワークエラーの処理

### 4. 使用方法
```bash
# 環境変数の設定
export OPENAI_API_KEY=your-api-key

# 実行
python wiki_search.py
```

### 5. 依存パッケージ
- langchain==0.3.17
- openai==1.61.1
- wikipedia-api==0.8.1
- python-dotenv==1.0.1
- faiss-cpu==1.10.0

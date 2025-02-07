import os
from typing import Optional
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.document_loaders import WikipediaLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

class WikiSearchError(Exception):
    pass

def check_api_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise WikiSearchError("OpenAI APIキーが設定されていません。.envファイルを確認してください。")

def search_wikipedia(query: str, language: str = "ja", test_mode: bool = False) -> Optional[RetrievalQA]:
    try:
        if test_mode:
            print(f"\nテストモード: '{query}'の検索をシミュレートします")
            return None
            
        loader = WikipediaLoader(query=query, lang=language)
        documents = loader.load()
        
        if not documents:
            raise WikiSearchError(f"'{query}'に関する記事が見つかりませんでした。")
        
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_documents(documents)
        
        embeddings = OpenAIEmbeddings()
        docsearch = FAISS.from_documents(texts, embeddings)
        
        qa = RetrievalQA.from_chain_type(
            llm=OpenAI(temperature=0),
            chain_type="stuff",
            retriever=docsearch.as_retriever()
        )
        
        return qa
    except Exception as e:
        if isinstance(e, WikiSearchError):
            raise e
        raise WikiSearchError(f"エラーが発生しました: {str(e)}")

def main() -> None:
    try:
        load_dotenv()
        test_mode = not os.getenv("OPENAI_API_KEY")
        
        if test_mode:
            print("\n注意: APIキーが設定されていないため、テストモードで実行します。")
        else:
            check_api_key()
        
        search_term = input("検索キーワードを入力してください: ")
        qa_chain = search_wikipedia(search_term, test_mode=test_mode)
        
        if test_mode:
            print("\nテストモード: 質問応答をシミュレートします。実際の回答には OpenAI APIキーが必要です。")
            return
            
        while True:
            question = input("\n質問を入力してください（終了する場合は'q'を入力）: ")
            if question.lower() == 'q':
                break
                
            result = qa_chain.run(question)
            print(f"\n回答: {result}")
            
    except WikiSearchError as e:
        print(f"\nエラー: {str(e)}")
    except KeyboardInterrupt:
        print("\n\nプログラムを終了します。")
    except Exception as e:
        print(f"\n予期せぬエラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()

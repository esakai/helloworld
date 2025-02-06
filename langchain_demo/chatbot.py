from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()

def create_chat():
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
    )
    return chat

def main():
    chat = create_chat()
    memory = ConversationBufferMemory()
    conversation = ConversationChain(
        llm=chat,
        memory=memory,
        verbose=False
    )
    
    print("チャットボットが起動しました。'終了'と入力すると終了します。\n")
    
    while True:
        try:
            user_input = input("ユーザー: ")
            if user_input.lower() in ['quit', 'exit', '終了']:
                break
            
            response = conversation.predict(input=user_input)
            print(f"\nアシスタント: {response}\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            break

if __name__ == "__main__":
    main()

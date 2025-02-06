from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv
import os

load_dotenv()

def create_chat():
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
    )

def create_conversation_chain():
    chat = create_chat()
    
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            "あなたは親切で役立つAIアシスタントです。ユーザーとの会話の文脈を理解し、適切な応答を心がけてください。"
        ),
        MessagesPlaceholder(variable_name="history"),
        HumanMessagePromptTemplate.from_template("{input}")
    ])
    
    memory = ConversationBufferMemory(return_messages=True)
    
    conversation = ConversationChain(
        memory=memory,
        prompt=prompt,
        llm=chat,
        verbose=False
    )
    
    return conversation

def main():
    conversation = create_conversation_chain()
    
    print("チャットボットが起動しました。'終了'と入力すると終了します。\n")
    
    while True:
        try:
            user_input = input("ユーザー: ").encode('utf-8').decode('utf-8')
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

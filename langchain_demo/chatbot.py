from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from dotenv import load_dotenv
import os

load_dotenv()

class InMemoryHistory(BaseChatMessageHistory):
    def __init__(self):
        self.messages = []
    
    def add_message(self, message):
        self.messages.append(message)
    
    def clear(self):
        self.messages = []

def create_chat():
    return ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.7,
    )

def create_conversation_chain():
    chat = create_chat()
    history = InMemoryHistory()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "あなたは親切で役立つAIアシスタントです。ユーザーとの会話の文脈を理解し、適切な応答を心がけてください。"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    
    chain = prompt | chat
    
    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: history,
        input_messages_key="input",
        history_messages_key="history"
    )
    
    return chain_with_history

def main():
    conversation = create_conversation_chain()
    
    print("チャットボットが起動しました。'終了'と入力すると終了します。\n")
    
    while True:
        try:
            user_input = input("ユーザー: ").encode('utf-8').decode('utf-8')
            if user_input.lower() in ['quit', 'exit', '終了']:
                break
            
            response = conversation.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": "default"}}
            )
            print(f"\nアシスタント: {response.content}\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            break

if __name__ == "__main__":
    main()

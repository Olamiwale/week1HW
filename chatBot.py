import os
from openai import OpenAI


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def ask_bot(question):
   
    message = {"role": "user", "content": question}
    
 
    model = "gpt-3.5-turbo"
    
   
    response = client.chat.completions.create(
        model=model,
        messages=[message],
        stream=True
    )
    
    
    response_content = next(response).choices[0].delta.content
    
    return response_content.strip()


if __name__ == "__main__":
    while True:
        user_question = input("How may I help you today: ")
        if user_question.lower() == 'exit':
            print("Exiting the chatbot. Goodbye!")
            break
        bot_answer = ask_bot(user_question)
        print("Bot:", bot_answer)

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)

model = ChatOpenAI(model="gpt-4o-mini")

# Get input from the user
prompt = input("Enter your prompt: ")

response = model.invoke(prompt)

print(response.content)


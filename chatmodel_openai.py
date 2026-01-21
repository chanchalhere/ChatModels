from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model='gpt-5-nano',temperature=1.5,max_completion_tokens=50)
result=model.invoke("who are you?")
print(result)
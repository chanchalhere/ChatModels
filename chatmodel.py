from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation"
)
conversation = [
    SystemMessage(content="You are a helpful and friendly assistant."),
    HumanMessage(content="Hi! Who is your godfather?")
]
model=ChatHuggingFace(llm=llm)
result=model.invoke(conversation)
print(result.content)

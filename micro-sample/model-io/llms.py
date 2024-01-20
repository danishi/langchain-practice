from langchain.llms import OpenAI

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
)

result = llm(
    "美味しいラーメンを作るには、",
    stop="。"
)
print(result)

from langchain.chat_models import ChatOpenAI
# from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

result = chat(
    [
        HumanMessage(content="こんにちは！")
    ]
)
print(result.content)

result = chat(
    [
        SystemMessage(content="あなたは関西人です。関西弁を使ってください。"),
        HumanMessage(content="こんにちは！")
    ]
)
print(result.content)

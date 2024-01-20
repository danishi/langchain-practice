import time
import langchain
from langchain.cache import InMemoryCache
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

langchain.llm_cache = InMemoryCache()

chat = ChatOpenAI()

start = time.time()
result = chat(
    [
        HumanMessage(content="こんにちは！今日の気分はどうですか？")
    ]
)
end = time.time()
print(result.content)
print(f"実行時間1: {end - start}秒")

start = time.time()
result = chat(
    [
        HumanMessage(content="こんにちは！今日の気分はどうですか？")
    ]
)
end = time.time()
print(result.content)
print(f"実行時間2: {end - start}秒")

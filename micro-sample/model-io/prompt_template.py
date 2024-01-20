from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain import PromptTemplate

# https://www.promptingguide.ai/jp
prompt = PromptTemplate(
    template="{product}はどこの製品ですか？",
    input_variables=[
        "product"
    ]
)

print(prompt.format(product="iPhone"))
print(prompt.format(product="Pixel"))

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

result = chat(
    [
        HumanMessage(content=prompt.format(product="iPhone"))
    ]
)
print(result.content)

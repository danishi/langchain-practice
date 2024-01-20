from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema import HumanMessage

output_parsers = CommaSeparatedListOutputParser()

chat = ChatOpenAI(
    model="gpt-3.5-turbo",
)

result = chat(
    [
        HumanMessage(content="都道府県をすべて答えてください。"),
        HumanMessage(content=output_parsers.get_format_instructions())
    ]
)
print(result.content)

output = output_parsers.parse(result.content)
print(output)
for item in output:
    print(item)

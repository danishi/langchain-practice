from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    streaming=True,
    callbacks=[
        StreamingStdOutCallbackHandler()
    ]
)
resp = chat([
    HumanMessage(content="美味しいカレーの作り方を教えて")
])


from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# uses env varaible OPENAI_API_KEY
llm = ChatOpenAI()

# llm.invoke("how can langsmith help with testing?")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

value = chain.invoke({"input": "how can langsmith help with testing?"})

print(value)
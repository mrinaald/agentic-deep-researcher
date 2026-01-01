# -*- coding: utf-8 -*-
# author: Mrinaal Dogra (mrinaald)

from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage

# Setup the Tool
search_tool = DuckDuckGoSearchRun()

# Setup the Model
# We use temperature=0 because we want precise tool usage, not creativity.
llm = ChatOllama(model="llama3.1", temperature=0)

# "Bind" the tool to the model
# This effectively appends a system prompt telling Llama 3.1:
# "You have a tool called 'duckduckgo_search'. Use it if needed."
llm_with_tools = llm.bind_tools([search_tool])

# Test Query
query = "What is the current stock price of NVIDIA? Answer briefly."
print(f"User: {query}")

# Invoke
response = llm_with_tools.invoke([HumanMessage(content=query)])

# Analyze the Result
print("\n--- LLM Response ---")
# If successful, 'content' might be empty, but 'tool_calls' will have data
print(f"Content: {response.content}")
print()
print(f"Tool Calls: {response.tool_calls}")

if response.tool_calls:
    print("\nSUCCESS: The model decided to use the tool!")
    print(f"Tool Name: {response.tool_calls[0]['name']}")
    print(f"Arguments: {response.tool_calls[0]['args']}")
else:
    print("\nFAILURE: The model tried to answer from memory.")

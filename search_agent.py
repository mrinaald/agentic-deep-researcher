# -*- coding: utf-8 -*-
# author: Mrinaal Dogra (mrinaald)

import argparse

from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage


class DeepSearchReActAgent:
    def __init__(self, model_name="llama3.1",  verbose: bool = False):
        self.tools = [DuckDuckGoSearchRun()]
        self.model_name = model_name
        self.model = ChatOllama(model=model_name, temperature=0)

        # Creating the ReAct Agent
        self.agent_graph = create_agent(self.model, self.tools, debug=verbose)

    def research(self, query: str) -> str:
        print("Starting Research...")
        inputs = {"messages": [HumanMessage(content=query)]}

        response = self.agent_graph.invoke(inputs)

        print("\n--- Final Report ---")
        # The response 'messages' list contains the full conversation:
        # [UserQuery, AI_ToolCall, ToolOutput, AI_FinalAnswer]
        # We want the last message (i.e., the final answer).
        print(response["messages"][-1].content)

        # # If we want to stream (for future references)
        # for chunk in agent_graph.stream(inputs, stream_mode="updates"):
        #     print(chunk)
        # print()
        # print(chunk["model"]["messages"][-1].content)

def _main():
    parser = argparse.ArgumentParser(description="Research ReAct Agent")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    args = parser.parse_args()

    agent = DeepSearchReActAgent(verbose=args.verbose)
    while True:
        print("="*50)
        user_query = input("Enter your research query (or type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break
        print()
        agent.research(user_query)
        print("="*50)
        print()


if __name__ == "__main__":
    _main()

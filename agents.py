

from langchain.agents import create_agent
from llm import llm
from tools import tool_kit

agent_executor = create_agent(model=llm, tools=tool_kit) 


if __name__ == "__main__":
    print("Agent Graph compiled successfully. Initializing test streams...\n")
    
    # 1. Test Natural Language Math Translation
    math_query = {"messages": [("user", "What is twenty divided by five?")]}
    print(f"User Question: {math_query['messages'][0][1]}")
    
    math_response = agent_executor.invoke(math_query)
    # The final answer will be inside the last index of the message list
    print("Agent Response:", math_response["messages"][-1].content)
    print("-" * 50)
    
    # 2. Test Wikipedia Factual Fetching
    wiki_query = {"messages": [("user", "what is population of India? and multiply 0.75 to it.")]}
    print(f"User Question: {wiki_query['messages'][0][1]}")
    
    wiki_response = agent_executor.invoke(wiki_query)
    print("Agent Response:", wiki_response["messages"][-1].content)
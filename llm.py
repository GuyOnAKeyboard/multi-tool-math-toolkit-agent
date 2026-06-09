from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="qwen2.5:1.5b",
)

if __name__=="__main__":
    response = llm.invoke("What is tool calling in langchain?")
    print("\nResponse Content: ", response.content)
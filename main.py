from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool


@tool("SayHello", return_direct=True)
def say_hello(name: str) -> str:
    """Answer when someone say hello"""
    return f"Hello {name}! My name is Sainapsis"


@tool("eciResponse", return_direct=True)
def resp_query(query: str) -> str:
    """Answer when someone say something about ECI Julio Garavito"""
    return f"Hello, "


def main():
    llm = ChatOpenAI(temperature=0)
    tools = [
        say_hello
    ]
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    print(agent.run("Hello! My name is Camilo"))


if __name__ == "__main__":
    main()


"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
RetrievalQA(llm=OpenAI().chain_type="refine")
index.as_retriever(tipo="similarity")
"""

import os
from importlib.metadata import version

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter

load_dotenv()

core_version = version("langchain-core")
langgraph_version = version("langgraph")


def main():
    print(f"langchain-core version: {core_version}")
    print(f"langgraph version: {langgraph_version}")

    # Test OpenRouter
    api_key = os.getenv("OPENROUTER_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY is missing. Check your .env file."
        )

    llm = ChatOpenRouter(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        temperature=0,
        api_key=api_key,
    )

    response = llm.invoke("Say 'setup complete!'")

    print(f"Response from OpenRouter: {response.content}")
    print("Setup complete!")


if __name__ == "__main__":
    main()
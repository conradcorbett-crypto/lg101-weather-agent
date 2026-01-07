from agents.lg101_weather_agent import agent

def ask_agent(question: str):
    """Send a question to the agent and return the response."""
    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return result["messages"][-1].content

if __name__ == "__main__":
    # Example: Recommend a comedy movie
    question = "recommend a comedy movie"

    print(f"\nQuestion: {question}")
    print("=" * 50)

    response = ask_agent(question)

    print(f"\nResponse: {response}\n")

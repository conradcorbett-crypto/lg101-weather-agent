# Install SDK: pip install langgraph-sdk
import os
from pathlib import Path
from dotenv import load_dotenv
from langgraph_sdk import get_sync_client

# Load environment variables from .env file
project_root = Path(__file__).resolve().parent
load_dotenv(dotenv_path=project_root / ".env", override=True)

# Use your deployment's API URL and LangSmith API key (from .env file)
client = get_sync_client(
    url="https://cc-testing-weather-agent-88cc91b82b285fee8e2e3a24e4d3df8c.us.langgraph.app",
    api_key=os.getenv("LANGSMITH_DEPLOYMENT_API_KEY")
)

# Stream a threadless run to your "agent" (defined in langgraph.json)
print("Streaming agent response...\n")

final_state = None
for chunk in client.runs.stream(
    None,  # New thread
    "LG101 Weather Agent",  # Assistant/graph name from langgraph.json
    input={
        "messages": [{"role": "human", "content": "recommend a sci-fi movie"}]
    },
    stream_mode="updates"
):
    print(chunk)

final_message = chunk.data
print("\n" + "="*50)
print("FINAL MESSAGE:")
print("="*50)
print(final_message["model"]["messages"][-1]["content"])
print("="*50)
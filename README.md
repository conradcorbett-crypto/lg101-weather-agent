# lg101-weather-agent
## Setup
### Package Installation
Ensure you have a recent version of pip and python installed
```

# Install the package, allowing for pre-release 
uv sync

# Activate the virtual environment
source .venv/bin/activate
```

### Running Langsmith Studio locally
Add --allow-blocking
```

langgraph dev --allow-blocking
```

### Invoking the agent locally
Add --allow-blocking
```

python ./test_agent.py
```
## LangSmith Deployments
### Deploy your app using the LangSmith Deployments UI. Hook LangSmith Deployments up to the github repo
LangSmith SDK
```

# Use the LangSmith SDK to invoke your application
python ./langsmith_deployment.py
```
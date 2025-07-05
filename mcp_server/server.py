# Enhanced MCP server with improved comments and structure

from fastapi import FastAPI, HTTPException
from gateway.agent_registry import AgentRegistry
from gateway.routing import route_message

# Initialize FastAPI application
app = FastAPI()

# Initialize the Agent Registry
agent_registry = AgentRegistry()

@app.get("/health")
def health_check():
    """Endpoint to check the health of the MCP server."""
    return {"status": "healthy"}

@app.post("/process")
def process_message(agent_name: str, message: dict):
    """Endpoint to process a message using a specified agent.

    Args:
        agent_name (str): The name of the agent to process the message.
        message (dict): The message to be processed.

    Returns:
        dict: The processed message or an error if the agent is not found.
    """
    agent = agent_registry.agents.get(agent_name)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return route_message(agent, message)

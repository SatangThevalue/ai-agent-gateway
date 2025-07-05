# Enhanced Agent Registry with improved comments and structure

class AgentRegistry:
    """Registry to manage agent registration and discovery."""

    def __init__(self):
        # Dictionary to store registered agents and their metadata
        self.agents = {}

    def register_agent(self, name, metadata):
        """Register a new agent with its metadata.

        Args:
            name (str): The name of the agent.
            metadata (dict): Metadata describing the agent's capabilities.
        """
        self.agents[name] = metadata

    def discover_agent(self, capability):
        """Discover agents based on a specific capability.

        Args:
            capability (str): The capability to search for.

        Returns:
            list: A list of agents matching the capability.
        """
        return [agent for agent, meta in self.agents.items() if capability in meta.get("capabilities", [])]

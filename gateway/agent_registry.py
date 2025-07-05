# Agent registration/discovery

class AgentRegistry:
    def __init__(self):
        self.agents = {}

    def register_agent(self, name, metadata):
        self.agents[name] = metadata

    def discover_agent(self, capability):
        return [agent for agent, meta in self.agents.items() if capability in meta.get("capabilities", [])]

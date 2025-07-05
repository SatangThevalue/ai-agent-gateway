# Context handling

class ContextManager:
    def __init__(self):
        self.contexts = {}

    def store_context(self, key, value):
        self.contexts[key] = value

    def get_context(self, key):
        return self.contexts.get(key)

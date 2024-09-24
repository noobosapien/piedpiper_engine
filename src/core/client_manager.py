from .agent_queue import AgentQueue


class ClientManager:
    _capacity_full = False

    def __init__(self):
        pass

    def at_capacity(self):
        return self._capacity_full

    def to_process(self, client_queue: AgentQueue):
        pass

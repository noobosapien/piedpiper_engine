from .client_queue import ClientQueue


class AgentManager:
    _capacity_full = False
    _agents = []

    def __init__(self):
        pass

    def at_capacity(self):
        return self._capacity_full

    def to_process(self, client_queue: ClientQueue):
        pass

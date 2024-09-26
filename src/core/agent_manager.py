from typing import Dict, List

from .client_queue import ClientQueue
from .agent import Agent


class AgentManager:
    _capacity_full = False
    _client_to_agent: Dict[str, List[Agent]] = {}

    def __init__(self):
        pass

    def at_capacity(self):
        return self._capacity_full

    def to_process(self, client_queue: ClientQueue):
        pass

    def add_agent(self, client, agent):
        pass

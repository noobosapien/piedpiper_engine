from typing import List


class AgentQueue:
    def __init__(self, agent):
        self._messages: List[str] = []
        self._agent = agent

    def is_agent(self, agent):
        pass

    def is_agent_by_id(self, agent_id):
        pass

    def add_message(self, input):
        pass

    def is_empty(self):
        return False

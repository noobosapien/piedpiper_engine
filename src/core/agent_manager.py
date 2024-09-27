import asyncio

from typing import Dict, List

from .client_queue import ClientQueue
from .agent import Agent
from .agent_manager_thread import AgentManagerThread
from .agent_processor import AgentProcessor


class AgentManager:
    _client_to_agent: Dict[str, List[Agent]] = {}

    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.agent_manager_thread = AgentManagerThread(self.loop)
        self.agent_manager_thread.start()
        self.agent_processor = AgentProcessor(self.loop)
        self.agent_processor.start()

    def to_process(self, client_queue: ClientQueue):
        pass

    def add_agent(self, client, agent):
        pass

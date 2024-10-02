from typing import List
import asyncio

from core.client import Client
from core.agent import Agent
from core.client_queue import ClientQueue
from core.client_manager import ClientManager
from core.agent_queue import AgentQueue
from core.agent_manager import AgentManager
from .engine_manager_thread import EngineManagerThread


class ClientToQueues:
    def __init__(self, client_id, client_queue, agent_queue):
        self.client_id = client_id
        self.client_queue = client_queue
        self.agents = []
        self.agent_queue = agent_queue


class Engine:
    # Only use agent queue if there is an output, if the agent is functional this queue will not be used

    def __init__(self):
        self._all_queues: List[ClientToQueues] = []
        self._loop = asyncio.new_event_loop()

        self._agent_manager = AgentManager(engine=self)
        self._client_manager = ClientManager()

        self._engine_manager_thread = EngineManagerThread(self._loop)
        self._engine_manager_thread.start()
        self._engine_manager_futures = []

    def get_loop(self):
        return self._loop

    def _find_client_queue_(self, client_id) -> ClientQueue:
        for ctq in self._all_queues:
            if ctq.client_id == client_id:
                return ctq.client_queue

        return None

    def _find_client_to_queue_(self, client_id):
        for ctq in self._all_queues:
            if ctq.client_id == client_id:
                return ctq

        return None

    def clear_queues(self):
        self._all_queues = []

    def add_client(self, client: Client):
        cl = self._find_client_queue_(client._id)

        if cl is not None:
            return

        client.add_engine(self)
        client_queue = ClientQueue(client)
        agent_queue = None

        ctq = ClientToQueues(client._id, client_queue, agent_queue)

        self._all_queues.append(ctq)

    def add_agent(self, client: Client, agent: Agent = None):
        ctq = self._find_client_to_queue_(client._id)

        if ctq is None or agent is None:
            return

        agent.add_engine(self)
        ctq.agents.append(agent)
        aq = AgentQueue(agent)
        ctq.agent_queue = aq

    def remove_client(self, client: Client):
        self._all_queues = list(
            filter(lambda ctq: (ctq.client_id != client._id), self._all_queues)
        )

    def add_message(self, client_id, input):
        ctq = self._find_client_to_queue_(client_id)

        if ctq is not None:
            ctq.client_queue.add_message(input)

        self._engine_manager_futures.append(
            asyncio.run_coroutine_threadsafe(self.process(), self._loop)
        )

    async def process(self):
        for ctq in self._all_queues:
            if ctq.client_queue._is_new:
                await self._agent_manager.to_process(ctq)

    def loop(self):
        pass

    def quit(self):
        if self._agent_manager is not None:
            self._agent_manager.quit()

from typing import Dict
from multiprocessing import Process, Value
from ctypes import c_bool

from core.client import Client
from core.client_queue import ClientQueue
from core.client_manager import ClientManager
from core.agent_queue import AgentQueue
from core.agent_manager import AgentManager


class Engine:
    # Only use agent queue if there is an output, if the agent is functional this queue will not be used
    _all_queues: Dict[str, Dict[ClientQueue, AgentQueue]] = {}

    _agent_manager = AgentManager()
    _client_manager = ClientManager()

    _loop_process: Process = None
    _set_quit_loop = Value(c_bool, False)

    def __init__(self):
        pass

    def _find_client_queue_(self, client_id) -> ClientQueue:
        for id, queues in self._all_queues.items():
            if id == client_id:
                return list(queues.keys())[0]

        return None

    def clear_queues(self):
        self._all_queues = {}

    def add_client(self, client: Client):
        cl = self._find_client_queue_(client._id)

        if cl is not None:
            return

        client.add_engine(self)
        client_queue = ClientQueue(client)
        agent_queue = AgentQueue()

        self._all_queues[client._id] = {client_queue: agent_queue}

    def remove_client(self, client: Client):
        del self._all_queues[client._id]

    def add_message(self, client_id, input):
        cq = self._find_client_queue_(client_id)

        if cq is not None:
            cq.add_message(input)

    def process(self):
        while True:
            if self._set_quit_loop.value is True:
                break

            for _, queues in self._all_queues:
                for cq, aq in queues:
                    if not cq.is_empty():
                        self._agent_manager.to_process(cq)
                    if not aq.is_empty():
                        self._client_manager.to_process(aq)  # Optional

    def loop(self):
        self._loop_process = Process(target=self.process)
        self._loop_process.start()

    def quit(self):
        self._set_quit_loop.value = True
        self._loop_process.join()

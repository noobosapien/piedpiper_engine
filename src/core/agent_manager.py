import asyncio
from concurrent.futures import ThreadPoolExecutor
import functools

from .agent import Agent
from .client import Client
from .client_queue import ClientQueue


class NoAgentToClient(Exception):
    pass


class AgentManager:
    def __init__(self, engine=None):
        self._engine = engine
        self.loop = engine.get_loop()
        self.tasks = []

    async def to_process(self, ctq):
        with ThreadPoolExecutor() as pool:
            while ctq.client_queue.is_empty() is False:
                self.tasks.append(
                    self.loop.run_in_executor(
                        pool,
                        ctq.agents[0].process(
                            ctq.client_id, ctq.client_queue.get_next_message()
                        ),
                    )
                )

                print("Tasks: ", len(self.tasks))
                # for task in self.tasks:
                #     print(task.exception())

            results = await asyncio.gather(*self.tasks)
            print(results)

    def quit(self):
        # self.agent_processor.cancel_all()
        pass

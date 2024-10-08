import asyncio
from concurrent.futures import ThreadPoolExecutor
import functools


class NoAgentToClient(Exception):
    pass


class AgentManager:
    def __init__(self, engine=None):
        self._engine = engine
        self.loop = engine.get_loop()
        self.tasks = []

    def clear_finished_tasks(self):
        self.tasks = list(
            filter(
                lambda task: (task.done() is False),
                self.tasks,
            )
        )

    async def to_process(self, ctq):
        with ThreadPoolExecutor() as pool:
            while ctq.client_queue.is_empty() is False:
                self.tasks.append(
                    self.loop.run_in_executor(
                        pool,
                        functools.partial(
                            ctq.agents[0].process,
                            ctq.client._id,
                            ctq.client_queue.get_next_message(),
                        ),
                    )
                )

            for result in asyncio.as_completed(self.tasks):
                self.clear_finished_tasks()

                agent_out = await result

                # print("Agent out: ", agent_out[1].serialize())

                self._engine.add_agent_output(agent_out[0], agent_out[1])

    def quit(self):
        # self.agent_processor.cancel_all()
        pass

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
                            ctq.client_id,
                            ctq.client_queue.get_next_message(),
                        ),
                    )
                )

            # for task in self.tasks:
            print("Tasks: ", len(self.tasks))

            # results = await asyncio.gather(*self.tasks)
            for results in asyncio.as_completed(self.tasks):
                self.clear_finished_tasks()

                # print(await results)
                # print(type(results))
                # await results
                print(await results)

    def quit(self):
        # self.agent_processor.cancel_all()
        pass

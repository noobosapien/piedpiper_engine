from multiprocessing import Queue

from piedpiper_engine import Event, System, SystemLastEvent, SystemQuitEvent


def get_example_system():
    class NewSystem(System):
        def __init__(self, in_queue, out_queue):
            super().__init__(in_queue, out_queue)
            self.last_event: Event = None

        def run(self):
            while True:
                for queue in self.in_queues:
                    if queue.empty():
                        continue

                    event = queue.get()

                    match event:
                        case SystemQuitEvent():
                            self.set_quit(True)

                        case SystemLastEvent():
                            for queue in self.out_queues:
                                queue.put(self.last_event)

                        case _:
                            self.last_event = event

                if self.get_quit():
                    return

    system = NewSystem(Queue(), Queue())

    return system

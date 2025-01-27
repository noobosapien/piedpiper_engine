from abc import ABC, abstractmethod
from multiprocessing import Process, Queue
from multiprocessing.synchronize import Condition


class System(ABC, Process):
    """Abstract system class of the engine, also inherits a process. Systems are the main processing units
    of the engine, every system must be inherited from this class."""

    def __init__(self, queue: Queue, condition: Condition):
        """
        Initializes a system.

        Args:
            queue (multiprocessing.Queue): The queue from the engine that brings the event.
            condition (multiprocessing.synchronize.Condition): The condition that lets the new events to be processed.

        """
        Process.__init__(self)

        self.queue: Queue = queue
        self.condition: Condition = condition

    @abstractmethod
    def run(self):
        """The run method that is neccasary for the Process class, it is an abstract method.
        This must be made by the inherited system.
        """
        pass

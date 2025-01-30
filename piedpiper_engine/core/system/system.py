import uuid
from abc import ABC, abstractmethod
from multiprocessing import Process, Queue
from typing import List, Optional, Tuple


class System(ABC, Process):
    """Abstract system class of the engine, also inherits a process. Systems are the main processing units
    of the engine, every system must be inherited from this class."""

    def __init__(self, in_queue: Optional[Queue], out_queue: Optional[Queue]) -> None:
        """
        Initializes a system with two queues, one for getting the events from outside and the other to send events
        to the outside. THe queues are appended to a list so more than one queue can get and recieve events.

        Args:
            in_queue (Optional[multiprocessing.Queue]): The queue from the engine that brings an event.
            out_queue (Optional[multiprocessing.Queue]): The queue from the system that sends an event.
        """
        Process.__init__(self)

        self.in_queues: List[Queue] = []
        self.out_queues: List[Queue] = []

        if in_queue:
            self.in_queues.append(in_queue)

        if out_queue:
            self.out_queues.append(out_queue)

        self.__id: str = "sys_" + str(uuid.uuid4())
        self.__quit: bool = False

    @abstractmethod
    def run(self) -> None:
        """The run method that is neccasary for the Process class, it is an abstract method.
        This must be made by the inherited system.
        """
        pass

    def get_id(self) -> str:
        """Returns the id of the system.

        Returns:
            str: id of the system.
        """
        return self.__id

    def get_new_queues(self) -> Tuple[Queue, Queue]:
        """Creates a new set of queues, one for incoming events and the other for outgoing events.

        Returns:
            Tuple[Queue, Queue]: The two queues, first is the incoming event queue, and the other one is
            the outgoing event queue from the system.
        """
        sys_in: Queue = Queue()
        sys_out: Queue = Queue()

        self.in_queues.append(sys_in)
        self.out_queues.append(sys_out)

        return (sys_in, sys_out)

    def set_quit(self, quit: bool) -> None:
        """Set whether to quit the engine, handled in the run method of the process.

        Args:
            quit (bool): Set to either True or False
        """
        self.__quit = quit

    def get_quit(self) -> bool:
        """Get whether the quit value of the engine is set to true or false, handled in the run method of
        the process.

        Returns:
            bool: The quit value of the system
        """
        return self.__quit

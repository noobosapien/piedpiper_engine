from multiprocessing import Process, Queue
from time import sleep
from typing import Dict, Tuple
from uuid import uuid4

from piedpiper_engine.classes.engine.engine_events import EngineQuitEvent
from piedpiper_engine.classes.event import Event
from piedpiper_engine.classes.system.system_events import SystemEvent, SystemQuitEvent
from piedpiper_engine.core.engine.context import Context
from piedpiper_engine.core.engine.event_store import EventStore
from piedpiper_engine.core.system import System


class Engine(Process):
    """The main class of the event engine it inherits from a process."""

    def __init__(self) -> None:
        """Initializes the engine and the parent process."""

        Process.__init__(self)
        self.__context: Context = Context()
        self.__event_store: EventStore = EventStore()

        self.__in_queue: Queue = Queue()
        self.__systems: Dict[str, Tuple[System, Queue, Queue]] = {}

    def get_context(self) -> Context | None:
        """Get the context object of the engine.

        Returns:
            Context | None: context
        """
        return self.__context

    def get_event_store(self) -> EventStore | None:
        """Get the EventStore object of the engine.

        Returns:
            EventStore | None: event_store
        """
        return self.__event_store

    def get_in_queue(self) -> Queue:
        """Get the inwards queue of the engine, this is the only way of communication of the engine
        when it is processing.

        Returns:
            Queue | None: in_queue
        """
        return self.__in_queue

    def add_system(self, system: System) -> None:
        """Add a new system to the engine.
        The engine stores system ids to the queues of the system and the system as a tuple

        Args:
            system (System): new system to be added.
        """
        queues: Tuple[Queue, Queue] = system.get_new_queues()
        self.__systems[system.get_id()] = (system, queues[0], queues[1])

    def get_systems_len(self) -> int:
        """Gets the number of systems in the engine.

        Returns:
            int: The number of systems.
        """
        return len(self.__systems)

    def add_event(self, event: SystemEvent) -> None:
        """Adds the event to the event store with the system id.

        Args:
            event (SystemEvent): The SystemEvent to be catalouged.
        """
        self.__event_store.add_event_to_system(event)

    def run(self) -> None:
        """The run method of the process where there is a continuous loop looking for new events."""
        while True:
            if not self.__in_queue.empty():
                event = self.__in_queue.get()

                if isinstance(event, EngineQuitEvent):
                    self.__quit_engine()
                    break

                self.__process_event(event)

            sleep(0.1)

    def __process_event(self, event: SystemEvent) -> None:
        """Private method for processing the recieved events from the in_queue.

        Args:
            event (Event): The event to be processed.
        """

        try:
            sys_id = event.sys_id
            system = self.__systems[sys_id]

            system[1].put(event)
        except KeyError:
            print("System not found")

    def __quit_engine(self) -> None:
        """For every system in the engine send the SystemQuitEvent and wait for the system to break out of the loop
        and join that process.
        """

        for _, sys in self.__systems.items():
            sys[1].put(
                SystemQuitEvent(id="event_" + str(uuid4()), sys_id=sys[0].get_id())
            )

            del sys

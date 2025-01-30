from typing import Dict, List

from piedpiper_engine.classes.system.system_events import SystemEvent


class EventStore:
    """The class that matches events with the system workflows."""

    def __init__(self):
        """Initialize the EventStore."""
        self.system_to_event: Dict[str, List[SystemEvent]] = {}

        pass

    def add_event_to_system(self, event: SystemEvent) -> None:
        """Adds the event to the system's list.

        Args:
            event (SystemEvent): The event to add to the system (SystemEvent already has the system_id)
        """
        try:
            events = self.system_to_event[event.sys_id]
            events.append(event)
        except KeyError:
            self.system_to_event[event.sys_id] = [event]

    def get_system_from_event(self, event: SystemEvent) -> str:
        """Gets the id of the system the event belongs to.

        Args:
            event (SystemEvent): The event to lookup.

        Returns:
            str: The id of the system the event belongs.
        """
        return event.sys_id

from dataclasses import dataclass

from piedpiper_engine.classes.event import Event


@dataclass(kw_only=True)
class SystemEvent(Event):
    """Base dataclass for events exposed by systems.

    Args:
        Event (SystemEvent): Base dataclass of a system event.
    """

    id: str
    sys_id: str


@dataclass(kw_only=True)
class SystemLastEvent(SystemEvent):
    """Event to get the last event handled by the system.

    Args:
        Event (SystemLastEvent): Event to get the last event handled by the system.
    """

    pass


@dataclass(kw_only=True)
class SystemQuitEvent(SystemEvent):
    """Event to quit the system.

    Args:
        Event (SystemQuitEvent): Event to quit the system.
    """

    pass

from dataclasses import dataclass

from piedpiper_engine.classes.event import Event


@dataclass(kw_only=True)
class EngineQuitEvent(Event):
    """Event to shutdown the engine

    Args:
        Event (EngineQuitEvent): Event to shutdown the engine
    """

    id: str

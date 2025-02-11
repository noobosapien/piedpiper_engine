from dataclasses import dataclass

from piedpiper_engine.classes.event import Event


@dataclass(kw_only=True)
class ModuleEvent(Event):
    """Base dataclass for events exposed by modules.

    Args:
        Event (ModuleEvent): Base dataclass of a module event.
    """

    id: str
    mod_id: str


@dataclass(kw_only=True)
class ModuleAsyncEvent(ModuleEvent):
    """Asynchrounous event from an asynchronous module.

    Args:
        ModuleEvent (ModuleEvent): Asynchrounous event from an asynchronous module.
    """

    pass


@dataclass(kw_only=True)
class ModuleSyncEvent(ModuleEvent):
    """Synchrounous event from a synchronous module.

    Args:
        ModuleEvent (ModuleEvent): Synchrounous event from a synchronous module.
    """

    pass

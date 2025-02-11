from typing import Type

from piedpiper_engine.classes.system import ModuleSyncEvent
from piedpiper_engine.core.system.module import Module


class ModuleSync(Module):
    """The Module class that handles synchronous operations of a workflow.

    Args:
        Module: The main Module class that the SyncModule is inherited from.
    """

    def __init__(self) -> None:
        """Creates an instance of a ModuleSync class which can handle synchronous functions"""
        super().__init__()

    def process(
        self, last_event: Type[ModuleSyncEvent]
    ) -> Type[ModuleSyncEvent] | None:
        """Process an event synchronously and returns a processed event.

        Args:
            last_event (Event): The last event of the previous module.

        Returns:
            Event | None: Outputs a processed event.
        """
        pass

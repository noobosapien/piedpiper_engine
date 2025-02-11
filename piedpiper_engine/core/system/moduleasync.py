from typing import Type

from piedpiper_engine.classes.system import ModuleAsyncEvent
from piedpiper_engine.core.system.module import Module


class ModuleAsync(Module):
    """The Module class that handles async operations of a workflow.

    Args:
        Module: The main Module class that the AsyncModule is inherited from.
    """

    def __init__(self) -> None:
        """Creates an instance of a ModuleAsync class which can handle async functions"""
        super().__init__()

    async def process(
        self, last_event: Type[ModuleAsyncEvent]
    ) -> Type[ModuleAsyncEvent] | None:
        """Process an event asynchronously and returns a processed event.

        Args:
            last_event (Event): The last event of the previous module.

        Returns:
            Event | None: Outputs a processed event.
        """
        pass

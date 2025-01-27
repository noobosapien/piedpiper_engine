from piedpiper_engine.core.engine.context import Context


class Engine:
    """The main class of the event engine."""

    def __init__(self) -> None:
        """Initializes the engine."""

        self.context: Context = Context()

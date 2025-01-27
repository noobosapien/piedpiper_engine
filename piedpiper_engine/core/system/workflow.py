from abc import ABC, abstractmethod


class Workflow(ABC):
    """An abstract class that needs to be inherited from to create custom workflows of systems."""

    @abstractmethod
    def __init__(self):
        """Initialize a Workflow class"""
        pass

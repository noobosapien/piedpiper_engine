from typing import Any, Dict

from piedpiper_engine.core.system import System


class Context:
    """The class that holds the context of the engine and the functionality related to it."""

    def __init__(self):
        """Initializes the context of the engine. Creates a dictionary to hold
        global values, and a dictionary to hold system values."""
        self.globals: Dict[str, Any] = {}
        self.sys_values: Dict[str, Dict[str, Any]] = {}

    def set_global(self, name: str, value: Any) -> None:
        """Sets a value to the global store.

        Args:
            name (str): Name of the global value.
            value (Any): The value to store.
        """

        self.globals[name] = value

    def get_global(self, name: str) -> Any:
        """Get the value stored in the global scope, if there is no such value return None.

        Args:
            name (str): Name of the value to return.

        Returns:
            Any: Returns the value if present or else returns None
        """

        try:
            return self.globals[name]
        except KeyError:
            return None

    def remove_global(self, name: str) -> None:
        """Removes a value from the global scope of the context.

        Args:
            name (str): Name of the value to be removed.
        """
        try:
            del self.globals[name]
        except KeyError:
            pass

    def set_value(self, system: System, name: str, value: Any) -> None:
        """Sets a value to the context of the system with the given name.

        Args:
            system (System): The system to add to.
            name (str): Name of the value.
            value (Any): The value.
        """
        if system.get_id() in self.sys_values:
            ctx = self.sys_values[system.get_id()]
            ctx[name] = value
        else:
            self.sys_values[system.get_id()] = {name: value}

    def get_value(self, system: System, name: str) -> Any:
        """Returns the value in a system context which has the specific name.

        Args:
            system (System): The system the context belongs to.
            name (str): The name of the value.

        Returns:
            Any: The value that is returned.
        """
        try:
            ctx = self.sys_values[system.get_id()]
            return ctx[name]
        except KeyError:
            return None

    def remove_value(self, system: System, name: str) -> None:
        """Removes a specific value by the name.

        Args:
            system (System): System the context belongs to.
            name (str): Name of the value to be removed
        """
        try:
            ctx = self.sys_values[system.get_id()]
            del ctx[name]
        except KeyError:
            pass

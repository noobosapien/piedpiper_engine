from dataclasses import dataclass


@dataclass(kw_only=True)
class Event:
    """The event class that is extended from the BaseModel"""

    id: str

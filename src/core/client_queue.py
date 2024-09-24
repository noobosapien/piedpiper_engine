from typing import List
from .client import Client


class ClientQueue:
    def __init__(self, client: Client):
        self._messages: List[str] = []
        self._client = client

    def is_client(self, client: Client) -> bool:
        if client._id == self._client._id:
            return True
        return False

    def is_client_by_id(self, client_id):
        if client_id == self._client._id:
            return True
        return False

    def add_message(self, input: str):
        self._messages.append(input)

    def get_next_message(self):
        if len(self._messages) > 0:
            message = self._messages[0]
            self._messages.pop(0)
            return message
        else:
            return None

    def is_empty(self):
        return len(self._messages) == 0

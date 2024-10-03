import uuid
import requests


class Agent:
    def __init__(self, engine=None):
        self._id = uuid.uuid4().hex
        self.engine = engine

    def add_engine(self, engine):
        self.engine = engine

    def process(self, client_id, client_msg):
        response = requests.get(client_msg)
        return (client_id, response.status_code)

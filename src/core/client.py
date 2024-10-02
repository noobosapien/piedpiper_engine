import uuid


class Client:
    def __init__(self, id=None, engine=None):
        self._engine = engine

        if id is None:
            self._id = uuid.uuid4().hex
        else:
            self._id = id

    def add_engine(self, engine):
        if self._engine is None:
            self._engine = engine

    def process(self, input):
        if self._engine is not None:
            self._engine.add_message(self._id, input)

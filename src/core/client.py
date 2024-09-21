from piedpiper_engine.engine import Engine


class Client:
    def __init__(self):
        self._engine: Engine = None
        self._id = None

    def add_engine(self, engine: Engine):
        if self._engine is None:
            self._engine = engine

    def process(self, input):
        if self._engine is not None:
            self._engine.add_message(self._id, input)

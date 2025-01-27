from multiprocessing import Condition as create_condition
from multiprocessing import Queue

import pytest

from piedpiper_engine import System


def test_unit_system_is_abstract():
    with pytest.raises(TypeError):
        queue = Queue()
        condition = create_condition()

        s = System(queue, condition)

        s.start()
        s.join()


def test_unit_system_validation():
    class newSys(System):
        def __init__(self, queue, condition):
            System.__init__(self, queue, condition)

        def run(self):
            pass

    queue = Queue()
    condition = create_condition()

    s = newSys(queue, condition)

    s.start()
    s.join()

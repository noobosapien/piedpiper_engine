import pytest

from piedpiper_engine import Engine
from tests.factoriies.event_factory import (
    get_engine_quit_event,
    get_example_event,
    get_last_event,
)
from tests.factoriies.system_factory import get_example_system


def test_unit_engine_validation():
    _ = Engine()


def test_unit_engine_have_context():
    engine = Engine()

    if engine.get_context() is None:
        raise ValueError


def test_unit_engine_have_event_store():
    engine = Engine()

    if engine.get_event_store() is None:
        raise ValueError


def test_unit_engine_has_inward_queue():
    engine = Engine()

    if engine.get_in_queue() is None:
        raise ValueError


def test_unit_engine_can_add_system():
    engine = Engine()

    engine.add_system(get_example_system())

    assert engine.get_systems_len() == 1


def test_unit_engine_runs_until_exit_event():
    engine = Engine()
    queue = engine.get_in_queue()

    engine.start()
    queue.put(get_engine_quit_event())
    engine.join()


@pytest.mark.timeout(2)
def test_unit_engine_sends_event_to_correct_system():
    engine = Engine()

    system = get_example_system()
    event = get_example_event(system)
    l_event = get_last_event(system)

    engine.add_system(system)
    engine.add_event(event)
    engine.add_event(l_event)

    eng_queue = engine.get_in_queue()
    (_, sys_out) = system.get_new_queues()

    engine.start()
    system.start()

    eng_queue.put(event)
    eng_queue.put(l_event)
    from_sys = sys_out.get()

    eng_queue.put(get_engine_quit_event())

    engine.join()

    assert event.id == from_sys.id

from piedpiper_engine import EventStore
from tests.factoriies.event_factory import get_example_event
from tests.factoriies.system_factory import get_example_system


def test_unit_event_store_validation():
    try:
        _ = EventStore()

    except Exception as e:
        raise e


def test_unit_event_store_add_and_get_event_to_system():
    system = get_example_system()
    event = get_example_event(system)

    es = EventStore()

    es.add_event_to_system(event)

    sys_from_es = es.get_system_from_event(event)

    assert sys_from_es == system.get_id()

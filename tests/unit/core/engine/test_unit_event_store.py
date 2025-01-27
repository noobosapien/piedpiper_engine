from piedpiper_engine import EventStore


def test_unit_event_store_validation():
    try:
        _ = EventStore()

    except Exception as e:
        raise e

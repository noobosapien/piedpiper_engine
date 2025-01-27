from piedpiper_engine import Engine


def test_unit_engine_validation():
    try:
        _ = Engine()

    except Exception as e:
        raise e

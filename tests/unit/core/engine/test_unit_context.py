from piedpiper_engine import Context


def test_unit_context_validation():
    try:
        _ = Context()

    except Exception as e:
        raise e

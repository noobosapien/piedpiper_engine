from piedpiper_engine import Context
from tests.factoriies.system_factory import get_example_system


def test_unit_context_validation():
    try:
        _ = Context()

    except Exception as e:
        raise e


def test_unit_context_add_and_get_global_value():
    context = Context()

    context.set_global("test_value", 24)
    assert 24 == context.get_global("test_value")

    context.set_global("test_value", "test")
    assert "test" == context.get_global("test_value")

    context.set_global("test_value", {"test": 43})
    assert {"test": 43} == context.get_global("test_value")

    context.set_global("test_value", ("test", "another"))
    assert ("test", "another") == context.get_global("test_value")

    context.set_global("test_value", 10)
    assert None is context.get_global("not_test_value")


def test_unit_context_add_and_get_system_value():
    system = get_example_system()
    context = Context()

    context.set_value(system, "system_test_value", 25)
    assert 25 == context.get_value(system, "system_test_value")


def test_unit_context_remove_global_value():
    context = Context()

    context.set_global("test_value", 24)
    assert 24 == context.get_global("test_value")

    context.remove_global("test_value")
    assert None is context.get_global("test_value")


def test_unit_context_remove_system_value():
    system = get_example_system()
    context = Context()

    context.set_value(system, "system_test_value", 25)
    assert 25 == context.get_value(system, "system_test_value")

    context.remove_value(system, "system_test_value")
    assert None is context.get_value(system, "system_test_value")

import time


from piedpiper_engine.engine import Engine
from core.client import Client


def test_find_client_queue_with_client_id():
    engine = Engine()
    client_1 = Client()
    client_2 = Client()
    client_3 = Client()

    engine.add_client(client_1)
    engine.add_client(client_2)
    engine.add_client(client_3)

    cq = engine._find_client_queue_(client_1._id)

    assert cq.is_client(client_1)


def test_add_client_method_adds_engine_to_client():
    engine = Engine()
    client = Client()

    engine.add_client(client)

    assert client._engine is engine


def test_adding_same_client_twice_will_not_add_again():
    engine = Engine()
    engine.clear_queues()

    client = Client()

    engine.add_client(client)
    engine.add_client(client)

    assert len(engine._all_queues) == 1


def test_remove_client_works():
    engine = Engine()
    engine.clear_queues()

    client = Client()

    engine.add_client(client)
    engine.remove_client(client)

    assert engine._find_client_queue_(client._id) is None


def test_cannot_remove_client_not_present():
    pass


def test_adding_message_will_add_to_the_client_queue():
    engine = Engine()
    engine.clear_queues()

    client = Client()

    engine.add_client(client)

    engine.add_message(client._id, "Test message")

    cq = engine._find_client_queue_(client._id)

    assert cq.get_next_message() == "Test message"


def test_method_process_will_run_until_stopped():
    engine = Engine()
    engine.clear_queues()

    engine._set_quit_loop.value = True  # Sets the quit value beforehand

    engine.process()
    time.sleep(0.4)


def test_loop_creates_a_seperate_process():
    pass


def test_adding_messages_to_client_queue_will_send_to_agent_manager():
    pass


def test_adding_messages_to_agent_queue_will_send_to_agent_manager():
    pass


def test_adding_to_both_queues_will_send_to_both_managers():
    pass


def test_method_quit_exits_process_succesfully():
    pass

import time
import pytest
import random

from piedpiper_engine.engine import Engine
from core.client import Client
from core.agent import Agent


def test_find_client_queue_with_client_id(engine):
    client_1 = Client()
    client_2 = Client()
    client_3 = Client()

    engine.add_client(client_1)
    engine.add_client(client_2)
    engine.add_client(client_3)

    cq = engine._find_client_queue_(client_1._id)

    assert cq.is_client(client_1)


def test_add_client_method_adds_engine_to_client(engine):
    client = Client()

    engine.add_client(client)

    assert client._engine is engine


def test_adding_same_client_twice_will_not_add_again(engine):
    engine.clear_queues()

    client = Client()

    engine.add_client(client)
    engine.add_client(client)

    assert len(engine._all_queues) == 1


def test_remove_client_works(engine):
    engine.clear_queues()

    client = Client()

    engine.add_client(client)
    engine.remove_client(client)

    assert engine._find_client_queue_(client._id) is None


def test_adding_message_will_add_to_the_client_queue(engine):
    engine.clear_queues()

    client = Client()

    engine.add_client(client)

    engine.add_message(client._id, "Test message")

    cq = engine._find_client_queue_(client._id)

    assert cq.get_next_message() == "Test message"


def test_adding_messages_to_client_queue_will_be_valid_on_loop(engine):
    engine.clear_queues()

    client = Client()
    engine.add_client(client)

    engine.add_message(client._id, "Test message 1")
    engine.add_message(client._id, "Test message 2")
    engine.add_message(client._id, "Test message 3")
    engine.add_message(client._id, "Test message 4")
    engine.add_message(client._id, "Test message 5")

    cq = engine._find_client_queue_(client._id)

    assert cq.get_next_message() == "Test message 1"
    assert cq.get_next_message() == "Test message 2"
    assert cq.get_next_message() == "Test message 3"
    assert cq.get_next_message() == "Test message 4"
    assert cq.get_next_message() == "Test message 5"


def test_adding_messages_to_client_queue_will_send_to_agent_manager(engine):
    engine.clear_queues()
    engine.loop()

    client = Client()
    engine.add_client(client)

    agent = Agent()
    engine.add_agent(client, agent)

    for _ in range(5):
        for i in range(random.randint(10, 60)):
            engine.add_message(client._id, "https://www.example.com")
        time.sleep(3)


def test_adding_messages_to_agent_queue_will_send_to_agent_manager(engine):
    pass


def test_adding_to_both_queues_will_send_to_both_managers(engine):
    pass


def test_method_quit_exits_process_succesfully(engine):
    pass

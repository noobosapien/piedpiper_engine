import time
import pytest
import random


from piedpiper_engine.engine import Engine
from core.client import Client
from core.agent import Agent
from modules.LangchainSyncAgent import LangchainSyncAgent
from modules.placetime_tools import hof_create_place_time, CreatePlaceTime


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
    client = Client()
    engine.add_client(client)

    agent = LangchainSyncAgent(
        content=(
            "You are an assistant who has the job of creating instances of given classes of a timeline told by a story.\n"
            "CALL THE RELEVANT TOOLS.\n"
            "For example when you recieve:\n"
            "'a couple of weeks ago me and my friend at a party and then at about 11pm someone fell down the stairs and broke his neck he was probably drunk, but I think someone pushed him over'\n"
            "You call the relevant instances using tools for this example:\n"
            "placetimes_tool with args: place=party, place_vague=false, time=11pm, date=(calculate 2 weeks earlier from today), time_vague=true\n"
        )
    )

    agent.add_tool(
        hof_create_place_time,
        CreatePlaceTime,
        "create_place_time",
        "Create an instance of class Placetime which holds only the information of the time and the place of the event",
    )

    engine.add_agent(client, agent)

    for _ in range(3):
        for i in range(random.randint(1, 2)):
            engine.add_message(
                client._id, "On the 31st of may at the pub I was with my friend"
            )
            engine.add_message(client._id, "last wednsday I was at school with Adam")
            engine.add_message(client._id, "last week at the mall I was with fred")
        time.sleep(10)

    time.sleep(5)


def test_adding_messages_to_agent_queue_will_send_to_agent_manager(engine):
    pass


def test_adding_to_both_queues_will_send_to_both_managers(engine):
    pass


def test_method_quit_exits_process_succesfully(engine):
    pass

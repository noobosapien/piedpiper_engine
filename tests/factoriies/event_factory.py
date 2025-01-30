from uuid import uuid4

from piedpiper_engine import EngineQuitEvent, System, SystemEvent, SystemLastEvent


def get_engine_quit_event():
    return EngineQuitEvent(id="event_" + str(uuid4()))


def get_example_event(system: System):
    eid = str(uuid4())
    sys_event = SystemEvent(id="event_" + eid, sys_id=system.get_id())

    return sys_event


def get_last_event(system):
    eid = str(uuid4())
    sys_last_event = SystemLastEvent(id="event_" + eid, sys_id=system.get_id())

    return sys_last_event

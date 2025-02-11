import asyncio
import time
from dataclasses import dataclass
from uuid import uuid4

from piedpiper_engine import ModuleAsync, ModuleAsyncEvent, ModuleSync, ModuleSyncEvent


@dataclass(kw_only=True)
class AsyncEvent(ModuleAsyncEvent):
    value: str


def get_example_async_module():
    class Example(ModuleAsync):
        def __init__(self):
            super().__init__()

        async def process(self, last_event):
            await asyncio.sleep(0.2)

            event = AsyncEvent(
                id="event_" + str(uuid4()),
                mod_id="mod_" + str(uuid4()),
                value=last_event.value + "-1",
            )

            return event

    return Example()


def get_example_async_module_no_event():
    class Example(ModuleAsync):
        def __init__(self):
            super().__init__()

        async def process(self, last_event):
            await asyncio.sleep(0.2)
            return None

    return Example()


@dataclass(kw_only=True)
class SyncEvent(ModuleSyncEvent):
    value: str


def get_example_sync_module():
    class Example(ModuleSync):
        def __init__(self):
            super().__init__()

        def process(self, last_event):
            time.sleep(0.2)
            event = SyncEvent(
                id="event_" + str(uuid4()),
                mod_id="mod_" + str(uuid4()),
                value=last_event.value + "-1",
            )

            return event

    return Example()


def get_example_sync_module_no_event():
    class Example(ModuleSync):
        def __init__(self):
            super().__init__()

        def process(self, last_event):
            time.sleep(0.2)
            return None

    return Example()


@dataclass(kw_only=True)
class AsyncIntEvent(ModuleAsyncEvent):
    value: int


def get_example_async_int_module():
    class Example(ModuleAsync):
        def __init__(self):
            super().__init__()

        async def process(self, last_event):
            await asyncio.sleep(0.01)
            event = AsyncIntEvent(
                id="event_" + str(uuid4()),
                mod_id="mod_" + str(uuid4()),
                value=last_event.value + 1,
            )
            return event

    return Example()


@dataclass(kw_only=True)
class SyncIntEvent(ModuleSyncEvent):
    value: int


def get_example_sync_int_module():
    class Example(ModuleSync):
        def __init__(self):
            super().__init__()

        def process(self, last_event):
            time.sleep(0.01)
            event = SyncIntEvent(
                id="event_" + str(uuid4()),
                mod_id="mod_" + str(uuid4()),
                value=last_event.value + 1,
            )

            return event

    return Example()

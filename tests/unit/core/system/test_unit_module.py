import asyncio

import pytest

from piedpiper_engine import Module, ModuleAsync, ModuleSync
from tests.factoriies.module_factory import (
    AsyncEvent,
    AsyncIntEvent,
    SyncEvent,
    SyncIntEvent,
    get_example_async_int_module,
    get_example_async_module,
    get_example_async_module_no_event,
    get_example_sync_int_module,
    get_example_sync_module,
    get_example_sync_module_no_event,
)

pytest_plugins = ("pytest_asyncio",)


def test_unit_module_validation():
    _ = Module()
    _ = ModuleSync()
    _ = ModuleAsync()


@pytest.mark.asyncio
async def test_unit_module_async_process_returns_event():
    prev_out = AsyncEvent(id="test-1", mod_id="mod_" + "0", value="test")

    async_mod = get_example_async_module()
    event = await async_mod.process(prev_out)

    assert event.value == "test-1"


def test_unit_module_sync_process_returns_event():
    prev_out = SyncEvent(id="test-1", mod_id="mod_" + "0", value="test")

    sync_mod = get_example_sync_module()
    event = sync_mod.process(prev_out)

    assert event.value == "test-1"


@pytest.mark.asyncio
async def test_unit_module_async_process_returns_no_event():
    prev_out = AsyncEvent(id="test-1", mod_id="mod_" + "0", value="test")

    async_mod = get_example_async_module_no_event()
    event = await async_mod.process(prev_out)

    assert event is None


def test_unit_module_sync_process_returns_no_event():
    prev_out = SyncEvent(id="test-1", mod_id="mod_" + "0", value="test")

    sync_mod = get_example_sync_module_no_event()
    event = sync_mod.process(prev_out)

    assert event is None


@pytest.mark.asyncio
async def test_unit_module_async_chain_100_modules():
    prev_out = AsyncIntEvent(id="test-1", mod_id="mod_" + "0", value=1)

    async_mods = [get_example_async_int_module() for _ in range(100)]

    for mod in async_mods:
        prev_out = await mod.process(prev_out)

    assert prev_out.value == 101


def test_unit_module_sync_chain_100_modules():
    prev_out = SyncIntEvent(id="test-1", mod_id="mod_" + "0", value=1)

    async_mods = [get_example_sync_int_module() for _ in range(100)]

    for mod in async_mods:
        prev_out = mod.process(prev_out)

    assert prev_out.value == 101


@pytest.mark.asyncio
async def test_unit_module_async_concurrent_100_modules():
    prev_out = AsyncIntEvent(id="test-1", mod_id="mod_" + "0", value=1)

    async_mods = [
        asyncio.create_task(get_example_async_int_module().process(prev_out))
        for _ in range(100)
    ]

    await asyncio.gather(*async_mods)

    for task in async_mods:
        assert task.result().value == 2

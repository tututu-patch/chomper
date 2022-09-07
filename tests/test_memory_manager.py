import pytest

from infernum import Infernum


@pytest.fixture()
def emulator():
    return Infernum()


def test_alloc(emulator):
    for n in range(1, 17):
        buffer = emulator.memory_manager.alloc(2**n)
        emulator.read_bytes(buffer, 2**n)


def test_free(emulator):
    buffer = emulator.memory_manager.alloc(255)
    emulator.memory_manager.free(buffer)

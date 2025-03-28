import pytest


@pytest.fixture()
def set_up():
    print('НАЧАЛО ТЕСТА!')
    yield
    print('КОНЕЦ ТЕСТА!')
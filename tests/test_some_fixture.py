import pytest

@pytest.fixture
def my_info():
    with open('myinfo.txt') as file:
        content = file.read()
    return content

def test_one(my_info):
    assert 'tiger' in my_info

def test_two(my_info):
    assert 'zebra' in my_info

def test_three(my_info):
    assert 'elephant' in my_info
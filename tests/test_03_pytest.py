import pytest

def test_always_passes():
    a = 2
    b = 2
    assert a == b
    
def test_always_fails():
    assert 1 == 2
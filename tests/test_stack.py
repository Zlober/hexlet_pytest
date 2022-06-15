import pytest


def test_stack():
    stack = []
    assert not stack
    stack.append('one')
    assert bool(stack)
    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()
import pytest


def always_returns_true():
    print("Create merge conflict!")


def test_always_returns_true():
    assert always_returns_true()

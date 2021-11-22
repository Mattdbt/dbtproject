from dbtproject.lib import try_me


def test_try_me():
    assert try_me('Hello')
    assert try_me('Hi')

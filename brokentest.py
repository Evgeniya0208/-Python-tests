import demotest.py


def test_add():
    res=demotest.inc(2,5)
    assert res==10


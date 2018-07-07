import demotest


def test_add():
    res=demotest.inc(2,5)
    assert res==7

import pytest
import sys

@pytest.mark.skip
def test_demo_1():
    assert True

@pytest.mark.skip(reason='Not included it in this build!')
def test_demo_2():
    assert True

def test_demo_3():
    assert True

# sys.version_info(major=3, minor=10, micro=6, releaselevel='final', serial=0)
@pytest.mark.skipif(sys.version_info < (3, 11), reason='requires sys 3.11 or higher')
def test_demo_4():
    assert True


def test_demo_5():
    assert True

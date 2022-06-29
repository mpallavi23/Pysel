import pytest
'''
@pytest.mark.skip
#@pytest.mark.xfail
@pytest.mark.smoke
def test_demo2_first():
    msg = "Hello"
    assert msg == "Hi", "Test failed"
'''


@pytest.mark.usefixtures("setup")
class TestFixture:

    def test_fixturedemo(self):
        print("fixture method")

    def test_fixturedemo2(self):
        print("fixture method2")

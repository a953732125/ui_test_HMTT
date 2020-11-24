from Base.driver import Driver
import pytest


@pytest.mark.run(order=-1)
class TestQuitMpDriver:
    def test_quit_mp_driver(self):
        Driver.quit_mp_driver()

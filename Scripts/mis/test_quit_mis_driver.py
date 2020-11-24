from Base.driver import Driver
import time,pytest
@pytest.mark.run(order=-1)

class TestQuitMisDriver:
    def test_quit_mis(self):
        time.sleep(2)
        Driver.quit_mis_driver()

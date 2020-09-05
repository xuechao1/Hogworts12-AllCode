import pytest
import yaml

from ui_framework_demo.test_case.test_base import TestBase


class TestMain(TestBase):
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./test_main.yaml")))
    def test_main(self, value1, value2):
        self.app.start().main().goto_search()
        print(value1)
        print(value2)

    def test_windows(self):
        self.app.start().main().goto_windows()

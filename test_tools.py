from unittest.mock import MagicMock, patch

import tools


class TestTools:
    def test_load_nums_from_file(self):
        test_data = ["1, 1", "1.5, 0.5", "10, 100", "", "12", "12, 33, 4"]
        expected = [(1, 1), (1.5, 0.5), (10, 100)]

        fake_api = MagicMock()
        fake_api.get_data.return_value = test_data
        with patch("tools.API", fake_api):
            nums = tools.load_nums_from_file()
            assert nums == expected

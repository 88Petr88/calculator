from unittest.mock import MagicMock, patch

from rc import validate_rc


class TestRC:
    def test_validation_rc(self):
        test_data = ["9402238054", "9503260591", "9411020146", "8503259655", "8102158834",
                     "8403X92512", "7-1186549", "97015204", "89911209354", "7401151214"]
        expected = [("9402238054", True), ("9503260591", True), ("9411020146", True), ("8503259655", True), ("8102158834", True),
                    ("8403X92512", False), ("7-1186549", False), ("97015204", False), ("89911209354", False), ("7401151214", False)]

        fake_api = MagicMock()
        fake_api.get_rc.return_value = test_data
        with patch("rc.API", fake_api):
            result = validate_rc()
            assert result == expected

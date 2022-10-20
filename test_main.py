import pytest

from main import add, subtract, multiply, divide


class Testclass:
    @pytest.fixture()   #použiju pokud chci s těmito čísly ve více funkcí pracovat
    def numbers(self):
        x = 10
        y = 20
        z = 30
        return [x, y, z]

    def test_add_2(self, numbers):
        x = numbers[0]
        y = numbers[1]
        z = numbers[2]
        assert add(x, y) == z

    @pytest.mark.odecitani  # zápis v terminalu    pytest test.py -v -m "odecitani"
    @pytest.mark.parametrize("x, y, z", [(1, 1, 2), (1.5, 0.5, 2), (10, 100, 110)])
    def test_add(self, x, y, z):
        assert add(x, y) == z

    @pytest.mark.custom_mark
    @pytest.mark.parametrize("x, y, z", [(5, 3, 2), (10, 10, 0), (150, 80, 70)])
    def test_subtract(self, x, y, z):
        assert subtract(x, y) == z

    @pytest.mark.skip  # přeskočení funkce
    @pytest.mark.parametrize("x, y, z", [(5, 5, 25), (10, 10, 100), (3, 3, 9)])
    def test_multiply(self, x, y, z):
        assert multiply(x, y) == z

    @pytest.mark.xfail  # vynechání testu
    @pytest.mark.parametrize("x, y, z", [(10, 2, 5), (9, 3, 3), (110, 100, 1.1)])
    def test_divide(self, x, y, z):
        assert divide(x, y) == z



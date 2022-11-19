from one_hot_encoder import fit_transform
import pytest


def test_moscow():
    assert fit_transform('Moscow') == [('Moscow', [1])]


def test_empty():
    assert fit_transform('') == [('', [1])]


def test_raise_type_error():
    with pytest.raises(TypeError):
        fit_transform(1)


@pytest.mark.parametrize(
    "source_cities,result", [
        (['Moscow', 'New York', 'Moscow', 'London'],
         [
             ('Moscow', [0, 0, 1]),
             ('New York', [0, 1, 0]),
             ('Moscow', [0, 0, 1]),
             ('London', [1, 0, 0]),
         ]
         )
    ], )
def test_decode(source_cities, result):
    assert fit_transform(source_cities) == result
from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_morse,result", [
        ('... --- ...', 'SOS'),
        ('.', 2),
        ('SOS', 'S'),
    ], )
def test_decode(source_morse, result):
    """ Проверяет правильность декодирования функции decode"""
    assert decode(source_morse) == result

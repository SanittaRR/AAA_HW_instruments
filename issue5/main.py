from what_is_year_now import what_is_year_now
from unittest.mock import patch
import pytest


def test_get_cases1():
    with patch("urllib.request.urlopen") as mocked_get_cases:
        with patch("json.load") as mocked_get_cases2:
            mocked_get_cases2.return_value = {'currentDateTime': "2022-11-18 00:00:00"}
            assert what_is_year_now() == 2022
            mocked_get_cases.assert_called_once()


def test_get_cases2():
    with patch("urllib.request.urlopen") as mocked_get_cases:
        with patch("json.load") as mocked_get_cases2:
            mocked_get_cases2.return_value = {'currentDateTime': "01.10.2023 00:00:00"}
            assert what_is_year_now() == 2022
            mocked_get_cases.assert_called_once()


def test_get_cases3():
    with patch("urllib.request.urlopen") as mocked_get_cases:
        with patch("json.load") as mocked_get_cases2:
            mocked_get_cases2.return_value = {'currentDateTime': "01:10:2023 00:00:00"}
            assert what_is_year_now() == 2022
            mocked_get_cases.assert_called_once()


#def test_raise_type_error():
    #with pytest.raises(TypeError):
        #what_is_year_now('dr')

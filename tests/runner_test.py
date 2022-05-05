"""
Moduł zawiera testy jednostkowe dla pliku runner.py

Klasy:
------
- brak

Funkcje:
--------
- test_get_source_if_put_correct_line_get_correct_answer():
    Jeżeli zostanie podana linia z prawidłową składnią to powinna zostać zwrócona prawidłowa wartość - dane po znaku
    dwukropka.
- test_get_source_if_put_bad_line_get_error():
    Jeżeli podana linia będzie miała nieprawidłowy format do powinien zostać zwrócony wyjątek
- test_get_source_if_put_empty_line_get_value_error():
    Jeżeli podana linia będzie pusta to powinien zostać zwrócony wyjątek
- test_get_destination_if_put_correct_line_get_correct_answer():
    Jeżeli zostanie podana linia z prawidłową składnią to powinna zostać zwrócona prawidłowa wartość - dane po znaku
    dwukropka.
- test_get_destination_if_put_line_without_dest_word_get_value_error():
    Jeżeli w podanej linii nie będzie słowa DEST to powinien zostać zwrócony wyjątek
- test_get_destination_if_put_empty_line_get_value_error():
    Jeżeli podana linia będzie pusta to powinien zostać zwrócony wyjątek

Wyjątki:
--------
- brak
"""

# Standard library imports

# Third party imports
import pytest

# Local imports
import runner


def test_get_source_if_put_correct_line_get_correct_answer():
    """
    Jeżeli zostanie podana linia z prawidłową składnią to powinna zostać zwrócona prawidłowa wartość - dane po znaku
    dwukropka.
    """
    text_line = '   Source : C:\\Users\\Piotr\\'
    value = runner.get_source(text_line)
    assert value == 'C:\\Users\\Piotr\\'


def test_get_source_if_put_bad_line_get_value_error():
    """
    Jeżeli podana linia będzie miała nieprawidłowy format to powinien zostać zwrócony wyjątek
    """
    text_line = '   C:\\Users\\Piotr\\'
    with pytest.raises(ValueError):
        runner.get_source(text_line)


def test_get_source_if_put_empty_line_get_value_error():
    """
    Jeżeli podana linia będzie pusta to powinien zostać zwrócony wyjątek
    """
    text_line = ''
    with pytest.raises(ValueError):
        runner.get_source(text_line)


def test_get_destination_if_put_correct_line_get_correct_answer():
    """
    Jeżeli zostanie podana linia z prawidłową składnią to powinna zostać zwrócona prawidłowa wartość - dane po znaku
    dwukropka.
    """
    text_line = '   Dest : C:\\Users\\Piotr\\'
    value = runner.get_destination(text_line)
    assert value == 'C:\\Users\\Piotr\\'


def test_get_destination_if_put_line_without_dest_word_get_value_error():
    """
    Jeżeli w podanej linii nie będzie słowa DEST to powinien zostać zwrócony wyjątek
    """
    text_line = '   : C:\\Users\\Piotr\\'
    with pytest.raises(ValueError):
        runner.get_destination(text_line)


def test_get_destination_if_put_empty_line_get_value_error():
    """
    Jeżeli podana linia będzie pusta to powinien zostać zwrócony wyjątek
    """
    text_line = ''
    with pytest.raises(ValueError):
        runner.get_destination(text_line)

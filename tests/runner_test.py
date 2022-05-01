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


def test_get_source_if_put_bad_line_get_error():
    """
    Jeżeli podana linia będzie miała nieprawidłowy format do powinien zostać zwrócony wyjątek
    """
    text_line = '   C:\\Users\\Piotr\\'
    with pytest.raises(ValueError):
        runner.get_source(text_line)


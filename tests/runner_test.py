"""
Moduł zawiera testy jednostkowe dla pliku runner.py

Klasy:
------
- brak

Funkcje:
--------
- test_get_configuration_settings_if_file_not_found_get_error():
    Jeżeli nie znaleziono pliku konfiguracyjnego to zwracany jest wyjątek FileNotFoundError


Wyjątki:
--------
- brak
"""

# Standard library imports

# Third party imports
import pytest

# Local imports
import runner


def test_get_configuration_settings_if_file_not_found_get_error():
    """
    Jeżeli nie znaleziono pliku konfiguracyjnego to zwracany jest wyjątek FileNotFoundError
    """
    path_to_file = '.\\data\\no_file_config.ini'
    with pytest.raises(FileNotFoundError):
        runner.get_configuration_settings(path_to_file)

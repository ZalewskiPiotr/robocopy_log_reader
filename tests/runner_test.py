"""
Moduł zawiera testy jednostkowe dla pliku runner.py

Klasy:
------
- brak

Funkcje:
--------
- test_get_configuration_settings_if_file_exists_get_data():
    Jeżeli plik konfiguracyjny istnieje to zwracana jest nazwa i ścieżka do pliku logu
- test_get_configuration_settings_if_file_not_found_get_error():
    Jeżeli nie znaleziono pliku konfiguracyjnego to zwracany jest wyjątek FileNotFoundError
- test_get_configuration_settings_if_file_not_found_get_error():
    Jeżeli nie znaleziono sekcji 'settings' w pliku konfiguracyjnym to zwracany jest wyjątek


Wyjątki:
--------
- brak
"""

# Standard library imports

# Third party imports
import pytest

# Local imports
import runner


def test_get_configuration_settings_if_file_exists_get_data():
    """
    Jeżeli plik konfiguracyjny istnieje to zwracana jest nazwa i ścieżka do pliku logu
    """
    path_to_file = '.\\data\\test_config.ini'
    file_name, file_path = runner.get_configuration_settings(path_to_file)
    assert file_name == 'test_plik_logu.txt'
    assert file_path == '.\\test_data\\'


def test_get_configuration_settings_if_no_settings_get_error():
    """
    Jeżeli nie znaleziono pliku konfiguracyjnego to zwracany jest wyjątek FileNotFoundError
    """
    path_to_file = '.\\data\\test_config_without_settings.ini'
    with pytest.raises(KeyError):
        runner.get_configuration_settings(path_to_file)


def test_get_configuration_settings_file_not_found_get_error():
    """
    Jeżeli nie znaleziono sekcji 'settings' w pliku konfiguracyjnym to zwracany jest wyjątek
    """
    path_to_file = '.\\data\\no_file_config.ini'
    with pytest.raises(FileNotFoundError):
        runner.get_configuration_settings(path_to_file)


def test_get_configuration_settings_if_no_key_get_error():
    """
    Jeżeli nie znaleziono klucza w sekcji 'settings' w pliku konfiguracyjnym to zwracany jest wyjątek
    """
    path_to_file = '.\\data\\test_config_without_key.ini'
    with pytest.raises(KeyError):
        runner.get_configuration_settings(path_to_file)

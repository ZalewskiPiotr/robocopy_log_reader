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
- test_get_config_path():
    Jeżeli podano ścieżkę do katalogu to funkcja powinna dodać do niego pliki o nazwie 'config.ini
- test_get_path_to_log_file():
    Jeżeli podano prawidłowe dane to funkcja powinna zwrócić ścieżkę zbudowaną z podanych danych wejściowych

Wyjątki:
--------
- brak
"""

# Standard library imports
import pathlib

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


def test_get_config_path():
    """
    Jeżeli podano ścieżkę do katalogu to funkcja powinna dodać do niego pliki o nazwie 'config.ini
    """
    folder = pathlib.Path(__file__).resolve().parent
    config_file = pathlib.Path.joinpath(folder, 'config.ini')
    assert config_file == runner.get_config_path(folder)


def test_get_path_to_log_file():
    """
    Jeżeli podano prawidłowe dane to funkcja powinna zwrócić ścieżkę zbudowaną z podanych danych wejściowych
    """
    folder = pathlib.Path(__file__).resolve().parent
    log_file = pathlib.Path.joinpath(folder, 'katalog_z_danymi', 'plik_logu.log')
    assert log_file == runner.get_path_to_log_file(folder, 'katalog_z_danymi', 'plik_logu.log')

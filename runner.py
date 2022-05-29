""" Skrypt uruchamiający i sterujący programem 'Robocopy log reader'

Ten skrypt uruchamia program i steruje jego przepływem.

Uruchomienie skryptu odbywa się poprzez wywołanie:
`python runner.py`

Skrypt zawiera funkcje:
-----------------------
- get_configuration_settings() -> tuple[str, str]
    Odczyt pliku konfiguracyjnego
- main
    Główna funkcja sterująca przepływem programu
"""
# Standard library imports
import configparser

# Third party imports

# Local imports
from robocopy_log_reader.robocopy_log_reader import read_log_file


def get_configuration_settings(path_to_config_file: str) -> tuple[str, str]:
    """ Odczyt pliku konfiguracyjnego

    Funkcja odczytuje dane z pliku konfiguracyjnego

    :param path_to_config_file: Ścieżka do pliki konfiguracyjnego
    :type path_to_config_file: str
    :return: Nazwa pliku log, Ścieżka do pliku logu
    :rtype: tuple[str, str]
    """
    config = configparser.ConfigParser()
    found_files = config.read(path_to_config_file)
    if len(found_files) == 0:
        raise FileNotFoundError(f"Nie znaleziono pliku konfiguracyjnego: {path_to_config_file}")

    if config.has_section('settings'):
        if config.has_option('settings', 'log_file_name') and config.has_option('settings', 'path_to_log_file'):
            log_file_name = config['settings']['log_file_name']
            log_file_path = config['settings']['path_to_log_file']
            return log_file_name, log_file_path
        else:
            raise KeyError(f"W pliku konfiguracyjnym {path_to_config_file} nie znaleziono klucza 'log_file_name' lub"
                             f"path_to_log_file")
    else:
        raise KeyError(f"W pliku konfiguracyjnym {path_to_config_file} nie znaleziono sekcji 'settings'")


def main():
    """ Główna funkcja sterująca przepływem programu.

    Funkcja uruchamia odczyt danych z pliku logu, następnie uruchamia wyświetlenie podsumowania.
    """
    log_file_name, log_file_path = get_configuration_settings('config.ini')
    robocopy_list = read_log_file(log_file_path + log_file_name)

    # Wyświetlenie raportu
    message: str = ''
    error_message: str = ''
    skipped_message: str = ''
    for info in robocopy_list:
        message = message + str(info) + '\n'
        if info.file_errors > 0 or info.folder_errors > 0:
            error_message = '!!!!!!!!!! WYKRYTO BłĘDY W PLIKU LOGU !!!!!!!!!!'
        if info.file_skipped > 0 or info.folder_skipped > 0:
            skipped_message = '!!!!!!!!!! WYKRYTO POMINIĘTE PLIKI W PLIKU LOGU !!!!!!!!!!'

    print(message)
    if len(error_message) > 0:
        print(error_message)
    if len(skipped_message) > 0:
        print(skipped_message)


if __name__ == "__main__":
    main()


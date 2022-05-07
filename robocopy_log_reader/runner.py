""" Skrypt uruchamiający i sterujący programem 'Robocopy log reader'

Ten skrypt uruchamia program i steruje jego przepływem.

Uruchomienie skryptu odbywa się poprzez wywołanie:
`python robocopy_log_reader/runner.py`

Skrypt zawiera funkcje:
-----------------------
- get_start_date(text_line: str) -> str:
    Pobranie informacji o dacie startu kopiowania
- get_source(text_line: str) -> str:
    Pobranie źródła kopiowanych danych
- get_destination(text_line: str):
    Pobranie docelowego miejsca kopiowanych danych
- get_dirs_info(text_line: str) -> tuple[int, int, int]:
    Odczytanie podsumowania dla katalogów
- get_files_info(text_line: str) -> tuple[int, int, int]:
    Odczytanie podsumowania dla plików
- read_log_file(file_path: str)
    Odczyt danych z pliku logu
- main
    Główna funkcja sterująca przepływem programu
"""
# Standard library imports

# Third party imports

# Local imports
from one_robocopy_info import OneRobocopyInfo


def get_start_date(text_line: str) -> str:
    """ Pobranie informacji o dacie startu kopiowania

    Funkcja z podanego ciągu tekstowego wyciąga informację o dacie uruchomienia polecenia 'robocopy'

    :param text_line: linia z pliku logu w formacie '  Started : czwartek, 31 października 2019 16:19:48'
    :type text_line: str
    :return: Data uruchomienia polecenia. W przypadku nieprawidłowego formatu ciągu wejściowego zwracany jest ValueError
    :rtype: str
    """
    data_from_line = text_line.strip().split(' : ')
    if data_from_line[0].upper() == 'STARTED':
        return data_from_line[1]
    else:
        raise ValueError(f"Nieprawidłowe dane wejściowe: '{text_line}'. Spodziewano się ciągu 'Started : '")


# TODO: dodać testy jednostkowe
def get_end_date(text_line: str) -> str:
    """ Pobranie informacji o dacie zakończenia kopiowania

    Funkcja z podanego ciągu tekstowego wyciąga informację o dacie zakończenia polecenia 'robocopy'

    :param text_line: linia z pliku logu w formacie '  Ended : czwartek, 31 października 2019 16:19:48'
    :type text_line: str
    :return: Data zakończenia polecenia. W przypadku nieprawidłowego formatu ciągu wejściowego zwracany jest ValueError
    :rtype: str
    """
    data_from_line = text_line.strip().split(' : ')
    if data_from_line[0].upper() == 'ENDED':
        return data_from_line[1]
    else:
        raise ValueError(f"Nieprawidłowe dane wejściowe: '{text_line}'. Spodziewano się ciągu 'Ended : '")


def get_source(text_line: str) -> str:
    """ Pobranie źródła kopiowanych danych

    Funkcja z podanego ciągu pobiera informację o źródłowym katalogu, który był kopiowany.

    :param text_line: linia z pliku logu w formacie 'SOURCE : xxxxxxx'
    :type text_line: str
    :return: Kopiowany katalog. W przypadku nieprawidłowego formatu ciągu wejściowego zwracany jest ValueError
    :rtype: str
    """
    data_from_line = text_line.strip().split(' : ')
    if data_from_line[0].upper() == 'SOURCE':
        return data_from_line[1]
    else:
        raise ValueError(f"Nieprawidłowe dane wejściowe: '{text_line}'. Spodziewano się ciągu 'Source : '")


def get_destination(text_line: str) -> str:
    """ Pobranie docelowego miejsca kopiowanych danych

    :param text_line: linia z pliku logu w formacie 'DEST : xxxxxxx'
    :type text_line: str
    :return: miejsce docelowe dla kopiowanych danych. W przypadku nieprawidłowego formatu ciągu wejściowego zwracany
    jest ValueError
    :rtype: str
    """
    data_from_line = text_line.strip().split(' : ')
    if data_from_line[0].upper() == 'DEST':
        return data_from_line[1]
    else:
        raise ValueError(f"Nieprawidłowe dane wejściowe: '{text_line}'. Spodziewano się ciągu 'Dest : '")


def get_dirs_info(text_line: str) -> tuple[int, int, int]:
    """ Odczytanie podsumowania dla katalogów

    Funkcja odczytuje z pliku logu podsumowanie wykonania polecenia robocopy. Funkcja zwraca informacje podsumowujące
    dla katalogów.

    :param text_line: linia z pliku logu w formacie 'Dirs :         1         1         0         0         0         0'
    Poszczególne pozycje oznaczają: Total    Copied   Skipped  Mismatch    FAILED    Extras
    :type text_line: str
    :return: ilość katalogów skopiowanych, ilość katalogów pominiętych, ilość błędów
    :rtype: tuple[int, int, int]
    """
    data_from_line = text_line.strip().split(' : ')
    if data_from_line[0].upper() == 'DIRS':
        dir_info = data_from_line[1].strip().split()
        return int(dir_info[1]), int(dir_info[2]), int(dir_info[4])

    else:
        raise ValueError(f"Nieprawidłowe dane wejściowe: '{text_line}'. Spodziewano się ciągu 'Dirs : '")


def get_files_info(text_line: str) -> tuple[int, int, int]:
    """ Odczytanie podsumowania dla plików

    Funkcja odczytuje z pliku logu podsumowanie wykonania polecenia robocopy. Funkcja zwraca informacje podsumowujące
    dla plików.

    :param text_line: linia z pliku logu w formacie 'Files :         1         1         0         0         0         0'
    Poszczególne pozycje oznaczają: Total    Copied   Skipped  Mismatch    FAILED    Extras
    :type text_line: str
    :return: ilość plików skopiowanych, ilość plików pominiętych, ilość błędów
    :rtype: tuple[int, int, int]
    """
    data_from_line = text_line.strip().split(' : ')
    if data_from_line[0].upper() == 'FILES':
        dir_info = data_from_line[1].strip().split()
        return int(dir_info[1]), int(dir_info[2]), int(dir_info[4])

    else:
        raise ValueError(f"Nieprawidłowe dane wejściowe: '{text_line}'. Spodziewano się ciągu 'Files : '")


# TODO: dodać test jednostkowy. Podać ścieżkę do pliku testowego
def read_log_file(file_path: str) -> list[OneRobocopyInfo]:
    """ Odczytanie pliku logu

    Funkcja odczytuje dane z pliku logu oraz zarządza tworzeniem informacji podsumowującej odczytane dane.

    :param file_path: ścieżka do pliku z logiem
    :type file_path: str
    :return: lista obiektów, które przechowują informacje podsumowujące każde wywołanie polecenie 'robocopy'
    :rtype: list[OneRobocopyInfo]
    """

    robocopy_list = []
    with open(file_path, 'rt', encoding='utf16') as text_file:
        line = text_file.readline()
        while line:
            if (line.find('Started :')) > -1:  # Początek polecenia robocopy
                start_date = get_start_date(line)
                info_source = get_source(text_file.readline())
                info_destination = get_destination(text_file.readline())
                line = text_file.readline()
            if (line.find('Dirs :')) > -1:  # Odczyt podsumowania kopiowania z pliku logu
                dirs_copied, dirs_skipped, dirs_failed = get_dirs_info(line)
                files_copied, files_skipped, files_failed = get_files_info(text_file.readline())
                line = text_file.readline()
            if (line.find('Ended :')) > -1:  # DAta końca wykonania polecenia robocopy
                end_date = get_end_date(line)
                robocopy_info = OneRobocopyInfo(start_date, end_date, info_source, info_destination, dirs_skipped,
                                                dirs_copied, dirs_failed, files_skipped, files_copied, files_failed)
                robocopy_list.append(robocopy_info)
            line = text_file.readline()
    return robocopy_list


def main():
    """ Główna funkcja sterująca przepływem programu.

    Funkcja uruchamia odczyt danych z pliku logu, następnie uruchamia wyświetlenie podsumowania.

    :return: ---
    :rtype: ---
    """
    robocopy_list = read_log_file('C:/work/Python projects/robocopy_log_reader/data/KopiaZapasowaLOG.txt')

    # sekcja testowa - testujemy to co wytworzysliśmy
    for info in robocopy_list:
        print(info)


if __name__ == "__main__":
    main()


""" Skrypt uruchamiający i sterujący programem 'Robocopy log reader'

Ten skrypt uruchamia program i steruje jego przepływem.

Uruchomienie skryptu odbywa się poprzez wywołanie:
`python robocopy_log_reader/runner.py`

Skrypt zawiera funkcje:
-----------------------
- read_log_file(file_path: str)
    Odczyt danych z pliku logu
- main
    Główna funkcja sterująca przepływem programu
"""
# Standard library imports

# Third party imports

# Local imports
from one_robocopy_info import OneRobocopyInfo


# TODO: dodać dokumentację
def get_source(text_line: str):
    data_from_line = text_line.strip().split(' : ')
    if data_from_line[0].upper() == 'SOURCE':
        return data_from_line[1]


# TODO: dodać dokumentację
# TODO: dodać testy jednostkowe
def get_destination(text_file: str):
    pass


# TODO: dodać test jednostkowy. Podać ścieżkę do pliku testowego
def read_log_file(file_path: str) -> list[OneRobocopyInfo]:
    """ Odczytanie pliku logu

    Funkcja odczytuje dane z pliku logu oraz zarządza tworzeniem informacji podsumowującej odczytane dane.

    :param file_path: ścieżka do pliku z logiem
    :type file_path: str
    :return: lista obiektów, które przechowują informacje podsumowujące każde wywołanie polecenie 'robocopy'
    :rtype: list[OneRobocopyInfo]
    """
    with open(file_path, 'rt') as text_file:
        line = text_file.readline()
        while line:
            print(line.strip('\t\n'))
            if (line.find('Started :')) > -1:  # Początek polecenia robocopy
                info_source = get_source(text_file.readline())
                info_destination = get_destination(text_file.readline())
                line = text_file.readline()
                print(line.strip('\t\n'))
                while line.find('Ended :') > -1:
                    print(line.strip('\t\n'))
                    line = text_file.readline()
            line = text_file.readline()


def main():
    """ Główna funkcja sterująca przepływem programu.

    Funkcja uruchamia odczyt danych z pliku logu, następnie uruchamia wyświetlenie podsumowania.

    :return: ---
    :rtype: ---
    """
    read_log_file('C:/work/Python projects/robocopy_log_reader/data/KopiaZapasowaLOG.txt')

    # sekcja testowa - testujemy to co wytworzysliśmy
    info = OneRobocopyInfo('24 kwieciec 2022', '25 wkiecień 2022', 'c:\dane\source', 'c:\dane\dest', 1, 2, 3, 10, 20,
                           30)
    print('hello')


if __name__ == "__main__":
    main()


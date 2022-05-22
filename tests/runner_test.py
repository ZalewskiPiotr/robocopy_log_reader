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
- test_get_start_date_if_put_correct_line_get_correct_answer()
    Jeżeli zostanie podany prawidłowy ciąg wejściowy to na wyjściu powinna zostać zwrócona prawidłowa wartość, czyli
    dane po znaku dwukropka
- test_get_start_date_if_put_line_without_started_word_get_value_error():
    Jeżeli w podanej linii nie będzie słowa 'started' to powinien zostać zwrócony wyjątek
- test_get_start_date_if_put_empty_line_get_value_error():
    Jeżeli podany zostanie pusty ciąg wejściowy to powinien zostać zwrócony wyjątek
- test_get_end_date_if_put_correct_line_get_correct_answer():
    Jeżeli zostanie podany prawidłowy ciąg wejściowy to na wyjściu powinna zostać zwrócona prawidłowa wartość, czyli
    dane po znaku dwukropka
- test_get_end_date_if_put_line_without_started_word_get_value_error():
    Jeżeli w podanej linii nie będzie słowa 'ended' to powinien zostać zwrócony wyjątek
- test_get_end_date_if_put_empty_line_get_value_error():
    Jeżeli podany zostanie pusty ciąg wejściowy to powinien zostać zwrócony wyjątek
- test_get_dirs_info_if_put_correct_line_get_correct_answer():
    Jeżeli podano prawidłowy ciąg wejściowy, to funkcja zwróci odpowiednie wartości
- test_get_dirs_info_if_put_line_without_dirs_word_get_value_error():
    Jeżeli w podanym ciągu brakuje słowa kluczowego 'Dirs :' to funkcja zwróci wyjątek
- test_get_dirs_if_put_empty_line_get_value_error():
    Jeżeli podano pusty ciąg to funkcja zwróci wyjątek
- test_get_files_info_if_put_correct_line_get_correct_answer():
    Jeżeli podano prawidłowy ciąg wejściowy, to funkcja zwróci odpowiednie wartości
- test_get_files_info_if_put_line_without_dirs_word_get_value_error():
    Jeżeli w podanym ciągu brakuje słowa kluczowego 'Files :' to funkcja zwróci wyjątek
- test_get_files_if_put_empty_line_get_value_error():
    Jeżeli podano pusty ciąg to funkcja zwróci wyjątek


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


def test_get_start_date_if_put_correct_line_get_correct_answer():
    """
    Jeżeli zostanie podany prawidłowy ciąg wejściowy to na wyjściu powinna zostać zwrócona prawidłowa wartość, czyli
    dane po znaku dwukropka
    """
    text_line = '  Started : czwartek, 31 października 2019 16:19:48'
    value = runner.get_start_date(text_line)
    assert value == 'czwartek, 31 października 2019 16:19:48'


def test_get_start_date_if_put_line_without_started_word_get_value_error():
    """
    Jeżeli w podanej linii nie będzie słowa 'started' to powinien zostać zwrócony wyjątek
    """
    text_line = 'czwartek, 31 października 2019 16:19:48'
    with pytest.raises(ValueError):
        runner.get_start_date(text_line)


def test_get_start_date_if_put_empty_line_get_value_error():
    """
    Jeżeli podany zostanie pusty ciąg wejściowy to powinien zostać zwrócony wyjątek
    """
    text_line = ''
    with pytest.raises(ValueError):
        runner.get_start_date(text_line)


def test_get_end_date_if_put_correct_line_get_correct_answer():
    """
    Jeżeli zostanie podany prawidłowy ciąg wejściowy to na wyjściu powinna zostać zwrócona prawidłowa wartość, czyli
    dane po znaku dwukropka
    """
    text_line = '  Ended : czwartek, 31 października 2019 16:19:48'
    value = runner.get_end_date(text_line)
    assert value == 'czwartek, 31 października 2019 16:19:48'


def test_get_end_date_if_put_line_without_started_word_get_value_error():
    """
    Jeżeli w podanej linii nie będzie słowa 'ended' to powinien zostać zwrócony wyjątek
    """
    text_line = 'czwartek, 31 października 2019 16:19:48'
    with pytest.raises(ValueError):
        runner.get_end_date(text_line)


def test_get_end_date_if_put_empty_line_get_value_error():
    """
    Jeżeli podany zostanie pusty ciąg wejściowy to powinien zostać zwrócony wyjątek
    """
    text_line = ''
    with pytest.raises(ValueError):
        runner.get_end_date(text_line)


def test_get_dirs_info_if_put_correct_line_get_correct_answer():
    """
    Jeżeli podano prawidłowy ciąg wejściowy, to funkcja zwróci odpowiednie wartości
    """
    text_line = '    Dirs :         1         2         3         0         5         0'
    copied, skipped, failed = runner.get_dirs_info(text_line)
    assert copied == 2
    assert skipped == 3
    assert failed == 5


def test_get_dirs_info_if_put_line_without_dirs_word_get_value_error():
    """
    Jeżeli w podanym ciągu brakuje słowa kluczowego 'Dirs :' to funkcja zwróci wyjątek
    """
    text_line = '    :         1         2         3         0         5         0'
    with pytest.raises(ValueError):
        runner.get_dirs_info(text_line)


def test_get_dirs_if_put_empty_line_get_value_error():
    """
    Jeżeli podano pusty ciąg to funkcja zwróci wyjątek
    """
    text_line = '   '
    with pytest.raises(ValueError):
        runner.get_dirs_info(text_line)


def test_get_files_info_if_put_correct_line_get_correct_answer():
    """
    Jeżeli podano prawidłowy ciąg wejściowy, to funkcja zwróci odpowiednie wartości
    """
    text_line = '    Files :         1         2         3         0         5         0'
    copied, skipped, failed = runner.get_files_info(text_line)
    assert copied == 2
    assert skipped == 3
    assert failed == 5


def test_get_files_info_if_put_line_without_dirs_word_get_value_error():
    """
    Jeżeli w podanym ciągu brakuje słowa kluczowego 'Files :' to funkcja zwróci wyjątek
    """
    text_line = '    :         1         2         3         0         5         0'
    with pytest.raises(ValueError):
        runner.get_files_info(text_line)


def test_get_files_if_put_empty_line_get_value_error():
    """
    Jeżeli podano pusty ciąg to funkcja zwróci wyjątek
    """
    text_line = '   '
    with pytest.raises(ValueError):
        runner.get_files_info(text_line)

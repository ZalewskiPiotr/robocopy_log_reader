# Robocopy log reader
> Projekt służy do odczytania pliku logu polecenia `ROBOCOPY`

Program odczytuje plik logu polecenia 'ROBOCOPY' i wyświetla sumaryczne informacje o wyniku kopiowania danych.
W szczególności wskazywane są informacje dotyczące błędów podczas kopiowania

_Więcej informacji znajduje się w [Wikipedii projektu][wiki]._

## Instalacja
Należy pobrać wersję dystrybucyjną programu i skopiować w dowolne miejsce na dysku.
Następnie, w pliku config.ini należy zmienić parametry:
- **path_to_log_file** - ścieżka do katalogu, w którym znajduje się plik logu polecenia ``robocopy``. Ścieżka może być
podana w postaci względnej (ze znakiem ``.``) lub w postaci bezwzględnej.
- **log_file_name** - nazwa pliku logu polecenia ``robocopy`` 

## Przykład użycia
W systemie Windows należy uruchomić plik **robocopy_log_reader.exe**

## Środowisko deweloperskie
#### Python
Należy pobrać wersję [Pythona 3.10.4][python-version] w postaci pliku 'Windows installer' i zainstalować na komputerze deweloperskim.

#### Pytest
Pakiet jest wykorzystywany do uruchamiania testów jednostkowych. Należy zainstalować pakiet Pytest poleceniem:
```sh
pip install pytest
```

#### Pyinstaller
Pakiet jest wykorzystywany do przygotowania wersji dystrybucyjnej programu. Pakiet należy zainstalować poleceniem:
```sh
pip install pyinstaller
```
#### Lista pakietów
Prawidłowe środowisko deweloperskie powinno zawierać poniższą listę pakietów:
```sh
Package                   Version
------------------------- --------
altgraph                  0.17.2
atomicwrites              1.4.0
attrs                     21.4.0
colorama                  0.4.4
future                    0.18.2
iniconfig                 1.1.1
packaging                 21.3
pefile                    2021.9.3
pip                       22.0.4
pluggy                    1.0.0
py                        1.11.0
pyinstaller               5.1
pyinstaller-hooks-contrib 2022.6
pyparsing                 3.0.8
pytest                    7.1.2
pywin32-ctypes            0.2.0
setuptools                57.0.0
tomli                     2.0.1
wheel                     0.36.2
```

## Przygotowanie wersji dystrybucyjnej programu
Do przygotowania wersji dystrybucyjnej programu potrzebny jest Pyinstaller oraz plik cli.py.
Aby utworzyć wersję dystrybucyjną należy wykonać polecenie:
```sh
pyinstaller cli.py --name robocopy_log_reader --add-data="config.ini;."
```
gdzie:
- **pyinstaller** - nazwa modułu, który tworzy wersję dystrybucyjną programu
- **cli.py** - nazwa skryptu, z informacjami dla pyinstaller-a
- **--name robocopy_log_reader** - nazwa docelowa programu exe, który zostanie utworzony
- **--add-data="config.ini;."** - dodanie pliku ``config.ini`` do katalogu głównego aplikacji

Wersja dystrybucyjna tworzona jest w katalogu:
> .\dist\robocopy_log_reader


## Historia zmian

* 0.1.0
    * Pierwsza wersja programu

## Licencja

Program jest rozpowszechniany na podstawie licencji ``GNU GPL`` 
[https://pl.wikipedia.org/wiki/GNU_General_Public_License][licence]

## Autor

[PiotrZET][mail]

<!-- Markdown link & img dfn's -->
[wiki]: https://github.com/ZalewskiPiotr/robocopy_log_reader/wiki
[licence]: https://pl.wikipedia.org/wiki/GNU_General_Public_License
[python-version]: https://www.python.org/downloads/release/python-3104/
[mail]: mailto:1piotrzalewski@gmail.com

# Standard library imports

# Third party imports

# Local imports

class OneRobocopyInfo:
    """
    Klasa reprezentuje informacje o jednym wywołaniu polecenia robocopy.

    Informacje odczytywane są z tekstowego pliku logu.

    Atrybuty:
    ---------
    #TODO: dodać dokumentację atrybutów

    Metody:
    -------

    Wyjątki:
    --------
    """

    def __init__(self, start_date: str, end_date: str, source: str, destination: str, folder_amount_skipped: int,
                 folder_amount_copied: int, folder_amount_errors: int, file_amount_skipped: int,
                 file_amount_copied: int, file_amount_errors: int):
        self._start_date = start_date
        self._end_date = end_date
        self._source = source
        self._destination = destination
        self._folder_amount_skipped = folder_amount_skipped
        self._folder_amount_copied = folder_amount_copied
        self._folder_amount_errors = folder_amount_errors
        self._file_amount_skipped = file_amount_skipped
        self._file_amount_copied = file_amount_copied
        self._file_amount_errors = file_amount_errors

    def __str__(self):
        errors: str = str(self._folder_amount_errors + self._file_amount_errors)
        return self._start_date + \
               ' -> ' + self._source + \
               ' -> Folders copied: ' + str(self._folder_amount_copied) + \
               ' -> Files copied: ' + str(self._file_amount_copied) + \
               ' -> Files skipped: ' + str(self._file_amount_skipped) + \
               ' -> ERRORS: ' + errors

    @property
    def file_errors(self):
        return self._file_amount_errors

    @property
    def folder_errors(self):
        return self._folder_amount_errors

    @property
    def file_skipped(self):
        return self._file_amount_skipped

    @property
    def folder_skipped(self):
        return self._folder_amount_skipped

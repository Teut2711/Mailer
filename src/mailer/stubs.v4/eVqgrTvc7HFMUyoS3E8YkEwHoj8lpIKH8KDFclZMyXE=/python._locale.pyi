import locale as _mod_locale

CHAR_MAX = 127
Error = _mod_locale.Error
LC_ALL = 0
LC_COLLATE = 1
LC_CTYPE = 2
LC_MONETARY = 3
LC_NUMERIC = 4
LC_TIME = 5
__doc__ = 'Support for POSIX locales.'
__name__ = '_locale'
__package__ = ''
def _getdefaultlocale():
    pass

def localeconv():
    '() -> dict. Returns numeric and monetary locale-specific parameters.'
    return dict()

def setlocale():
    '(integer,string=None) -> string. Activates/queries locale processing.'
    return ''

def strcoll():
    'string,string -> int. Compares two strings according to the locale.'
    return 1

def strxfrm(string):
    'strxfrm(string) -> string.\n\nReturn a string that can be used as a key for locale-aware comparisons.'
    return ''


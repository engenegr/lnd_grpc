import platform
from pathlib import Path
from os import environ, path


def set_data_dir():
    """
    Set default LND directory based on detected OS platform
    """
    _lnd_dir = None
    _platform = platform.system()
    _home_dir = str(Path.home())
    if _platform == 'Darwin':
        _lnd_dir = _home_dir + '/Library/Application Support/Lnd/'
    elif _platform == 'Linux':
        _lnd_dir = _home_dir + '/.lnd/'
    elif _platform == 'Windows':
        _lnd_dir = path.abspath(environ.get('LOCALAPPDATA') + 'Lnd/')
    return _lnd_dir


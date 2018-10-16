import subprocess

from ....lib import logger

__all__ = ['_launch_kite', '_locate_kite']

_QUERY = 'reg query "HKEY_LOCAL_MACHINE\\Software\\Kite\\AppData" /v InstallPath /s /reg:64'

def _launch_kite(app):
    proc = subprocess.Popen([app])
    return proc

def _locate_kite():
    installed = False
    app = None

    try:
        logger.log('running query...')
        out = subprocess.check_output(_QUERY)
        logger.log('query result:\n{}'.format(out))
        if len(out) > 0:
            res = out.decode().strip().split('\n')[1].strip()
            logger.log('parsed result:\n{}'.format(res))
            app = '{}\\kited.exe'.format(res[res.find('C:\\'):])
            installed = True
    except subprocess.CalledProcessError:
        installed = False
        app = None
    finally:
        logger.log('located kite: ({}, {})'.format(installed, app))
        return (installed, app)

#!C:\Users\ye973\PycharmProjects\face_training\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Crypto-Notify==1.0.0','console_scripts','cryptonotifier'
__requires__ = 'Crypto-Notify==1.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Crypto-Notify==1.0.0', 'console_scripts', 'cryptonotifier')()
    )

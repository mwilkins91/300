import subprocess
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read():
    result = subprocess.run(['python', os.path.join(__location__, '300.py')], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')
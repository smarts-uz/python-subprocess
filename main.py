import subprocess
import sys

pros = subprocess.Popen([f'{sys.executable}','sub.py',])
code = pros.wait()
print(code)


import subprocess
import json
# import jsane
from time import sleep
from pprint import pprint


# while True:
# text = subprocess.check_output('heroku logs -t', shell = True)
# pprint(text)
text = subprocess.check_output('ls', shell=True)
print(text)

# log_json.py

import json
import os
import time


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FILE_PATH = os.path.join(PROJECT_ROOT, "logs", "logs.json")


def log(message):
    log_entry = {'Time': time.asctime(time.localtime(time.time())), 'Message': message}
    if os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'r+') as file:
            data = json.load(file)
            data.append(log_entry)
            file.seek(0)
            json.dump(data, file)
    else:
        with open(FILE_PATH, 'w') as file:
            json.dump([log_entry], file)

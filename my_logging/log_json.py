# log_json.py

import json
import os
import time

def log(message):
    log_entry = {'Time': time.asctime(time.localtime(time.time())), 'Message': message}
    if os.path.isfile('../logs/logs.json'):
        with open('../logs/logs.json', 'r+') as file:
            data = json.load(file)
            data.append(log_entry)
            file.seek(0)
            json.dump(data, file)
    else:
        with open('../logs/logs.json', 'w') as file:
            json.dump([log_entry], file)

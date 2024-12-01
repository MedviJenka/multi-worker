import os

# Full project path which used to strip to get global path
abstract_dir = os.path.dirname(os.path.abspath(__file__))
GLOBAL_PATH = abstract_dir.split('server')[0][:-1]
PROJECT_PATH = fr'{GLOBAL_PATH}\server'
LOGS = fr'{PROJECT_PATH}\data\logs.log'

import os
import logging
from datetime import datetime
from dataclasses import dataclass


# Full project path which used to strip to get global path
abstract_dir = os.path.dirname(os.path.abspath(__file__))
GLOBAL_PATH = abstract_dir.split('server')[0][:-1]
PROJECT_PATH = fr'{GLOBAL_PATH}\server'
LOGS = fr'{PROJECT_PATH}\data\logs.log'


@dataclass
class Logger:

    time: object = datetime.now()
    time_format: str = f'{time: %A | %d/%m/%Y | %X}'
    format: str = f'%(levelname)s | {time_format} | %(message)s | Function: %(funcName)s | Line: %(lineno)d'

    @property
    def level(self) -> logging:

        """
        logger method
        :params: level ........... logging level, debug, info, etc...
                 text ............ text displayed in logger


        outcome:
        INFO |  Sunday | 01/12/2024 | 19:59:18 | Creating server 1 | Function: main | Line: 18

        """
        logging.basicConfig(filename=LOGS,
                            filemode='w',
                            encoding='utf-8',
                            datefmt=self.time_format,
                            format=self.format,
                            level=logging.INFO)
        return logging

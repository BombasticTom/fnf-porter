"""Utility tool for configuring the logger"""

import logging
import psychtobase.src.window as window

from time import strftime
from os import mkdir

class CustomHandler(logging.StreamHandler):
    def emit(self, record):
        log_entry = self.format(record)
        print(log_entry)
        window.window.logsLabel.append(log_entry)

def setup() -> logging.RootLogger:
	"""instance of Logger module, will be used for logging operations"""
	
	# logger config
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)

	# log format
	log_format = logging.Formatter("%(asctime)s: [%(filename)s] [%(levelname)s] %(message)s", "%H:%M:%S")

	try: mkdir("logs")
	except: pass
     
	# file handler
	log_file = f"""logs/fnf-porter-{strftime("%Y-%m-%d_%H-%M-%S")}.log"""
	file_handler = logging.FileHandler(log_file)
	file_handler.setFormatter(log_format)

    # console handler
	console_handler = CustomHandler()
	console_handler.setFormatter(log_format)

	_GB_ToolID = ''

	logger.handlers.clear()
	logger.addHandler(file_handler)
	logger.addHandler(console_handler)
	logger.info("Logger initialized!")

	return logger
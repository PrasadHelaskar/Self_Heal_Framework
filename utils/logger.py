import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, base_log_dir="/mnt/k/self_heal_framework/code/reports/logs", log_level=logging.INFO):
        # Directory wrt year and month creation
        today = datetime.now()
        year = today.strftime("%Y")
        month = today.strftime("%m")
        date = today.strftime("%d")
        year_directory = os.path.join(base_log_dir, year)
        log_directory = os.path.join(year_directory, month)

        # Create the log directory if it does not exist
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Log file creation
        log_file_path = os.path.join(log_directory, f"{date}.log")
        self.logger = logging.getLogger(__name__)

        # Adjesting the Log level entries
        self.logger.setLevel(log_level)

        if not self.logger.handlers:
            # Exporting the Log entries to the designated file
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(log_level)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)

            formatter = logging.Formatter('%(asctime)s - %(classname)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self, classname=None):
        # using the logger to push entried in the file
        if classname:
            # Classname is passed while initiating log in the dersired file
            return logging.LoggerAdapter(self.logger, {'classname': classname})

        else:
            # Classname is not passed while initiating log in the dersired file
            return logging.LoggerAdapter(self.logger, {'classname': 'GLOBAL'})


# Usage
# if __name__ == "__main__":
#     log = Logger().get_logger(__name__)

#     log.debug('This is a debug message')
#     log.info('This is an info message')
#     log.warning('This is a warning message')
#     log.error('This is an error message')
#     log.critical('This is a critical message')

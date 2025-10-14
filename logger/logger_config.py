import logging
import os

class LoggerConfig:
    LOGS_DIR_NAME = 'logs'
    LOGGER_NAME = 'Logger'
    LOGS_FILE_NAME = os.path.join(LOGS_DIR_NAME, 'test.log')
    LOGS_LEVEL = logging.INFO
    MAX_BYTES = 150000
    BACKUP_COUNT = 12
    FORMAT = '[%(asctime)s - %(levelname)s] - %(message)s'
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

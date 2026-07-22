import logging
import os
from datetime import datetime


class Logger:

    _logger = None

    @staticmethod
    def get_logger():

        if Logger._logger:
            return Logger._logger

        # Create Logs Folder
        log_folder = "logs"
        os.makedirs(log_folder, exist_ok=True)

        # One log file for every execution
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        log_file = os.path.join(
            log_folder,
            f"Automation_{timestamp}.log"
        )

        logger = logging.getLogger("AutomationFramework")
        logger.setLevel(logging.INFO)
        logger.propagate = False

        # Remove existing handlers
        if logger.handlers:
            logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File Handler
        file_handler = logging.FileHandler(
            log_file,
            mode="w",
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

        Logger._logger = logger

        logger.info("=" * 70)
        logger.info("Automation Framework Started")
        logger.info(f"Log File : {log_file}")
        logger.info("=" * 70)

        return logger
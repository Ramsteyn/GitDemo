import logging

# object of logging class
logger = logging.getLogger(__name__)

# File in which logs will be saved
file = logging.FileHandler("logFile.log")

# formatting a log file
formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
file.setFormatter(formatter)

# File handler which will save the log into above file
logger.addHandler(file)

logger.setLevel(logging.DEBUG)

# Types of log need to be printed
logger.debug("A debug Start to be executed")
logger.info("Information statement")
logger.warning("Something is in warning mode")
logger.error("A major error has happened")
logger.critical("Critical Issue occurred")

import logging

l = logging.getLogger(__name__)
file = logging.FileHandler("logFile.log")
l.addHandler(file)
l.debug("Debug statement")
l.info("Info statement")
l.warning("warning statement")
l.error("error message")
l.critical("critical message")
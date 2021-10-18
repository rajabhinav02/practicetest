import inspect
import logging
def custom_logging(loglevel="logging.DEBUG"):
    tcname= inspect.stack()[1][3]
    logger= logging.getLogger(tcname)
    logger.setLevel(logging.DEBUG)
    #FileHandler = logging.FileHandler("{0}.log".format(tcname))
    FileHandler = logging.FileHandler("auto.log", mode ="a")
    FileHandler.setLevel(loglevel)
    Format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    FileHandler.setFormatter(Format)
    logger.addHandler(FileHandler)
    return logger
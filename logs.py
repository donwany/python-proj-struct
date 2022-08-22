import logging

# create logger
logger = logging.getLogger("logs.py")
# set log level
logger.setLevel(logging.INFO)

# add file and stream handlers
file_h = logging.FileHandler('logfile.log')
#file_h.setLevel(logging.WARNING)
stream_h = logging.StreamHandler()
# formatter
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')

# set formatters
file_h.setFormatter(formatter)
stream_h.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_h)
logger.addHandler(stream_h)

def divide(x, y):
    try:
        out = x/y
    except ZeroDivisionError:
        logger.exception("Division by zero!")
    else:
        return out




if __name__ == '__main__':
    logger.info("Start ...")
    logger.error(f"Divide x/y = {divide(10, 0)}")
    logger.info("Finished ...")
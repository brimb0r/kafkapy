import logging

def setup_custom_logger(name):
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='producer.log',
                        filemode='w')
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
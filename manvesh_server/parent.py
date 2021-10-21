import logging

MY_FORMAT = '%(threadName)s %(funcName)10s %(name)10s %(levelname)10s %(levelno)5d'\
            '%(asctime)10s %(msecs)10s %(message)10s'

logging.basicConfig(level=logging.DEBUG,
                    datefmt='%H:%M:%S',
                    format=MY_FORMAT)

logger = logging.getLogger("logger_123")
#!/usr/bin/env python
# coding=utf-8

import os
import logging
from logging.config import dictConfig
import datetime


LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "./logs")
LOG_SETTINGS = dict(
    version=1,
    disable_existing_loggers=False,
    formatters={
        'standard': {
            'format': '%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s'
        },
    },
    handlers={
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH,
                                     "result_{}.log".format(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))),
            'formatter': 'standard',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    loggers={
        'default': {
            'handlers': ['file', 'console'],
            'level': logging.DEBUG,
        }
    }
)
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
dictConfig(LOG_SETTINGS)
logger= logging.getLogger('default')

if __name__ == '__main__':
    '''
    All level output use like this
    '''
    logger.debug("All level output")
    '''
    Parameterize
    '''
    logger.debug('%s,%s', 'param1', 'param2')

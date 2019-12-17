#!/usr/bin/env python
# coding=utf-8
import yaml
from pytest_mongodb.logger import logger
from pytest_mongodb.mongodb_client import MongodbManager


def singleton(cls):
    def _singleton(*args, **kwargs):
        instance = cls(*args, **kwargs)
        instance.__call__ = lambda: instance
        return instance

    return _singleton


@singleton
class DB(object):
    def __init__(self, mongocmdopt, rootdir):
        config_path = '{0}/{1}'.format(rootdir, mongocmdopt)
        with open(config_path) as f:
            self.env = yaml.load(f, Loader=yaml.FullLoader)

    @property
    def mongodb(self):
        mongodb_dict = dict()
        try:
            for k, v in self.env.get('mongodb', {}).items():
                mongodb_dict[k] = MongodbManager(host=v['host'],
                                                 username=v['username'],
                                                 password=v['password'],
                                                 port=v['port'],
                                                 database=v['database'])
        except Exception as e:
            logger.debug(e)
            raise ConnectionError(e)

        return mongodb_dict

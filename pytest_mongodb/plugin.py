# -*- coding: utf-8 -*-

import pytest
from configparser import ConfigParser
from pytest_mongodb.db import DB


def pytest_addoption(parser):
    group = parser.getgroup('pytest_mongodb')
    group.addoption(
        '--config_mongobd',
        action='store',
        # default='config/config.yml',
        help='relative path of config.yml'
    )


@pytest.fixture(scope="session", autouse=False)
def mongocmdopt(request):
    option_config = request.config.getoption("--config_mongobd")
    if option_config:
        return option_config
    else:
        try:
            ini_config = request.config.inifile.strpath
            config = ConfigParser()
            config.read(ini_config)
            mongodb_config = config.get('mongodb', 'config')
            return mongodb_config
        except Exception as e:
            raise RuntimeError("there is no mongodb config in pytest.ini", e)


@pytest.fixture(scope='session', autouse=False)
def mongodb(mongocmdopt, request):
    return DB(mongocmdopt, request.config.rootdir).mongodb

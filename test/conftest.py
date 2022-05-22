from os import remove

from ..modules import config
config.DB_PATH = "test.db"

def pytest_sessionfinish(session, exitstatus):
    remove(config.DB_PATH)
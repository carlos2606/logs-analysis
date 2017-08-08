#!/usr/bin/python3

import bleach
from config import Config


class LogsAnalyzer(object):
    """docstring for LogsAnalyzer"""
    def __init__(self):
        super(LogsAnalyzer, self).__init__()
        self.cursor = Config().get_db_cursor
        type(self.cursor)
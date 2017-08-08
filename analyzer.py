#!/usr/bin/python3

import bleach
from config import Config


class LogsAnalyzer(Config):
    """docstring for LogsAnalyzer"""
    def __init__(self):
        super(LogsAnalyzer, self).__init__()
        self.result = ''


class QueryProcessor(LogsAnalyzer):
    """docstring for QueryProcessor"""
    def __init__(self):
        super(QueryProcessor, self).__init__()

    def get_most_popular_articles(self):
        pass

    def get_most_popular_authors(self):
        pass

    def get_days_with_most_errors(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()

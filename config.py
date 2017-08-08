import psycopg2


class Config(object):
    """docstring for Config"""
    def __init__(self):
        super(Config, self).__init__()
        self.dbname = "news"
        self.db = psycopg2.connect(database=self.dbname)
        self.cursor = self.db.cursor()

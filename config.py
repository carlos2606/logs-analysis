import psycopg2


class Config(object):
    """Base class that defines the connection to the database
    """
    def __init__(self):
        super(Config, self).__init__()
        self.dbname = "news"
        self.db = psycopg2.connect(database=self.dbname)
        self.cursor = self.db.cursor()

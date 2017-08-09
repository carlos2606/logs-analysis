#!/usr/bin/python3

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
        query = """ select articles.title, count (*) as views
                    from articles join log on articles.slug =
                    (regexp_split_to_array(path, E'/article/'))[2]
                    where path != '/' group by
                    (regexp_split_to_array(path, E'/article/'))[2],
                    articles.title
                    order by views desc limit 3 ;"""
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.db.close()

    def get_most_popular_authors(self):
        pass

    def get_days_with_most_errors(self):
        pass


def main():
    qp = QueryProcessor()
    qp.get_most_popular_articles()
    print("Top 3 articles of all time: ")
    for a in qp.result:
        print("'{}' --- {} views".format(a[0], a[1]))


if __name__ == '__main__':
    main()

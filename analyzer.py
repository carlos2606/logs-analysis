#!/usr/bin/python3

from config import Config


class LogsAnalyzer(Config):
    """Class that stores the result of the queries processed
        by the child class QueryProcessor
    """
    def __init__(self):
        super(LogsAnalyzer, self).__init__()
        self.result = ''


class QueryProcessor(LogsAnalyzer):
    """Class that is in charge of processing the queries and
        retrieve the desired data
    """
    def __init__(self):
        super(QueryProcessor, self).__init__()

    def get_most_popular_articles(self):
        """ Method that retrieves the top 3 articles with most views
            of all time.
        """
        query = """ select articles.title, count (*) as views
                    from articles join log on articles.slug =
                    (regexp_split_to_array(path, E'/article/'))[2]
                    where path != '/' group by
                    (regexp_split_to_array(path, E'/article/'))[2],
                    articles.title
                    order by views desc limit 3 ;"""
        # Sending the query to be run
        self.cursor.execute(query)
        # Getting the results and updating the parent self.result variable
        self.result = self.cursor.fetchall()

    def get_most_popular_authors(self):
        pass

    def get_days_with_most_errors(self):
        pass


def main():
    # Instantiating the class QueryProcessor
    qp = QueryProcessor()
    # Calling method to get popular articles
    qp.get_most_popular_articles()
    # Printing the first results..
    print("Top 3 articles of all time: ")
    for a in qp.result:
        print("'{}' --- {} views".format(a[0], a[1]))

    # Calling method to get popular authors
    qp.get_most_popular_authors()

    # Closing connection
    qp.db.close()


if __name__ == '__main__':
    main()

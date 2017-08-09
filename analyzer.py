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
        self._execute_query(query)

    def get_most_popular_authors(self):
        """ Method that retrieves the most popular authors
            of all time.
        """
        query = """ select authors.name, count(log.path) as views from authors
                    left join articles on authors.id = articles.author
                    left join log on log.path like concat('%', articles.slug)
                    group by authors.name order by views desc ;"""
        self._execute_query(query)

    def get_days_with_most_errors(self):
        """ Method that retrieves days with a failure rate greater
            than 1%.
        """
        query = "select * from rate_val where val > 1;"
        self._execute_query(query)

    def _execute_query(self, query):
        """ Private method that does the actual query processing
        """
        # Sending the query to be run
        self.cursor.execute(query)
        # Getting the results and updating the parent self.result variable
        self.result = self.cursor.fetchall()


def main():
    # Instantiating the class QueryProcessor
    qp = QueryProcessor()
    # Calling method to get popular articles
    qp.get_most_popular_articles()
    # Printing the first results..
    print("********* Top 3 articles of all time: **********")
    for a in qp.result:
        print("'{}' --- {} views".format(a[0], a[1]))

    # Calling method to get popular authors
    qp.get_most_popular_authors()
    print("-------------------------------------------")
    print("********* Most popular authors of all time:  *********")
    for a in qp.result:
        print("{} --- {} views".format(a[0], a[1]))

    # Calling method to get days when failures were > than 1%
    qp.get_days_with_most_errors()
    print("-------------------------------------------")
    print("******** Days with more than 1{} of failures: *******".format('%'))
    for d in qp.result:
        print("{} --- {}{} errors".format(d[0], round(float(d[1]), 1), '%'))

    # Closing db connection
    qp.db.close()

if __name__ == '__main__':
    main()

from urllib import request
from stock_provider import StockProvider


class Fetcher(object):
    @staticmethod
    def fetch(provider: StockProvider) -> str:
        """
        Retrieve the contents of the specified URL

        :param provider: StockProvider for which to
            retrieve the webpage
        :return: Contents of the specified URL
        :rtype: str
        """
        return request.urlopen(provider.request_options(provider.url, provider.iid)).read()

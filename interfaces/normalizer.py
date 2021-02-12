from models.gpu import GPU
from stock_provider import StockProvider


class Normalizer(object):
    @staticmethod
    def normalize(provider: StockProvider) -> [GPU]:
        """
        Map the extracted values to a GPU object

        :param provider: StockProvider for which to
            normalize the extracted values
        :return: list with GPU elements
        :rtype: list
        """
        pass

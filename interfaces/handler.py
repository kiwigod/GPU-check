from stock_provider import StockProvider


class Handler(object):
    @staticmethod
    def handle(provider: StockProvider, callback: callable) -> callable:
        """
        Apply actions on the given StockProvider, and go to the
            next handler by executing the callback

        :param provider: The StockProvider for which to apply the
            handler's logic
        :param callback:
        :return: Value of the final callable in the pipeline
        :rtype: callable
        """
        return callback(provider)

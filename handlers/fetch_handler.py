from importlib import import_module
from interfaces.fetcher import Fetcher
from interfaces.handler import Handler
from stock_provider import StockProvider


class FetchHandler(Handler):
    @staticmethod
    def handle(provider: StockProvider, callback: callable) -> callable:
        fetcher: Fetcher = getattr(
            import_module(f"fetcher.{provider.name}"), f"{provider.get_class_name()}Fetcher"
        )
        provider.source = fetcher.fetch(provider)

        return callback(provider)

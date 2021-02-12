from importlib import import_module
from interfaces.extractor import Extractor
from interfaces.handler import Handler
from stock_provider import StockProvider


class ExtractorHandler(Handler):
    @staticmethod
    def handle(provider: StockProvider, callback: callable) -> callable:
        extractor: Extractor = getattr(
            import_module(f"extractor.{provider.name}"), f"{provider.get_class_name()}Extractor"
        )
        provider.extracted = extractor.extract(provider)

        return callback(provider)

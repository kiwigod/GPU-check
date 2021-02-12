from importlib import import_module
from interfaces.handler import Handler
from interfaces.normalizer import Normalizer
from stock_provider import StockProvider


class NormalizerHandler(Handler):
    @staticmethod
    def handle(provider: StockProvider, callback: callable) -> callable:
        normalizer: Normalizer = getattr(
            import_module(f"normalizer.{provider.name}"), f"{provider.get_class_name()}Normalizer"
        )
        provider.normalized = normalizer.normalize(provider)

        return callback(provider)

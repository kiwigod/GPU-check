from copy import deepcopy
from typing import Union
from handlers.extractor_handler import ExtractorHandler
from handlers.fetch_handler import FetchHandler
from handlers.normalizer_handler import NormalizerHandler
from interfaces.handler import Handler
from stock_provider import StockProvider

pipelines = {
    "gpu": [FetchHandler, ExtractorHandler, NormalizerHandler]
}


class Pipeline(object):
    def __init__(self, line: str):
        self.line: [Handler] = deepcopy(pipelines[line])

    def send(self, provider: StockProvider):
        handler = self.next_handler()
        if not handler:
            return provider

        return handler.handle(provider, self.send)

    def next_handler(self) -> Union[Handler, bool]:
        try:
            return self.line.pop(0)
        except IndexError:
            return False

import re
from typing import Union
from interfaces.normalizer import Normalizer
from models.gpu import GPU
from stock_provider import StockProvider


class MegekkoNvidiaNormalizer(Normalizer):
    @staticmethod
    def get_price(price: str) -> Union[float, None]:
        match = re.findall(r'\d+', price)
        if len(match) > 0:
            return float(match[0])
        return None

    @staticmethod
    def normalize(provider: StockProvider) -> [GPU]:
        normalized = list()
        for extracted in provider.extracted:
            normalized.append(
                GPU(
                    ean=extracted['EAN'],
                    sku=extracted['Vendorcode'],
                    brand=extracted['Merk'],
                    graphics_engine=extracted['Graphics Engine'],
                    memory=extracted['Videogeheugen'],
                    memory_type=extracted['VGA Geheugen type'],
                    price=MegekkoNvidiaNormalizer.get_price(extracted['price']),
                    avaialble=extracted['available'],
                    release_date=extracted['available_on'],
                    provider_url=provider.get_base_url()+extracted['link']
                )
            )

        return normalized

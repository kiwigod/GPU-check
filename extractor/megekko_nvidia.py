import re
from bs4 import BeautifulSoup, Tag
from interfaces.extractor import Extractor
from stock_provider import StockProvider


class MegekkoNvidiaExtractor(Extractor):
    CONTENT_VALIDATOR = re.compile(r'/product/\d+/')

    @staticmethod
    def extract(provider: StockProvider) -> list:
        gpu_page = BeautifulSoup(provider.source, 'html.parser')
        content = [div for div in gpu_page.find_all('div', class_='content')
                   if re.search(MegekkoNvidiaExtractor.CONTENT_VALIDATOR, str(div))]

        return [MegekkoNvidiaExtractor.extract_gpu(gpu) for gpu in content]

    @staticmethod
    def extract_gpu(gpu: Tag) -> dict:
        info = {'link': gpu.find_next('a').attrs['href']}
        current = gpu.find('div', class_='t0')
        # TODO: can be improved.
        while True:
            t1 = current = current.find_next('div', class_='t1')
            t2 = current = current.find_next('div', class_='t2')
            info[t1.get_text()] = t2.get_text()

            if t1.get_text() == 'Garantie':
                break

        price = current.find_next('div', class_='pricecontainer')
        available = current.find_next('div', class_='shopbutton')
        info['price'] = price.get_text()
        info['available'] = len(available.get_text()) == 0
        if not info['available']:
            info['available_on'] = available.find_next('div', class_='date').get_text()
        else:
            info['available_on'] = None

        return info

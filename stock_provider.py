import re
from request_options import RequestOptions


class StockProvider(object):
    def __init__(self, url: str, request_options: RequestOptions):
        self.url = url
        self.request_options = request_options
        self.name = ''
        self.iid = ''
        self.source = ''
        self.extracted = list()
        self.normalized = list()

    def get_base_url(self) -> str:
        """
        Extract the base url to append href values

        :return: base url
        :rtype: str
        """
        return re.match(r"(?P<base>(http(s)?://)?(www\.)?[a-z.]+)/", self.url).groupdict()['base']

    def get_class_name(self) -> str:
        """
        Generate class name used in the following handlers:
        - Fetch handler
        - Extractor handler
        - Normalizer handler

        :return: Class name
        :rtype: str
        """
        up_next = False
        cls_name = ''
        for c in self.name.title():
            if c == '_':
                up_next = True
                continue
            if up_next:
                cls_name += c.upper()
                up_next = False
            else:
                cls_name += c

        return cls_name

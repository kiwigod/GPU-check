class RequestOptions(object):
    def __init__(self, product_filter):
        self.product_filter = product_filter

    def __call__(self, url: str, iid: str):
        if callable(self.product_filter):
            return self.product_filter(url, iid)
        return f"{url}?{self.product_filter}{iid}"

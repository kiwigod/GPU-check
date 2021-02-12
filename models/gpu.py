class GPU(object):
    def __init__(self, **kwargs):
        self.ean: str = kwargs.get('ean')
        self.sku: str = kwargs.get('sku')
        self.brand: str = kwargs.get('brand')
        self.graphics_engine: str = kwargs.get('graphics_engine')
        self.memory: str = kwargs.get('memory')
        self.memory_type: str = kwargs.get('memory_type')
        self.available: bool = kwargs.get('avaialble')
        self.price: float = kwargs.get('price')
        self.release_date: str = kwargs.get('release_date')
        self.provider_url: str = kwargs.get('provider_url')
        self.additional: dict = kwargs.get('additional')

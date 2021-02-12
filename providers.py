from request_options import RequestOptions
from stock_provider import StockProvider

providers = {
    "megekko_nvidia": StockProvider(
        "https://www.megekko.nl/Computer/Componenten/Videokaarten/Nvidia-Videokaarten",
        RequestOptions(lambda url, iid: f"{url}?f=f_{iid}_vrrd-0")
    ),
    "megekko_amd": StockProvider(
        "https://www.megekko.nl/Computer/Componenten/Videokaarten/AMD-Videokaarten",
        RequestOptions(lambda url, iid: f"{url}?f=f_{iid}_vrrd-0")
    )
}


def get_provider(name: str) -> StockProvider:
    return providers[name]

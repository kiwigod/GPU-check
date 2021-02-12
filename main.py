from gpus import get_providers_for_gpu, get_gpu_iid, load_gpus
from pipeline import Pipeline
from providers import get_provider


def main():
    gpus_to_check_stock = ['rtx_3060_ti', 'rx_6900_xt', 'rx_5700_xt']
    for gpu in gpus_to_check_stock:
        providers = get_providers_for_gpu(gpu)
        for provider in providers:
            _provider = get_provider(provider)
            _provider.name = provider
            _provider.iid = get_gpu_iid(gpu, _provider.name)
            Pipeline('gpu').send(_provider)

            for _gpu in _provider.normalized:
                print(_gpu.__dict__)
            print('-------')


if __name__ == '__main__':
    load_gpus()
    main()

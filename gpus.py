import yaml
from typing import KeysView
gpus = {}


def load_gpus():
    global gpus
    with open("gpus.yml", "r") as stream:
        yml = yaml.safe_load(stream)
    gpus = {**yml['nvidia'], **yml['amd']}


def get_gpu_iid(gpu: str, provider: str) -> str:
    return gpus[gpu][provider]


def get_providers_for_gpu(gpu: str) -> KeysView[str]:
    return gpus[gpu].keys()

# logger/setup.py
import logging
from pathlib import Path
from typing import Union, cast

import yaml

from infra.logger.formatters import ColorizedFormatter

logger = logging.getLogger(__name__)
formatter = ColorizedFormatter(
    fmt='%(levelprefix)s %(name)-35s %(message)s', datefmt='%H:%M:%S'
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)


def get_dict_config() -> dict[str, Union[str, int]]:
    """Получить конфигурацию логгера из YAML файла"""
    logger.debug("Создаю config для логгера из .yaml")

    current_path = Path(__file__).parent
    base_config_path = Path(current_path, 'config.yaml')
    dev_config_path = Path(current_path, 'dev_config.yaml')

    if dev_config_path.exists():
        path = dev_config_path
        logger.warning(f'Конфигурационный файл: "dev_config.yaml"')
    else:
        path = base_config_path

    with open(path, 'rt') as f:
        config = cast(dict[str, Union[str, int]], yaml.safe_load(f))

    return config

import importlib
import inspect
from loguru import logger
from pathlib import Path
from typing import Type, List

from aiogram_dialog import Dialog

from .auto_register import AutoRegister




class DialogCollector:
    @classmethod
    def find_auto_register_classes(cls, package_path: str) -> List[Type[AutoRegister]]:
        """Рекурсивно сканирует пакет и находит все классы, наследующие от AutoRegister."""
        classes = []
        package = importlib.import_module(package_path)
        package_dir = Path(package.__file__).parent  # Получаем директорию пакета
        # Рекурсивно ищем все .py-файлы в пакете
        for py_file in package_dir.glob("**/*.py"):
            if py_file.name == "__init__.py":
                module_path = py_file.parent.relative_to(package_dir)
                if str(module_path) == '.':
                    continue
                module_name = f"{package_path}.{module_path}".replace("\\", ".")

            else:
                module_path = py_file.relative_to(package_dir).with_suffix("")
                module_name = f"{package_path}.{str(module_path).replace('\\', '.')}"

            # Пропускаем __pycache__ и служебные файлы
            if any(part.startswith("__") and part != "__init__" for part in module_name.split(".")):
                continue

            try:
                module = importlib.import_module(module_name)
                for name, obj in inspect.getmembers(module):
                    if (
                        inspect.isclass(obj)
                        and issubclass(obj, AutoRegister)
                        and obj != AutoRegister
                    ):
                        classes.append(obj)
            except ImportError as e:
                logger.warning(f"Could not import {module_name}: {e}")
            except Exception as e:
                logger.warning(f"Error processing {module_name}: {e}")

        return classes

    @classmethod
    def collect(cls, package_path: str) -> List[Dialog]:
        """Собирает все диалоги в проекте."""
        dialog_classes = set(cls.find_auto_register_classes(package_path))
        return [dialog_class.get_dialog() for dialog_class in dialog_classes]

import importlib
import inspect
from pathlib import Path
from typing import List, Type

from aiogram_dialog import Dialog

from .auto_register import AutoRegister


class DialogCollector:
    @staticmethod
    def _get_dir_package_path(package_path: str) -> Path:
        package = importlib.import_module(package_path)

        if not package.__file__:
            raise ValueError(f'Пакет {package.__name__} не имеет файла')

        return Path(package.__file__).parent  # Получаем директорию пакета

    @classmethod
    def find_auto_register_classes(cls, package_path: str) -> List[Type[AutoRegister]]:
        """Рекурсивно сканирует пакет и находит все классы, наследующие от AutoRegister."""
        classes = []
        package_dir = cls._get_dir_package_path(package_path)
        # Рекурсивно ищем все .py-файлы в пакете
        for py_file in package_dir.glob("**/*.py"):
            if py_file.name == "__init__.py":
                module_path = py_file.parent.relative_to(package_dir)
                if str(module_path) == '.':
                    continue
                module_name = f"{package_path}.{module_path}".replace("\\", ".")

            else:
                module_path = py_file.relative_to(package_dir).with_suffix("")
                module_name = f"{package_path}.{module_path}".replace("\\", ".")

            # Пропускаем __pycache__ и служебные файлы
            if any(
                part.startswith("__") and part != "__init__" for part in module_name.split(".")
            ):
                continue

            module = importlib.import_module(module_name)
            for name, obj in inspect.getmembers(module):
                if (
                    inspect.isclass(obj)
                    and issubclass(obj, AutoRegister)
                    and obj != AutoRegister
                ):
                    classes.append(obj)

        return classes

    @classmethod
    def collect(cls, package_path: str) -> List[Dialog]:
        """Собирает все диалоги в проекте."""
        dialog_classes = set(cls.find_auto_register_classes(package_path))
        return [dialog_class.get_dialog() for dialog_class in dialog_classes]

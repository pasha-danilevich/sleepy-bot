import subprocess
import sys
from pathlib import Path
from loguru import logger

def save_git_diff():
    # Получаем вывод git diff (универсальный способ для всех ОС)
    result = subprocess.run(
        ['git', 'diff'],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace',  # Обработка проблем с кодировкой
        shell=sys.platform == 'win32'  # Используем shell=True только на Windows
    )

    if result.returncode != 0:
        logger.error("Ошибка при выполнении git diff:")
        logger.error(result.stderr)
        return

    # Создаем путь к файлу (кросс-платформенный способ)
    output_path = Path(__file__).resolve().parent / 'output'
    path = Path(output_path, "prompt.txt")
    # Записываем вывод в файл с явным указанием кодировки
    with open(path, 'w', encoding='utf-8') as f:
        prompt = (
            "Задача:\n"
            "Напиши комментарий к моему commit используя следующую структуру:\n"
            "{краткое название commit`а, описывающее всю суть}\n"
            "{символ каретки для отступа (enter)}\n"
            "{пункты изменений (начинаются с дефиса)}\n"
            "СВОЙ ОТВЕТ НАПИШИ В code формате на русском языке\n\n"
            "git diff:\n"
        )
        diff_text = result.stdout
        f.write(prompt + diff_text)

    logger.success(f"Вывод git diff сохранён в {path}")


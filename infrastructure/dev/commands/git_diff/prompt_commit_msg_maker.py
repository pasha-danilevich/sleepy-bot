import subprocess
import sys
from pathlib import Path

import pyperclip
from loguru import logger


def save_git_diff():
    run_params = {
        'capture_output': True,
        'text': True,
        'encoding': 'utf-8',
        'errors': 'replace',  # Обработка проблем с кодировкой
        'shell': sys.platform == 'win32',  # Используем shell=True только на Windows
    }
    # Получаем вывод git diff (универсальный способ для всех ОС)
    diff = subprocess.run(['git', 'diff'], **run_params)
    diff_cached = subprocess.run(['git', 'diff', '--cached'], **run_params)

    if diff.returncode != 0 or diff_cached.returncode != 0:
        logger.error("Ошибка при выполнении git diff или git diff --cached:")
        logger.error(diff.stderr)
        return
    prompt = (
        "Задача:\n"
        "Напиши комментарий к моему commit используя следующую структуру:\n"
        "{краткое название commit`а, описывающее всю суть}\n"
        "{символ каретки для отступа (enter)}\n"
        "{пункты изменений (начинаются с дефиса)}\n"
        "СВОЙ ОТВЕТ НАПИШИ В code формате на русском языке\n\n"
    )
    diff_text = diff.stdout
    diff_cached_text = diff_cached.stdout
    full_text = prompt + f'git diff --cached: {diff_cached_text}' + f'git diff: {diff_text}'
    copy_to_buffer(full_text)


def copy_to_buffer(text: str):
    # Копируем текст в буфер обмена
    try:
        pyperclip.copy(text)
        logger.success("Промт успешно скопирован в буфер обмена!")
    except Exception as e:
        logger.error(f"Не удалось скопировать текст в буфер обмена: {e}")


def write_to_txt(text: str):
    # Создаем путь к файлу (кросс-платформенный способ)
    output_path = Path(__file__).resolve().parent / 'output'
    path = Path(output_path, "prompt.txt")
    # Записываем вывод в файл с явным указанием кодировки
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

    logger.success(f"Вывод git diff сохранён в {path}")

import os

from yaml import safe_load


def read_views() -> dict[str, str]:
    """
    Функция чтения .yaml-файла с представлениями.

    :return: Словарь представлениями.
    """

    data = {}

    for files in os.walk(f'views/'):
        for file in files[2]:
            if file.endswith('.yaml'):
                data.update(safe_load(open('views/' + file, 'r', encoding='UTF8')))

    return data

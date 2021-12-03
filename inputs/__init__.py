from pathlib import Path


def get_file_data(file_name, split_lines=True):
    file_abs_path = f'{Path(__file__)}/../{file_name}.txt'

    with open(file_abs_path, 'r', encoding='UTF-8') as file:
        if split_lines:
            return file.read().splitlines()

        return file.read()

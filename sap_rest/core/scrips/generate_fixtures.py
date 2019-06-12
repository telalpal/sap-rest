"""
script for generation fixtures from data
provided by https://github.com/OpenUpSA/pocket-reporter/tree/master/src/data/saved
"""
import json
import os
from typing import List, Dict

FOLDERS_PATH = './saved/folders/'
QUESTIONS_PATH = './saved/questions/'
RESOURCES_PATH = './saved/resources/'


def read_files(path: str) -> List[Dict]:
    files = []
    result = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    for file in files:
        try:
            print(file)
            try:
                with open(file) as json_file:
                    data = json.load(json_file)
                    result.append(data)
            except ValueError:
                print(f'cannot decode JSON from file "{file}"')
        except OSError:
            print(f'File "{file}" open error')

    return result


if __name__ == '__main__':
    folders_data = read_files(FOLDERS_PATH)
    questions_data = read_files(QUESTIONS_PATH)
    resources_data = read_files(RESOURCES_PATH)

    # collection data from folders
    icons = []
    folders = []
    icon_pk_counter = 1
    folder_pk_counter = 1
    for folder in folders_data:
        icon_name = folder.get('icon', None)
        if icon_name:
            icons.append({
                'model': 'core.Icon',
                'pk': icon_pk_counter,
                'fields': {
                    'name': icon_name,
                }
            })
            icon_pk_counter += 1
        else:
            print(f'Icon without name, skipping')

        folder_title = folder.get('title', None)
        if folder_title and icon_name:
            folders.append({
                'model': 'core.Folder',
                'pk': folder_pk_counter,
                'fields': {
                    'icon': icon_pk_counter,
                    'title': folder_title,
                }
            })
            folder_pk_counter += 1
        else:
            print(f'Icon without name or Folder without title, skipping')
    print(folders)

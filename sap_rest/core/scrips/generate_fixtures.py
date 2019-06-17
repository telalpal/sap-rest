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
    templates = []
    resources = []
    questions = []
    icon_pk_counter = 1
    folder_pk_counter = 1
    template_pk_counter = 1
    resource_pk_counter = 1
    question_pk_counter = 1
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

            # collecting relations to templates
            folder_questions = folder.get('questions', [])
            for question_template in folder_questions:
                if (
                    isinstance(question_template, dict)
                    and question_template.get('content')
                    and question_template.get('content').strip()
                ):
                    templates.append({
                        'model': 'core.Template',
                        'pk': template_pk_counter,
                        'fields': {
                            'folder': folder_pk_counter,
                            'title': question_template['content'],
                        }
                    })
                    template_pk_counter += 1

            folder_resources = folder.get('resources', [])
            for folder_resource in folder_resources:
                if (
                    isinstance(folder_resource, dict)
                    and folder_resource.get('content')
                    and folder_resource.get('content').strip()
                ):
                    resources.append({
                        'model': 'core.Resource',
                        'pk': resource_pk_counter,
                        'fields': {
                            'folder': folder_pk_counter,
                            'title': folder_resource['content'],
                        }
                    })
                    resource_pk_counter += 1
            # incrementing pk's at end
            icon_pk_counter += 1
            folder_pk_counter += 1
        else:
            print(f'!!!Icon without name or Folder without title, skipping')

    def find_template_id(template_title):
        for template in templates:
            if template['fields']['title'] == template_title:
                return template['pk']
    # collecting data from questions folder
    for question in questions_data:
        title = question.get('title')
        template_id = find_template_id(title)
        if not template_id:
            print(f'Template "{title}" not found, skipping questions')
            break
        for concrete_question_dict in question.get('questions', []):
            concrete_question = concrete_question_dict.get('question')
            questions.append({
                'model': 'core.Question',
                'pk': question_pk_counter,
                'fields': {
                    'template': template_id,
                    'text': concrete_question,

                }
            })
            # incrementing pk's at end
            question_pk_counter += 1


    def find_resource(_title):
        for _resource in resources:
            if _resource['fields']['title'] == _title:
                return _resource
    # collecting data from resources folder
    for resource in resources_data:
        title = resource.get('title')
        body = resource.get('body')
        resource_dict = find_resource(title)
        if not resource_dict:
            print(f'Resource "{title}" not found, skipping...')
            continue
        resource_dict['fields']['body'] = body

    # finally writing fixtures
    fixtures = []
    for values in [icons, folders, templates, resources, questions]:
        for value in values:
            fixtures.append(value)
    with open('fixtures.json', 'w') as outfile:
        json.dump(fixtures, outfile, indent=4)
        print('done!')

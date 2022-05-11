import os
import yaml

dict_data = {
    "name": "guoguo",
    "gender": "female",
    "county": "China",
    "city": "成都"
}

file_dir = os.path.join(os.path.dirname(os.path.relpath(__file__)), 'testyamldump.yaml')

with open(file_dir, 'w', encoding='utf-8') as f:
    yaml.dump(dict_data, f, encoding='utf-8', allow_unicode=True)

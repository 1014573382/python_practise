import os
import yaml

dict_data = {
    "name": "guoguo",
    "gender": "female",
    "county": "China",
    "city": "成都"
}
# os.path.dirname(__file__) 获取当前文件所在的目录(去掉了文件名，返回目录)
# os.path.realpath(__file__) 获取当前执行脚本的绝对路径。
file_dir = os.path.join(os.path.dirname(os.path.relpath(__file__)), 'testyamldump.yaml')

with open(file_dir, 'w', encoding='utf-8') as f:
    yaml.dump(dict_data, f, encoding='utf-8', allow_unicode=True)

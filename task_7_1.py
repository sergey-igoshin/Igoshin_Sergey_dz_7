"""
DZ 7_1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
import os
root = 'my_project'
directories = ['settings', 'mainapp', 'adminapp', 'authapp']
for dir in directories:
    if not os.path.exists(root) or (os.path.exists(root) and not os.path.exists(os.path.join(root, dir))):
        path = os.path.join(root, dir)
        os.makedirs(path)

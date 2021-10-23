"""
DZ 7_3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить;
обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён);
предусмотреть возможные исключительные ситуации;
это реальная задача, которая решена, например, во фреймворке django.
"""
import os

root = 'my_project'
directories = ['mainapp', 'authapp']
files = ['base.html', 'index.html']
for dir in directories:
    for file in files:
        if not os.path.exists(root) or \
                (os.path.exists(root) and not os.path.exists(os.path.join(root, dir))) or \
                (os.path.exists(root) and os.path.exists(os.path.join(root, dir)) and not os.path.exists(
                    os.path.join(root, dir, file))):
            path = os.path.join(root, dir, file)
            os.makedirs(path)

import os
import shutil

# Задача-1:
# Напишите скрипт создающий директории dir_1 - dir_9 в папке из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def create_folders(folder_name):
    try:
        os.mkdir(folder_name)
        print("Folder {} was created".format(folder_name))
    except FileExistsError as e:
        if e.errno == 17:
            print("Directory {} is exist".format(folder_name))


def remove_folders(folder_name):
    try:
        os.rmdir(folder_name)
        print("Folder {} was deleted".format(folder_name))
    except FileNotFoundError as e:
        if e.errno == 2:
            print("Directory \"dir_{}\" doesn't exist".format(i))

# Задача-2:
# Напишите скрипт отображающий папки текущей директории


def show_current_dir():
    dir_list = os.listdir()
    for f in dir_list:
        if os.path.isdir(f):
            print(f)

# Задача-3:
# Напишите скрипт создающий копию файла, из которого запущен данный скрипт


def copy_current_file():
    split = str.split(__file__, ".")
    shutil.copy(__file__, split[0] + "_copy." + split[1])


# Additional functions for task hw05_normal.py

def change_directory(new_path):
    os.chdir(new_path)

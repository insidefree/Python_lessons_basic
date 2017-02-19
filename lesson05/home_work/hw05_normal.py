import sys
import lesson05.home_work.hw05_easy as my_utils


# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов: 1, 3,4, программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/прейти"

# Для решения данной задачи используйте алоритмы из задания easy,
# оформленныйе в виде соответствующих функций, и импортированные в данный файл из easy.py


# my_utils.copy_current_file()
# print(sys.argv)


def print_help():
    print("cd - change directory --> example: 'python hw05_normal.py cd full_new_path'")
    print("ls - list directory --> example: 'python hw05_normal.py ls'")
    print("rmdir - remove directory --> example: 'python hw05_normal.py rmdir directory_name'")
    print("mkdir - make directory --> example: 'python hw05_normal.py mkdir directory_name'")
    print("exit - quit from script --> example: 'python hw05_normal.py exit'")


action_container = {
    "help": print_help,
    "cd": my_utils.change_directory,
    "ls": my_utils.show_current_dir,
    "rmdir": my_utils.remove_folders,
    "mkdir": my_utils.create_folders,
    "exit": sys.exit
}

if len(sys.argv) > 1:
    command = sys.argv[1]
    command_args = sys.argv[2:]
    try:
        if len(command_args) > 0:
            action_container[command](command_args[0])
        else:
            action_container[command]()
    except KeyError as e:
        print("Error: ", e)

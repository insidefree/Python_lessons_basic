import os


def copy_file(current_file_name, copy_file_name):
    path = os.getcwd()
    print(path)
    os.rename(path + "\\" + current_file_name, copy_file_name)


copy_file("test.txt", "copy")

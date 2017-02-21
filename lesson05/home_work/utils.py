import os

# import shutil
# import platform
#
#
# def copy_file(*args):
#     print(args)
#     path_split = str.split(args[0][0], "/" if platform.system() is "Windows" else "\\")
#     print(path_split)
#     if bool(args[0][2]):
#         dist_path = args[0][2]
#     file_name_split = str.split(args[0][1], ".")
#     shutil.copy(args[0][1], file_name_split[0] + "_copy." + file_name_split[1])
#
#
#
args = [1, 2, 3]
print(bool(args[4]))

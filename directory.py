import sys
import os
import sys
# path = sys.path

# name = str(input("enter a directory"))

# res = []
# def find_path(name):
#     # for i in path:
# if name in path:
#     for path in os.listdir(name):
#     # check if current path is a file
#         if os.path.isfile(os.path.join(name, path)):
#             res.append(path)
#     print(res)

def dir_tree(path):
    print(path)
    if os.path.isdir(path):
        for i in os.listdir(path):
            dir_tree(path +"/"+i)

dir_name = input("enter the directory : ")

dir_tree(dir_name)






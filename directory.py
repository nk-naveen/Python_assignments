import os

def dir_tree(path):
    print(path)
    if os.path.isdir(path):
        for i in os.listdir(path):
            dir_tree(path +"/"+i)

dir_name = input("enter the directory : ")

dir_tree(dir_name)






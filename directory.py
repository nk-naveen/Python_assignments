import os

def dir_tree(path, l=0):
    print(("|  "*l)+'|--'+ os.path.basename(path))
    if os.path.isdir(path):
        for i in os.listdir(path):
            dir_tree(path +"/"+i,(l+1))

dir_name = input("enter the directory : ")
dir_tree(dir_name)

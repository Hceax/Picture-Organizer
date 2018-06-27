# -*- coding: utf-8 -*
import os
def rename_files():
    #1 获取文件的名字
    file_list = os.listdir(r"./x")
    # 获取当前工作目录
    saved_path = os.getcwd()
    print("Current Working Directory is"+saved_path)
    # 改变工作目录至当前工作目录
    os.chdir(r"./x")

    n=0
    #2 给每一个文件重命名
    for file_name in file_list:
        print("Old Name - "+file_name)

        newname='T'+str(n+1)+'.JPG'
        os.rename(file_name,newname)
        n=n+1
    os.chdir(saved_path)
    
rename_files()

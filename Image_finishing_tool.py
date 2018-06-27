#!/usr/bin/python
# -*- coding: utf-8 -*
__author__ = 'Hceax'
import os
from Tkinter import *
from tkMessageBox import *
import tkFileDialog  
import tkMessageBox

root = Tk()

#屏幕居中
def center_window(w=300, h=200):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#获得文件目录
def get_directory():
    global filename  
    #创建文件对话框,只打开txt类型文件  
    filename = tkFileDialog.askdirectory(parent=root,initialdir='/',title=('选择路径'))
    folder.set(filename)  
 
#制作信息
def about():
    showinfo("Say Hello", "开发者名单\nHceax\nuncleq")
    
#文件重命名核心函数
def rename_files():
    filename = 1
    #1 获取文件的名字
    if(openPath.get() == ""):
        showinfo("fail", "请打开需整理图片所在的文件夹")
        return
    file_list = os.listdir(openPath.get())
    # 改变工作目录至当前工作目录
    os.chdir(openPath.get())

    #检测排除隐藏文件
    db=0
    for num in range(0,len(file_list)):
        #Thumbs.db是图片缓存文件，并且是隐藏文件
        if(file_list[num]=="Thumbs.db"):
            db+=1

    #2 给每一个文件重命名
    for num in range(0,len(file_list)):
        if(file_list[num]!="." and file_list[num]!=".." and file_list[num]!="Thumbs.db"):
            print("Old Name - "+file_list[num])
            if(openPath.get() == ""):
                newname=(fill_in_zero(len(file_list)-db,num+1)+str(filename)+'.JPG')
            else:
                newname=(prefix.get()+fill_in_zero(len(file_list)-db,num+1)+str(filename)+'.JPG')
            os.rename(file_list[num],newname)
            filename += 1
    showinfo("succeed", "图片整理完毕")

#比较当前文件与总文件数之间的差位数并返回补零个数，
#比如当前文件是12，总文件数9800，差位数为2，补2个“0”，变为“0012”
def fill_in_zero(len,num):
    i = bit_recursion(len)-bit_recursion(num)
    zero = ""
    for j in range(0,i):
        zero += "0"
    return zero

#递归判断10进制位数
def bit_recursion(x):
    #flag = 0
    if(x>0):
        x=x/10
        flag = bit_recursion(x)+1
        return flag
    else:
        return 0

#菜单
menubar = Menu(root)  
  
#创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#关于菜单
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
  
#显示菜单
root.config(menu=menubar)

#main 

fm1 = Frame(root)
label1 = Label(fm1)
label1['text'] = '文件路径：'
label1.pack(side=LEFT, fill=X, expand=YES)
folder = StringVar()
folder.set('')
openPath = Entry(fm1)
openPath['textvariable'] = folder
openPath.pack(side=LEFT, fill=X, expand=YES)
openButton = Button(fm1)
openButton['text'] = 'open'
openButton['command'] = get_directory
openButton.pack(side=LEFT, fill=BOTH, expand=YES)
fm1.pack(side=TOP, fill=X, expand=YES)


fm2 = Frame(root)
label2 = Label(fm2)
label2['text'] = '文件前缀：'
label2.pack(side=LEFT, fill=X, expand=YES)
prefix = StringVar()
prefix.set('')
filePrefix = Entry(fm2)
filePrefix['textvariable'] = prefix
filePrefix.pack(side=LEFT, fill=X, expand=YES)
label3 = Label(fm2)  
label3['text'] = '         '
label3.pack(side=LEFT, fill=X, expand=YES)
fm2.pack(side=TOP, fill=X, expand=YES)


StartButton = Button(root)
StartButton['text'] = 'start'
StartButton['fg'] = "blue"
StartButton['command'] = rename_files
StartButton.pack(side=TOP, fill=BOTH, expand=YES)


root.title("图片整理工具")
center_window(300, 100)
root.mainloop()
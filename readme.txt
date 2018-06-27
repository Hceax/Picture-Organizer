#Filename_batch.py是一个文件整理程序，支持自定义文件名，支持同一文件夹内不同类型文件分别进行整理
#Image_finishing_tool.py是一个图片快速整理程序，实际上和Filename_batch.py十分相似
#rename_files.py是Filename_batch.py的命令行版本

#py程序可以根据以下教程变为可运行的exe文件
#http://jingyan.baidu.com/article/67508eb43344829cca1ce4f1.html
#打开CMD窗口，将工作目录切换到python文件所在文件夹，并输入命令
python setup.py py2exe

##目录结构：
#setup.py:生成exe脚本
#rename_files.py:命令行脚本
#Image_finishing_tool.py:图片整理GUI
#Filename_batch.py:自定义文件名批量修改GUI

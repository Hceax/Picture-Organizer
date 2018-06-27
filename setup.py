from distutils.core import setup
import py2exe

#修改windows = ['']的值，即可打包目标文件
setup(windows = ['Image_finishing_tool.py'])

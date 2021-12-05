"""
描述
    用来给用户点击，来完成某种功能的控件，一般是矩形
    例如
        登录按钮，注册按钮，关闭按钮等

继承：QAbstractButton
功能
    创建按钮控件
        QPushButton：创建一个无父控件的按钮控件
        QPushButton(parent):创建控件的同时，设置父控件
        QPushButton(text,parent)：创建控件的同时，设置提示文本和父控件
        QPushButton(icon,text,parent):创建控件的同时，设置图标，提示文本和父控件

    菜单
    边框是否保持扁平
    默认处理

信号

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("构造函数")
w.resize(500, 500)


# 单独的按钮控件
def pureButton():
    btn = QPushButton()

    # 设置父控件
    btn.setParent(w)
    btn.show()


def textButton():
    btn = QPushButton('确定', w)


def iconButton():
    address = r"C:\Users\RONG\Pictures\Camera Roll\地图2.jpg"
    btn = QPushButton(QIcon(address), '取消', w)
    btn.move(200, 200)


# pureButton()
textButton()
iconButton()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

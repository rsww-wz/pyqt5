"""
API
    setIcon(QIcon(address))
        设置图标
    setIconSize(QSzie(w,h))
        设置图标大小
    icon()
        获取图标
    iconSize()
        获取图标大小
应用场景
    用户点击按钮前，给用户的图标提示
案例
    创建一个按钮，设置自定义图标，并调整图标大小
"""
# from PyQt5.Qt import *
import sys

# 创建程序对象
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("图标相关")
w.resize(500, 500)


def Icon():
    btn = QPushButton(w)
    btn.setText('地图')
    btn.move(200, 200)

    # 设置图标
    address = r"C:\Users\RONG\Pictures\Camera Roll\地图2.jpg"
    # btn.setIcon(QIcon(address))
    icon = QIcon(address)
    btn.setIcon(icon)

    # 设置大小
    # btn.setIconSize(QSize(50,50))
    size = QSize(50, 50)
    btn.setIconSize(size)

    # 获取按钮信息
    print(btn.icon())
    print(btn.iconSize())


Icon()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

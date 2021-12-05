"""
功能
    窗口只能在设定的最大尺寸和最小尺寸中间调整，不能超过最大和最小尺寸
    如果resize函数设置的尺寸超过最大或者最小尺寸，只能按照最大或者最小尺寸

API
    获取尺寸
        minimumWidth():最小尺寸宽度
        minimumHeight()：最小尺寸高度
        minimumSize()：最小尺寸

        maxmumWidth():最大尺寸宽度
        maxmumHieght()：最大尺寸高度
        maximunSize()：最大尺寸

    设置尺寸
        setMaximumWidth()：设置最大宽度
        setMaximumHeight():设置最大高度
        setMaximumSize()：设置最大尺寸
        setMinimumWidth()：设置最小宽度
        setMinimumHeight()：设置最小高度
        setMinimumSize()：设置最小尺寸

应用场景

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("最大最小尺寸测试")


def setbothsize():
    # 设置最大尺寸
    w.setMaximumSize(800, 800)
    # 设置最小尺寸
    w.setMinimumSize(200, 200)


def setsinglesize():
    w.setMaximumHeight(500)
    w.setMaximumWidth(600)

    w.setMinimumHeight(100)
    w.setMinimumWidth(100)


def getsize():
    # 获取最小尺寸
    print(w.minimumHeight())
    print(w.minimumWidth())
    print(w.minimumSize())

    # 获得最大尺寸
    print(w.maximumHeight())
    print(w.maximumWidth())
    print(w.maximumSize())


setsinglesize()
getsize()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

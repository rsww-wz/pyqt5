"""
1.控件的坐标系统
    左上角为坐标原点，向右为X轴正方向，向下为Y轴正方向
    即屏幕上边向右为X轴正方向，屏幕左边向下为Y正方向
    Z轴从坐标原点指向屏幕里面

    控件位置参照
        父控件
        顶层控件参照桌面

2. API
    获取位置
    注意：如果要获取控件的位置，一定要在控件设置完成再获取控件的位置，不然位置可能是错的
        窗口位置
            x()
                相对于父控件的x位置，顶层控件没有父控件，则相对于桌面x位置
            y()
                和x()类似
            pos()
                x和y的结合
                QPoint(x,y)

        用户区域大小
            width()
                控件的宽度，不包含任何窗口框架
            height()
                控件的高度，不包含任何窗口控件
            size()
                width和height的组合
                QSize(width,height)

        控件相对于用户区域的尺寸
        geometry()
            用户区域相对于父控件位置的尺寸组合
            QRect(x,y,width,height)
            x,y是相对于窗口位置，后面两个是大小尺寸
        rect()
            0,0,width,height的组合
            QRect(0,0,width,height)  相当于size

        整个窗口
            frameSize()
                窗口大小
            frameGeometry()
                窗口的位置和尺寸

    设置位置
        move(x,y)
            操控的是x,y，也就是pos
        resize(width,height)
            操控的是宽高，不包括窗口的框架
        setGeometry(x_noFrame,y_noFrame,width,height)
            此处参数为用户区域
        adjustSize()
            根据内容自适应大小
        setFixedSize()
            设置固定尺寸，固定窗口大小
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
window = QWidget()

# 设置控件
window.setWindowTitle("")

def get_postition():
    # 整个窗口
    # 获取窗口的x坐标
    print(window.x())
    # 获取窗口的y坐标
    print(window.y())
    # 获取窗口的坐标
    print(window.pos())

    # 用户区域
    print(window.width())
    print(window.height())
    print(window.size())

    # 控件相对用户区域
    print(window.geometry())
    print(window.rect())

    # 框架
    print(window.frameSize())
    print(window.frameGeometry())

def set_postition():
    # 移动pos
    #window.move(100,200)

    # 设置resize
    #window.resize(500,500)

    # 同时设置用户区域位置和用户区域大小
    #window.setGeometry(0,0,400,400)

    # 自动调整
    #window.adjustSize()

    # 固定尺寸
    window.setFixedSize(200,200)

def example1():
    window1 = QWidget()
    window1.resize(500,500)
    window1.move(300,300)

def example2():
    # 功能：通过给定的个数你负责在一个窗口内创建相应个数的子控件
    # 要求：按照九宫格的布局摆放，一列3个

    window.resize(500, 500)

    # 控件个数
    count = 10

    #计算一个控件的宽度
    column = 3
    widget_width = window.width() / count

    # 计算一个控件的高度
    row = (count - 1) // column + 1
    widget_height = window.height() / row

    for i in range(0,count):
        item = QWidget(window)
        item.resize(widget_width,widget_height)

        #计算x移动距离
        width_x = i % column * widget_width
        width_y = i // column * widget_height
        item.move(width_x,width_y)

        item.setStyleSheet('background-color:blue;border:1px solid red;')

# get_postition()
# set_postition()
# example1()
example2()

# 展示控件
window.show()

# 程序循环
sys.exit(app.exec_())


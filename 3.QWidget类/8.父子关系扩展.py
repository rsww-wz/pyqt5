"""
API
    childAt(x,y)
        获取在指定坐标的控件
    parentWidget()
        获取指定控件的父控件
    childRect()
        所有子控件组成的边界矩形

"""

from PyQt5.Qt import *
import sys

# 点击控件变色
class Label(QLabel):
    def mousePressEvent(self, QMouseEvent):
        self.setStyleSheet('background-color:red;')

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = Label()

# 设置控件
w.setWindowTitle("父子关系扩展")
w.resize(500,500)

def label():
    label1 = QLabel(w)
    label1.move(100,200)
    label1.resize(100,100)
    label1.setStyleSheet('background-color:red;')
    label1.setText('morning')

    label2 = QLabel(w)
    label2.move(200,200)
    label2.resize(100,100)
    label2.setStyleSheet('background-color:green;')
    label2.setText('afternoon')

    label3 = QLabel(w)
    label3.move(300,200)
    label3.resize(100,100)
    label3.setStyleSheet('background-color:blue;')
    label3.setText('evening')

    # 查看某个控件的父控件
    print(label2.parentWidget())

def check():
    # 查看该位置是否有控件存在
    print(w.childAt(100, 100))
    print(w.childAt(300, 200))

    # 查看所有子控件组成的边界矩形
    # 前面两个是对角线开始位置，后面两个是对角线结束位置
    print(w.childrenRect())


def example():
    for i in range(1,11):
        label = Label(w)
        label.setText('标签' + str(i))
        label.move(40*i,40*i)

# label()
# check()
example()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

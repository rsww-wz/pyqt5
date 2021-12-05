"""
状态提示(展示在状态栏)
    statusTip()
    setStatusTip(str)
    效果：鼠标停在控件上时，展示在状态栏

工具提示（展示在旁边）
    toolTip()
    setToolTip(str)
    时长：toolTipDuration()
        setToolTipDuration(msec)
    效果：鼠标悬停在控件上一会后，展示在旁边

这是什么
    whatsThis()
    setWhatsThis(str)
    效果：切换到“查看这是什么”模式，点击该控件时显示

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
# w = QWidget()

# 符合窗口控件
w = QMainWindow()

#懒加载，用到的时候才会创建
w.statusBar()

# 设置控件
w.setWindowTitle("信息提示")
w.resize(500,500)

def message():
    #当鼠标停留在窗口控件身上之后，在状态栏提示的一段文本
    w.setStatusTip('这是窗口')
    # 获取文本
    print(w.statusTip())

def label_():
    label = QLabel(w)
    label.setText('hello world')
    label.move(300,300)

    label.setStatusTip('This is a label')

    # 设置提示信息
    label.setToolTip('这是一个标签')
    # 设置显示时长，单位是ms
    label.setToolTipDuration(2000)
    # 获取展示时长
    print(label.toolTipDuration())


message()
label_()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())


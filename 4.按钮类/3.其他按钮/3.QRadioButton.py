"""
描述
    一般用于给用户提供若干选项中的单选操作
    此按钮左侧会有一个圆形图标，用于表示用户的选中状态
    当选中一个会自动取消另一个

继承：QAbstractButton
功能作用
    常用继承父类操作
        图标
            setIcon(QIcon)
        快捷键
            文本加&
            setShortcut()
信号
    都是继承自父类
    常用信号：toggled(bool)
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("QRadioButton")
w.resize(500,500)

# 创建按钮
btn1 = QRadioButton('男',w)
btn1.move(200,100)

btn2 = QRadioButton('女',w)
btn2.move(200,150)

def button():
    window1 = QWidget(w)
    window1.resize(100,100)
    window1.move(100,200)
    window1.setStyleSheet('background-color:red;')

    btn3 = QRadioButton('yes',window1)
    btn3.move(10,10)
    btn4 = QRadioButton('no',window1)
    btn4.move(10, 30)

    window2 = QWidget(w)
    window2.resize(100, 100)
    window2.move(210, 200)
    window2.setStyleSheet('background-color:green;')

    btn5 = QRadioButton('boy',window2)
    btn5.move(10,10)
    btn6 = QRadioButton('girl',window2)
    btn6.move(10, 30)

button()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

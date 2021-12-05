"""
setText(str):设置内容文本
    text():获取真实内容文本
    displayText():获取用户能看到的内容文本
    insert(newText):在光标处插入文本

应用场景
    通过代码来控制输入文本内容
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("设置文本内容")
w.resize(500,500)

# 创建空白文本框
def blank_text():
    le = QLineEdit(w)

# 为文本框添加内容
def add_text():
    le = QLineEdit(w)
    # 设置文本

    le.setText('hello world')
    # 统一设置

    box = QLineEdit('Good morning', w)
    box.move(200, 300)

# 获取文本内容
def get_text():
    le = QLineEdit(w)

    # 设置文本
    le.setText('hello world')

    # 获取真实文本内容，返回的是对象
    print(le.text)

    # 获取实际看到的文本内容,返回的是看到的文本
    print(le.displayText())

# 在光标处插入文本
def insert_text():
    le = QLineEdit(w)

    le.setText('hello world ')

    le.insert('newText')

# 案例1:交换文本框内容
def example1():
    le1 = QLineEdit(w)
    le1.move(200,200)

    le2 = QLineEdit(w)
    le2.move(200,250)

    btn = QPushButton('点击交换',w)
    btn.move(200,300)

    def cao():
        text1 = le1.displayText()
        text2 = le2.displayText()
        le1.setText(text2)
        le2.setText(text1)

    btn.clicked.connect(cao)

# 案例2
def example2():
    le1 = QLineEdit(w)
    le1.move(200, 200)

    le2 = QLineEdit(w)
    le2.move(200, 250)

    btn = QPushButton('点击复制', w)
    btn.move(200, 300)

    def cao():
        text1 = le1.text()
        le2.setText(text1)

    btn.clicked.connect(cao)

# blank_text()
# add_text()
# get_text()
# insert_text()
# example1()
example2()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

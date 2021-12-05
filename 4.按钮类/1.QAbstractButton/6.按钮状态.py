"""
API
    isDown()
        是否按下按钮
    setDown(bool)
        设置按钮，是否被按下

    isChecked()
        是否选中了按钮
    setChecked(bool)
        设置按钮，是否被选中

    isCheckable()
        按钮是否可以被选中
    setCheckable(bool)
        设置按钮，是否可以被选中

    toggle()
        切换选色与非选中状态
        可以用来做反选

    继承于QWidget中的能用状态
        isEnabled()
        setEnabled(bool)

应用场景
    判定按钮状态
"""

# from PyQt5.Qt import *
import sys

# 创建程序对象
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QCheckBox

app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("按钮状态")
w.resize(500, 500)


def buttonFlags():
    btn1 = QPushButton(w)
    btn1.move(200, 150)
    btn1.setText('确定')

    btn2 = QRadioButton(w)
    btn2.move(200, 200)
    btn2.setText('确定')

    btn3 = QCheckBox(w)
    btn3.move(200, 250)
    btn3.setText('确定')

    # 三个按钮都置位按下状态
    btn1.setDown(True)
    btn2.setDown(True)
    btn3.setDown(True)

    # 判断按钮是否为按下状态
    print(btn1.isDown())
    print(btn2.isDown())
    print(btn3.isDown())

    # 设置按钮是否被选中
    btn1.setChecked(True)
    btn2.setChecked(True)
    btn3.setChecked(True)

    # 判断按钮是否被选中
    print(btn1.isChecked())
    print(btn2.isChecked())
    print(btn3.isChecked())

    # 设置按钮是否可被选中
    # 可以点，但是不能被选中
    btn1.setCheckable(True)
    btn2.setCheckable(True)
    btn3.setCheckable(True)

    # 判断按钮是否可被选中
    print(btn1.isCheckable())
    print(btn2.isCheckable())
    print(btn3.isCheckable())

    # 设置按钮是否被选中，不能选的直接变成灰色（不能用）
    # btn1.setEnabled(False)
    # btn2.setEnabled(False)
    # btn3.setEnabled(False)

    def cao():
        # 选中与非选中之间切换
        btn2.toggle()
        btn3.toggle()

    btn1.pressed.connect(cao)


buttonFlags()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

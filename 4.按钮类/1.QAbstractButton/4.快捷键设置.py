"""
作用
    通过制定的看盘，触发按钮的点击
方式1
    有提示文本，如果提示文本包含&符号('&')的，会自动创建快捷键（快捷键是alt+第一个字母）
方式2
    没有提示文本
    setShortcut("快捷键组合")

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("快捷键设置")
w.resize(500,500)

def has_text():
    btn = QPushButton(w)
    btn.move(200,200)
    btn.setText('&ab')
    btn.pressed.connect(lambda :print('按钮被点击了'))

def no_text():
    btn = QPushButton(w)
    btn.move(200, 200)
    btn.setText('hello')
    btn.setShortcut('alt+f')


# has_text()
no_text()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

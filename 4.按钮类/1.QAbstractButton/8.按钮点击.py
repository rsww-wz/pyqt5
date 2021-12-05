"""
API
    click()
        普通点击
    animateClick(ms)
        动画点击

应用场景
    使用代码触发按钮点击
    发射相关信号
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("按钮点击")
w.resize(500,500)

btn = QPushButton(w)
btn.move(200,200)
btn.setText('这是按钮')
btn.pressed.connect(lambda :print('点击了这个按钮'))

# 代码执行的时候就模拟点击了按钮
btn.click()

# 代码执行的时候也会模拟点击按钮，并且会设置按钮点击动画（相当于设置鼠标点击按钮不放开鼠标的时间）
btn.animateClick(1000)

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())


"""
API
    setFlat(bool)
        默认值为False
        设置了此属性，除非按下按钮，否则大多数样式不会绘制按钮背景
    isFlat()
        获取当前按钮扁平化风格
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("扁平化")
w.resize(500, 500)

btn = QPushButton('确定', w)
btn.move(200, 200)
btn.setStyleSheet('background-color:cyan;')

# 设置扁平化风格,只有点击按钮的时候才会显示背景
btn.setFlat(True)

# 获取扁平化风格
print(btn.isFlat())

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

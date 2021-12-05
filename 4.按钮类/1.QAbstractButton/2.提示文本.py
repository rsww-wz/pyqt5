"""
API
    setText(str)
        设置按钮提示文本
    text()
        获取按钮提示文本
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("提示文本")
w.resize(500, 500)


def text():
    btn = QPushButton(w)
    btn.setText('1')
    btn.move(200, 200)

    # 信号与槽
    def cao():
        # 获取文本
        text = btn.text()
        text = int(text) + 1
        btn.setText(str(text))

    btn.pressed.connect(cao)


text()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

"""
API
    setAutoRepeat(tool)
        设置自动重复
    setAutoRepeatInterval(毫秒)
        设置自动重复检测间距
    setAutoRepeatDelay(毫秒)
        设置初次检测延迟
    autoRepeat()
        获取是否自动重复
    autoRepeatInterval()
        获取自动重复检测间距
    autoRepeatDelay()
        获取初次检测延迟

应用场景
    当用户点击按钮后，想快速重复性响应时设置

理解
    如果一个按钮点击加1，如果点击了不松手就会一直加一；可以设置首次点击时间，如果超过了这个时间，还是按下，就会一直加一
    每次加一的时间间隔可以设置
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("自动重复")
w.resize(500, 500)


def autoRepeat():
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

    # 设置自动重复
    btn.setAutoRepeat(True)

    # 设置首次自动重复时间间隔
    btn.setAutoRepeatDelay(2000)

    # 设置自动重复检测间距
    btn.setAutoRepeatInterval(500)

    # 获取是否自动重复
    print(btn.autoRepeat())

    # 获取自动重复检测间距
    print(btn.autoRepeatInterval())

    # 获取初次检测延迟
    print(btn.autoRepeatDelay())


autoRepeat()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

"""
API
    setPlaceholderText(notice_str)
    placeholderText()

应用场景
    在用户输入文本之前，给用户提示语句
    文本内容框
        空：显示提示文本
        空不：隐藏提示文本

理解
    就是在没有输入文本之前，提示这个框是干什么的，输入文本之后就消失了
"""

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('占位提示字符串')
window.resize(600,600)

def Tipstr():
    le1 = QLineEdit(window)
    le1.move(200,200)
    le1.setPlaceholderText('请输入账号')

    le2 = QLineEdit(window)
    le2.move(200,250)
    le2.setPlaceholderText('请输入密码')

    # 获取占位文本
    print(le1.placeholderText())
    print(le2.placeholderText())

Tipstr()

window.show()
sys.exit(app.exec_())



"""
API
    设置文本框边距
    setTextMargins(int left,int top,int right, int bottom)
    查看文本框边距
    getTextMargins()

    和QLable边距的设定一样
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("文本框边距")
w.resize(500,500)

le = QLineEdit(w)
le.move(40,40)
le.resize(300,300)

def setmargins():
    # 设置文本边距
    le.setTextMargins(20,20,20,20)
    le.setStyleSheet('background-color:cyan;')

    # 查看文本边距
    print(le.textMargins())

setmargins()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

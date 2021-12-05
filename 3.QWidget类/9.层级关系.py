"""
API
    lower()
        将控件降低到最底层
    raise_()
        将控件提升到最上层
    a.stackUnder(b)
        让a放在b下面
    注意：以上操作专职同级控件

应用场景
    需要调整控件z轴顺序
"""
from PyQt5.Qt import *
import sys

# 被点击控件显示在最上层
class Label(QLabel):
    def mousePressEvent(self, evt):
        self.raise_()

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("层级关系调整")
w.resize(500,500)

def adjust():

    #标签1
    label1 = Label(w)
    label1.resize(200,200)
    label1.move(200,200)
    label1.setStyleSheet('background-color:cyan;')

    # 标签2
    label2 = Label(w)
    label2.resize(200, 200)
    label2.move(300, 300)
    label2.setStyleSheet('background-color:red;')

    # 向下调整关系
    # label1.lower()
    # label2.lower()

    # 向上调整
    # label1.raise_()
    # label2.raise_()

    # 相对位置关系
    # label1.stackUnder(label2)
    # label2.stackUnder(label1)

adjust()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())


"""
API
    设置内容边距
        setContentMargins(左，上，右，下)
        理解：其实设置文本的页边距，如果不设置文本的大小就是整个控件的大小

    获取内容边距
        getContentMargins()
        返回值：元组类型，左，上，右，下
        理解：其实设置的边距

    获取内容区域
        contentsRect()
        理解：整个控件大小减去边距后，剩下的内容区域大小，也就是要设置的内容区域的大小

注意：必须是控件本身留足够对应的大小

应用场景
    调整控件内容边距，显得更好看
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("内容边距测试")
w.resize(500,500)

def margins():
    # 现在内容区域是整个控件的大小
    label = QLabel(w)
    label.setText('hello world')
    label.resize(300,300)
    label.setStyleSheet("background-color:cyan;")

    # 获取内容区域
    print(label.contentsRect())

    # 获取内容边距
    print(label.getContentsMargins())

def contentmargins():
    label = QLabel(w)
    label.setText('Good morning')
    label.resize(200,200)
    label.setStyleSheet('background-color:pink;')

    # 设置内容区域
    label.setContentsMargins(100,100,0,0)

    # 获取内容区域
    print(label.contentsRect())

    # 获取内容边距
    print(label.getContentsMargins())

# margins()
contentmargins()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())


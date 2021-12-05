"""
理论基础（通过文本光标，可以操作编辑文本对象，功能基本内容设置一样，但是可实现制定功能）
    概念
        整个文本编辑器其实就是为编辑这个文本提供了一个可视化界面
        简单理解，可以比喻成一个doc文档，使用Word软件打开这个文档，你就是可以随意操控

    操作文本对象的方法有两种
        一种是用系统提供的方法：设置内容，清空内容，复制，剪贴等操作
        另一种是自己用光标控制，实现自定义需求

获取文本文档的方法
    document()
        返回一个对象：QTextDocument

光标
    textCursor()
        返回一个对象：QTextCursor

textCursor:
    获取光标对象
    注意和Cursor的区别
        textCursor是获取文本框内的光标
        Cursor是获取鼠标光标

    获取到光标之后就可以使用QTextCursor类里面的方法了

    后面对文本框的学习也就是学习QTextCursor这个类里面对光标的方法了
"""

""""
补充
QTextDocument
    获取文本内容
    直接继承QObject
QTextCursor
    添加内容
    设置和合并格式
    获取内容相关
    文本选中和清空
    删除内容
    位置相关
    开始和结束编辑标识
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("获取光标")
w.resize(500,500)

te = QTextEdit(w)
te.move(120,100)

btn = QPushButton('获取光标',w)
btn.move(200,300)

btn1 = QPushButton('获取文本',w)
btn1.move(200,350)

def cao():
    # 返回光标对象
    cursor_obj = te.textColor()

    # 打印对标对象
    print(cursor_obj)

def cao1():
    # 获取文本对象
    document_obj = te.document()

    # 打印文本对象
    print(document_obj)

btn.clicked.connect(cao)
btn1.clicked.connect(cao1)

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

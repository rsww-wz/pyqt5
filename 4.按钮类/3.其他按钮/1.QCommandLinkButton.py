"""
描述
    命令链接是Windows Vista引入的新控件
    它的用途是类似于单选按钮的用途，因为他用于在一组互斥选项之间进行选择
    命令链接按钮不应单独使用，而应该作为导向和对话框单选按钮的代替选项
    外观通常类似于平面按钮外观，但除了普通按钮文本之外，它还允许描述性文本

继承：QPushButton

功能
    创建命令链接按钮
        QCommandLinkButton(parent)
        QCommandLinkButton(text,parent)
        QCommandLinkButton(text,descripion,parent)
    描述设置
        setDescription(str)
        description(str)

信号
    完全是QPushButton的信号
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("命令按钮")
w.resize(500,500)

btn = QCommandLinkButton(w)
btn.move(200,150)
btn.setText('确定')
btn.setDescription('这是一段描述文本')

# 统一设置
btn1 = QCommandLinkButton('取消','上一步',w)
btn1.move(200,250)

# 获取按钮信息
print(btn1.description())

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

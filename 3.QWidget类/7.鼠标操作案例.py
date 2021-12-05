"""
事件函数



"""

from PyQt5.Qt import *
import sys

class MyLable(QLabel):
    def enterEvent(self,*args,**kwargs):
        print('鼠标进入')
        self.setText('Good morning')

    def leaveEvent(self,*args,**kwargs):
        print('鼠标离开')
        self.setText('Good afternoon')

    def KeyPressEvent(self,evt):
        QKeyEvent

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("鼠标操作案例")
w.resize(500,500)

# 鼠标进入离开显示不同内容
def label_():
    label = MyLable(w)
    label.move(200,200)
    label.resize(200,200)
    label.setStyleSheet('background-color:cyan;')

# 监听用户输入
# 要求
#   监听用户输入：tab键
#   监听用户输入：Ctrl+S键
#   监听用户输入：Ctrl+shift+A键

label_()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

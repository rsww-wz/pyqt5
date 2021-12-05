"""
if __name__ == __main__:
    判断程序的执行方式
    如果程序是在当前窗口被右键执行的话，会执行if里面的程序
    如果程序是被其他模块导入进来的，就不会执行if里面的程序

    作用：可以模块的调试，在本模块中可以直接运行，被导入后就不会运行
    活动模板字符串：main

面向对象的好处
    控件会有多个属性，不同的控件的属性有可能是相同的，或者只是参数不同
    如果每个控件的属性都写一遍，效率会很低，所以可以使用面向对象的方式
    可以提高代码的可用性，可读性，可修改性

"""

from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("")

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())











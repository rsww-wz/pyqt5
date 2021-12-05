"""
API
    isWidgetType()
        判定是否是一个控件类型

    inherits(父类)
        判定是否是继承某个类，包括直接继承和间接继承

应用场景
    过滤筛选控件

"""

from PyQt5.Qt import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("类型判定测试")
        self.resize(500, 500)
        # self.setup_ui()
        self.example()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("hello world")

        obj = QObject()
        w = QWidget()
        btn = QPushButton()
        label = QLabel()

        objs = [obj, w, btn, label]
        # 判断哪些对象是控件
        for item in objs:
            print(item.isWidgetType())

        print('*' * 60)
        for itme in objs:
            # 判断哪些类继承于QWidget
            print(item.inherits("QPushButton"))

    def example(self):
        label = QLabel(self)
        label.setText("hello")

        label2 = QLabel(self)
        label2.setText('world')
        label2.move(0, 40)

        btn = QPushButton(self)
        btn.setText('点我')
        btn.move(100, 110)

        for item in self.findChildren(QLabel):
            if item.isWidgetType():
                item.setStyleSheet('background-color:cyan;font-size:25px')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())

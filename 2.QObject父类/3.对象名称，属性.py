"""
API
    setObjectName("唯一名称")
        给Qt对象设置一个名称
        一般这个名称是唯一的，当做对俩的id来使用

    objectName
        获取一个Qt对象的名称

    setProperty("属性名称"，"值")
        给Qt对象动态添加一个属性与值

    dynamicpropertyNames()
        获取对象中所有通过setProperty()设置的属性名称

应用场景
    用于qss的id选择器，属性选择器，方便统一设置杨样式
    用于装饰器的信号与槽

"""

from PyQt5.Qt import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("API测试")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        #常规控件
        label_one = QLabel(self)
        label_one.setText("hello world")

        # 设置id属性
        label_two = QLabel(self)
        label_two.move(100,100)
        label_two.setObjectName('notice')
        label_two.setText('Good morning')

        #设置id属性
        label = QLabel(self)
        label.move(200, 200)
        label.setObjectName('notice')
        label.setProperty("notice_level","warning")
        label.setText("Good afternoon")

        # 设置qss样式表
        # label.setStyleSheet("font-size:25px; color:green;")

        # 设置全局qss样式表
        address = r"E:\0-code\Pycharm\GUI\2.QObject父类\3.QObject样式表.qss"
        with open(address,mode='r',encoding='utf-8') as f:
            qApp.setStyleSheet(f.read())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())
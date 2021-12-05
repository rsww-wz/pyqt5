"""
基本概念
    信号和槽是Qt中核心机制，主要作用域对象之间的通讯
    信号：当一个控件的状态发生改变时，向外界发出的信息
    槽：一个执行某些操作的函数或者方法
    所有继承自QWidget的控件都支持信号与槽的机制

信号和槽的理解
    信号是控件发出的信息，槽是对这个信息作出的反应
    把信号和槽连接起来，当触发信号的时候，就会执行槽的程序

机制描述
    手动操作
        连接信号和槽，组织他们的关系
    自动操作
        当信号发生的时候，连接的槽函数会自动执行

基本使用介绍
    信号
        控件内置的信号
        也可以自定义信号
    槽
        不同控件内置的槽函数
        自定义的函数
    连接方法
        object信号.connect(槽函数)
    特性
        一个信号可以连接多个槽函数
        一个信号也可以连接另外一个信号
        信号的参数可以是任何python类型
        一个槽可以监听多个信号

高级


API
    建立连接
        widget.信号.connect(槽)

    取消连接
        obj.disconnect()

    临时取消或者阻止指定控件所有信号与槽的连接
    阻止连接：True
    恢复连接：False
    中间的代码如果有连接会被阻断
    效果相当于先取消连接再建立连接
        widget.blockSignals(bool)

    信号是否被阻止
        widget.signalsBlocked()
        True：是阻断连接
        False：是没有阻断连接

    返回连接到信号的接收器的数量，即查看信号连接了多少个槽
        widget.receivers(信号)

应用场景
    监听信号，响应用户行为
    信号与槽机制

信号
    objectNameChanged(bojectName):对象名称发生变化是发出信号
    destroyed(obj)：对象被销毁时，发出此信号

"""

from PyQt5.Qt import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号处理测试")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("hello world")

        # 信号
        self.obj = QObject()

        # # 槽函数
        # def destroy_cao(self):
        #     print('程序已销毁')

        # 槽函数可以有返回值，返回值是第二个参数，当槽函数执行的时候，会自动传递个信号
        def destroy_cao(obj):
            print('程序已销毁', obj)

        # 连接信号与槽函数
        # destroyed信号是程序被销毁时才会触发，是自动的信号
        self.obj.destroyed.connect(destroy_cao)

        # 销毁程序，触发信号和槽函数
        # del self.obj

        # 改变名称的槽函数
        def obj_name_cao(name):
            print('对象的名称发生了改变', name)

        # 建立连接
        self.obj.objectNameChanged.connect(obj_name_cao)

        # 触发信号
        self.obj.setObjectName('xxx')

        # 打印信号是否被阻断
        print(self.obj.signalsBlocked())

        # 阻断连接
        self.obj.blockSignals(True)
        # 打印信号是否被阻断
        print(self.obj.signalsBlocked())
        # 触发信号
        self.obj.setObjectName('xxoo')
        # 恢复连接
        self.obj.blockSignals(False)
        # 打印信号是否被阻断
        print(self.obj.signalsBlocked())

        # 触发信号
        self.obj.setObjectName('aaa')

        # 取消连接
        self.obj.objectNameChanged.disconnect()

        # 触发信号,但是已经取消连接，所以不会触发槽函数
        self.obj.setObjectName('ooo')

        # 打印信号连接了多少个槽
        print(self.obj.receivers(self.obj.destroyed))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())

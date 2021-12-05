"""
1.什么是控件
    一个程序界面上，各个独立的元素，都是一个矩形区域

2.具备不同的功能
    用户点击
    接收用户输入
    展示内容
    存放其他控件

3.不同的控件
    原理
        每个空控件都会有一些相同的特性，也会有自己独有的特性
        实现方法就是python里面的继承，把相同的特性放在父类，每个控件都是一个子类，继承于父类，子类会有自己的一些特性
        所以学习的时候，应该是先学习父类，然后再学习子类
    相同的共性
        名字
        矩形区域
        位置
        大小
        样式等
    不同的特性
        展示内容
        接收输入
        用户交互
        容器
        框架等

4.常用控件
    基础控件
        按钮
            QPushButton：单击，双击，右击
            QCommandLinkButton：跳转
            QRadioButton：单选框
            QCheckBox：复选框

        输入控件
            纯键盘输入
                QLineEdit：单行输入
                QTextEdit：多行文本（可以有图片，链接等）
                QPlainTextEdit：多行富文本（没有图片，链接等）
                QKeySequenceEdit：快捷键

            步长调整（鼠标+键盘）
                QDataTimeEdit：调时间
                QSpinBox：调数字
                QDoubleSpinBox：调浮点数

            组合框
                QComboBox：选地址

            滑块
                QDial：旋钮
                QSlider：滑块
                QScrollBar：滚动条

            橡皮筋选中

            对话框
                QColorDialog：颜色对话框
                QFileDialog：文件对话框
                QFontDialog:字体对话框
                QInputDialog：输入对话框

            日期
                QCalendarWidget

        展示控件
            标签：QLabel（普通文本、数字 、富文本、图片、GIF）
            LCD：QLCDNumber
            进度条：QProgressBar
            对话框
                QMessageBOx：展示提示消息
                QErrorMessage：错误对话框
                QProgressDialog：进度对话框



    高级控件
        容器控件
        结构控件
        滚动控件
        辅助控件
        其他控件

5.PyQt5类的继承结构
QObject
    QWidget
        各个控件的子类
            还可以具体控件的类

说明
    PyQt5有很多类，每个类实现具体的功能，比如网络，线程，界面等
    这个教程学习的是界面，主要学习的类就是Widget，主要实现的是界面的功能

"""

# from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

# 查看QObject的直接子类
# print(QObject.__subclasses__())


print(QWidget.__subclasses__())

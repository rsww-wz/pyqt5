from PyQt5.Qt import *
import sys

"""
代码执行方式
方法1
    右击，执行
方法2
    命令行 python 代码名称 参数
    sys.argv可以获取命令行参数
    当通过命令行启动程序时，可以通过设定一种功能，接收命令行传递的参数，来执行不同的功能
    也可以通过：对象.arguments() 获取命令行的参数
    
"""

"""
程序的基本结构分析
    导入需要的包
        app = QApplication(sys.argv)  创建一个应用程序

    控件操作
        创建控件
            w = QWidget()

        设置控件（大小，位置，样式，事件，信号处理……）
        控件也可以作为一个容器，承载其他控件
            w.setWindowTitle("我的第一个PyQt5程序")
            w.resize(400,200)
            w.move(300, 300)

        展示控件
            w.show()

        一个没有父对象的空间默认不显示，必须要调用show()才可以显示
        一个应用程序中可以显示多个顶级控件
            如果一个Widget没有父控件，则认定为是顶级控件（顶级窗口）
            如果想要一个空间展示另外一个控件内部，必须要有父子关系
            如果两个对象为父子关系，那么福对象显示之后，一般子对象会自动显示

    sys.exit(app.exec_())
    开始执行程序，并进入信息循环
    让整个程序一直执行(无限循环)，否则会运行一遍就退出
    检测整个程序所接受到的用户的交互信息（检测鼠标键盘）
    app.exec_()的返回值是程序结束的状态码   
"""

app = QApplication(sys.argv)

# 创建一个窗口
w = QWidget()

# 设置窗口的尺寸
w.resize(400, 200)

# 移动窗口
w.move(300, 300)

# 设置窗口标题
w.setWindowTitle("我的第一个PyQt5程序")

# 创建文本
label = QLabel(w)

# 创建文本
label.setText("hello world")

# 设置文本位置
label.move(150, 100)

# 显示窗口
w.show()

# 进入程序的主循环，并通过exit函数确保主循环安全退出
sys.exit(app.exec_())

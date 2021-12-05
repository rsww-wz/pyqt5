"""
API
    addAction(QAction,QLineEdit.ActionPosition)
        QLineEdit.LeadingPosition:放前面
        QLineEdit.TrailingPosition:放后面

    addAction(QIcon,QLineEditActionPosition)  返回QAction
应用场景
    为文本框添加附加的行为操作

案例
    手动控制明文和密文切换按钮

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("添加行为")
w.resize(500,500)

def addaction():
    le1 = QLineEdit(w)
    le1.move(200,200)
    le1.setClearButtonEnabled(True)
    le1.setPlaceholderText('请输入密码')


    address = r"C:\Users\RONG\Pictures\Camera Roll\地图2.jpg"
    # 创建图标
    icon = QIcon(address)

    # 创建行为
    action = QAction(le1)

    # 添加图标
    action.setIcon(icon)

    #监听icon

    # 方式1
    def cao1():
        if le1.echoMode() == 0:
            le1.setEchoMode(2)
            return None

        if le1.echoMode() == 2:
            le1.setEchoMode(0)
            return None

    # 方式2
    def cao2():
        if le1.echoMode() == 0:
            le1.setEchoMode(2)
        else:
            le1.setEchoMode(0)


    action.triggered.connect(cao2)

    # 添加行为,设置位置
    le1.addAction(action,QLineEdit.TrailingPosition)


addaction()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())


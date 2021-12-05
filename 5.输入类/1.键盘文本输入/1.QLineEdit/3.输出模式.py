"""
API
    setEchoMode(QLineEdit.EchoMode)
        NoEcho = 1:不输出
        Normal = 0:正常输出
        Password = 2:密文形式
        PasswordEchoOnEdit = 3:编辑时明文，结束时秘密

        输入数字或者具体枚举名都是可以的,但是返回值都是数字

    echoMode()
        QLineEdit.EchoMode:获取输出模式

应用场景
    设置输出模式，来适用不同的应用场景
        明文，密文，不输出

案例
    创建一个窗口，添加两个文本框和一个按钮
        一个用作账号，一个用作账号，
        点击登录，获取账号和密码信息
        进行比对账号密码信息
            如果账号错误：清空账号框
            如果秘密错误：清空密码框
            正确：正常显示
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("输出模式")
w.resize(500,500)

# 输出模式
def echomode():
    le = QLineEdit(w)
    le.move(200,200)
    le.setText('12345678')

    le1 = QLineEdit(w)

    # 设置输出模式

    # NoEcho = 1:不输出
    # le.setEchoMode(1)
    # le.setEchoMode(QLineEdit.NoEcho)

    # Normal = 0:正常输出
    # le.setEchoMode(0)
    le.setEchoMode(QLineEdit.Normal)

    # Password = 2:密文形式
    # le.setEchoMode(2)
    # le.setEchoMode(QLineEdit.Password)

    # PasswordEchoOnedit = 3:编辑时明文，结束时密文
    # le.setEchoMode(3)
    # le.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    # 获取输出模式
    print(le.echoMode())

# 案例
def example():
    le1 = QLineEdit(w)
    le1.move(200,200)

    le2 = QLineEdit(w)
    le2.move(200, 250)

    btn = QPushButton('登录',w)
    btn.move(200, 300)

    le2.setEchoMode(0)

    # 写法1
    def cao1():
        account = le1.text()
        password = le2.text()
        if account == 'rs':
            if password == 'love':
                print('登录成功')
            else:
                print('密码错误')
                le2.setText('')
                le2.setFocus()
        else:
            le2.setText('')
            le1.setText('')
            le1.setFocus()

    # 写法2
    def cao2():
        account = le1.text()
        password = le2.text()
        if account != 'rs':
            le2.setText('')
            le1.setText('')
            le1.setFocus()
            return None

        if password != 'love':
            print('密码错误')
            le2.setText('')
            le2.setFocus()
            return None

        print('登录成功')

    btn.clicked.connect(cao2)

# echomode()
example()


# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

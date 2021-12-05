"""
API
    setCompleter(QCompleter):设置完成器
    complete()  返回值：Qcomplete

    操作逻辑和QIcon一样

应用场景
    根据用户输入的字符串，快速联想补全

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("自动补全")
w.resize(500,500)

def autoTip():
    le = QLineEdit(w)
    le.move(200,200)
    le.setPlaceholderText('请输入用户名')
    le.setClearButtonEnabled(True)

    # 设置自动补全
    Tip = ['唐三藏','孙悟空','猪八戒','沙和尚','白龙马']
    le.setCompleter(QCompleter(Tip))

autoTip()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

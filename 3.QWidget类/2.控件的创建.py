"""
API
    parent：父控件
    flags：标志位

应用场景
    创建控件的时候，设置父控件，以及标志位


"""

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(500,500)

red = QWidget(window)
red.setStyleSheet('background:red')
red.move(100,100)

green = QWidget(window)
green.setStyleSheet('background:green')
green.move(100,200)

btn = QPushButton(window)
btn.setText('点击确定')
btn.move(100,300)

window.show()

sys.exit(app.exec_())


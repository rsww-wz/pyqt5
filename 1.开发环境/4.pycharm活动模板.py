"""
活动模板
    把一段代码作为python程序的模板
    敲入特定的字符可以调用模板
激活字符串：GUI
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("")
w.resize(500, 500)

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

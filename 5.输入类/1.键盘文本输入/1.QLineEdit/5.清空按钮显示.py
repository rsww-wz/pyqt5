"""
API
    setClearButtonEnabled(bool)
    isClearButtonEnable()  返回bool

应用场景
    用作快速清空文本框内容

效果
    输入文本之后，在最右边会显示一个叉
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("清空按钮显示")
w.resize(500, 500)


def clearButton():
    le1 = QLineEdit(w)
    le1.move(200, 200)

    # 设置快速清空
    le1.setClearButtonEnabled(True)

    # 查看是否设置快速清空
    print(le1.isClearButtonEnabled())


clearButton()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

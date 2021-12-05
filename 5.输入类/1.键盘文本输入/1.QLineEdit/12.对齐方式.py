"""
API
    setAlignment(Qt.Alignment)
        Qt.Alignment
            水平
                Qt.AlignLeft
                Qt.AlignRight
                Qt.AlignHCenter
                Qt.AlignJustify

            垂直
                Qt.AlignTop
                Qt.AlignBottom
                Qt.AlignVCenter
                Qt.AlignBaseline

            Qt.AlignCenter
                垂直和水平都居中

    注意：水平和垂直都是相互组合的，使用管道符可以组合多个属性参数
        还可以配合设置边距使用

    alignment()
        返回对齐方式
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("对齐方式")
w.resize(500,500)

le = QLineEdit(w)
le.move(200,200)
le.resize(100,100)
le.setPlaceholderText('请输入文本')
# le.setClearButtonEnabled(True)
le.setTextMargins(0,0,20,20)

def set_alignment():
    # 水平居左
    # le.setAlignment(Qt.AlignLeft)

    # 水平居中
    # le.setAlignment(Qt.AlignHCenter)

    # 自动调整（左对齐）
    # le.setAlignment(Qt.AlignJustify)

    # 顶部
    # le.setAlignment(Qt.AlignTop)

    # 底部
    # le.setAlignment(Qt.AlignBottom)

    # le.setAlignment(Qt.AlignVCenter)

    # le.setAlignment(Qt.AlignBaseline)

    # 水平垂直都居中
    # le.setAlignment(Qt.AlignCenter)

    # 多参数
    le.setAlignment(Qt.AlignRight | Qt.AlignBottom)

    # 返回对齐方式
    print(le.alignment())

set_alignment()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

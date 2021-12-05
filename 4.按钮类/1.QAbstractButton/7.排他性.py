"""
排他性理解
    如果存在多个按钮，并且所有按钮都设置排他性，那么在同一时刻，只能有一个按钮被选中
    只有设置排他性的按钮才会有排他性

API
    autoExclusive()
        是否自动排他
        一般按钮都是False，只有单选按钮是True
    setAutoExclusive(bool)
        设置自动排他性

应用场景
    设定按钮组中的按钮，单选特性
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("排他性")
w.resize(500,500)

btn1 = QCheckBox(w)
btn1.move(200,150)
btn1.setText('确定')

btn2 = QCheckBox(w)
btn2.move(200,200)
btn2.setText('确定')

btn3 = QCheckBox(w)
btn3.move(200,250)
btn3.setText('确定')

# 根据按钮的特性自动设置排他性，一般QCheckBox可以多选，QRadioButton是单选
def setautoexclusive():
    btn1.autoExclusive()
    btn2.autoExclusive()
    btn3.autoExclusive()


# 设置排他性,排他性为True，否则为false
def setexclusive():
    btn1.setAutoExclusive(True)
    btn2.setAutoExclusive(True)
    btn3.setAutoExclusive(True)

# setautoexclusive()
setexclusive()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

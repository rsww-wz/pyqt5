"""
描述
    一般用于给用户提供若干选项中的多选操作
    左侧会尊一个方框图标，表示用户的选中状态
继承：QAbstractButton
功能作用
    常用继承父类操作
        图标
        快捷键
    设置是否三态
        setTristate(bool)
        isTristate()
    设置复选框状态
        setCheckState()
            Qt.Unchecked:选中
            Qt.PartiallyChecked:中间态
            Qt.Checked:未选中
        checkState()
            0:选中
            1：中间态
            2：未选中
信号
    stateChanged(int state)
        选中或清除选中时，发射此信号
    其他都继承
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("多选框")
w.resize(500,500)

# 创建按钮
btn1 = QCheckBox('辣椒',w)
btn1.move(400,100)

btn2 = QCheckBox('蒜头',w)
btn2.move(400,120)

btn3 = QCheckBox('小葱',w)
btn3.move(400,140)

btn4 = QCheckBox('姜块',w)
btn4.move(400,160)

btn5 = QCheckBox('加肉',w)
btn5.move(400,180)

# 设置三态
# 除了选中和未选中还有第三种状态
# 第一个点击是标记的意思，第二次点击是选中
btn5.setTristate(True)

#查看是否是三态
print(btn5.isTristate())

# 设置复选框的状态
# 选中
btn1.setCheckState(Qt.Unchecked)
# 中间态
btn2.setCheckState(Qt.PartiallyChecked)
# 未选中
btn3.setCheckState(Qt.Checked)

# 查看状态
print(btn1.checkState())
print(btn2.checkState())
print(btn3.checkState())

# 状态发生改变信号
# 两态
btn4.toggled.connect(lambda isChanged:print(isChanged))
# 三态
btn5.stateChanged.connect(lambda state:print(state))

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

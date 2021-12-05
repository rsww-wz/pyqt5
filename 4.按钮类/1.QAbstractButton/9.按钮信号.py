"""
pressed()：鼠标按下信号

released():鼠标释放信号
    控件内松开鼠标
    鼠标移出控件范围后

clicked(checked = false)
    控件内按下 + 控件内释放

toggled(bool checked)
    切换信号(一般在单选框或者复选框中使用)

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("按钮信号")
w.resize(500,500)

btn = QPushButton(w)
btn.move(200,200)
btn.setText('确定')

# 按下就会执行
btn.pressed.connect(lambda :print('按钮被点击了'))

# 释放就会执行
btn.released.connect(lambda :print('按钮被释放了'))

# 完成按下和释放就会执行
btn.clicked.connect(lambda :print('按钮被点击和释放了'))

# 按钮要是可选的才能被反选
btn.setCheckable(True)
btn.toggled.connect(lambda :print('按钮选中状态发生了改变'))

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

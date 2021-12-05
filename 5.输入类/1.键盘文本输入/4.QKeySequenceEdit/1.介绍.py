"""
描述
    控件允许输入QKeySequence，它通常用采集作快捷方法
    当控件收到焦点时，开始录制，并在用户释放最后一个关键字后一秒结束录制

继承：QWidget
功能作用
    快捷键设置
        setKeySequence(QKeySequence KeySequence)
        keySequence()  -> QKeySequence
    清除
        clear()

信号
    editingFinshed()
    keySequenceChanged(QKeySequence KeySequence)
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("快捷键控件")
w.resize(500,500)

kse = QKeySequenceEdit(w)
kse.move(200,200)


# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

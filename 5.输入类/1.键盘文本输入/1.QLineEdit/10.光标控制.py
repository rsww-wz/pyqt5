"""
API
    cursorBackward(bool mark,int step = 1)
        向左移动steps个字符
        mark:True -- 带选中效果
        mark:False -- 不带选中效果

    cursorForward(bool mark,int step = 1)
        向前移动steps个字符

    cursorWordBackward(bool mark)
        向后移动一个单词长度

    cursorWordForward(bool mark)
        向前移动一个单词长度

    home(bool)
        移动到首行
        True：带选中
        False: 不带选中

    end(bool)

    setCursorPosition(int)
        设置光标位置

    cursorPosition
        获取光标位置

    cursorPositionAt(constQPoint & pos)
        获取指定坐标位置对应文本光标位置
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("光标位置")
w.resize(500,500)

le = QLineEdit(w)
le.move(200,200)
le.setPlaceholderText('请输入文本')
le.setClearButtonEnabled(True)

def cursor_cap():
    btn1 = QPushButton('光标向后移动', w)
    btn1.move(150, 250)
    btn2 = QPushButton('光标向前移动', w)
    btn2.move(300, 250)

    def cao1():
        # 不带选中效果
        le.cursorBackward(False,1)
        le.setFocus()

    def cao2():
        # 带选中效果
        le.cursorForward(True,1)
        le.setFocus()

    btn1.clicked.connect(cao1)
    btn2.clicked.connect(cao2)

def cursor_word():
    btn1 = QPushButton('光标向后移动一个单词', w)
    btn1.move(200, 250)
    btn2 = QPushButton('光标向前移动一个单词', w)
    btn2.move(200, 300)

    def cao1():
        le.cursorWordBackward(False)
        le.setFocus()

    def cao2():
        le.cursorWordForward(False)
        le.setFocus()


    btn1.clicked.connect(cao1)
    btn2.clicked.connect(cao2)

def home_end():
    btn1 = QPushButton('光标移动到开头', w)
    btn1.move(200, 250)
    btn2 = QPushButton('光标移动到结尾', w)
    btn2.move(200, 300)

    def cao1():
        le.home(False)
        le.setFocus()

    def cao2():
        le.end(False)
        le.setFocus()


    btn1.clicked.connect(cao1)
    btn2.clicked.connect(cao2)

def set_corsor_position():
    btn1 = QPushButton('光标移动到中间', w)
    btn1.move(200, 250)

    def cao1():
        # 设置光标位置
        le.setCursorPosition(len(le.text()) / 2)
        le.setFocus()
        # 获取光标位置
        print(le.cursorPosition())

    btn1.clicked.connect(cao1)

# cursor_back()
# cursor_word()
# home_end()
set_corsor_position()


# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

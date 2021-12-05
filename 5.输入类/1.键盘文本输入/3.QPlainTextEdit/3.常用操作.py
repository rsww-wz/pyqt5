"""
块
    blockCount()  -> int 当前块个数
    maximumBlockCount() -> int  最大块个数
    setMaximumBlockCount(int) 设置最大块个数

常用编辑操作
    selectAll():选中所有
    copy()
    cut()
    paste()
    clear()
    redo()
    undo()
    find(str,QTextDocument.FindFlags)
        QTextDoucment.FindBackward:向后搜索
        QTextDoucment.FindCaseSensitively
            默认情况下，查找工作区不分大小写
            指定此选项会将行为更改区分大小写查找
        QTextDoucment.FindWholeWords:查找匹配仅完整的单词
    zoomIn(int range = 1)
        range > 0 :放大
        range < 0 :缩小
    zoomOut()
        range > 0 :缩小
        range < 0 :放大

滚动
    centerCursor()
        控制光标，尽可能保证光标在文本框中间

    ensureCursorVisible()
        滚动控件保证光标可见
        setCenterOnScroll(bool)
            True:控制光标显示时能够展示在中间
        centerOnScroll()   -> bool

光标
    textCursor  -> QTextCursor  获取光标对象
    cursorForPosition(QPoint)  -> QTextCursor  获取指定位置文本光标对象
    setCursorWidth(int) 设置光标光标宽度
    cursorWidth()  -> int
    cursorRect(QTextCursor) 获取指定光标对象的矩形
    cursorRect()  -> QRect
    moveCursor(QTextCursor.MoveOperation,QTextCursor.MoveMode)
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("块的操作")
w.resize(500,500)

pte = QPlainTextEdit(w)
pte.move(100,120)
pte.setPlaceholderText('请输入文本')

btn = QPushButton('测试',w)
btn.move(180,320)

btn1 = QPushButton('测试1',w)
btn1.move(180,350)

def block():

    def cao():
        # 获取当前块的个数
        print(pte.blockCount())

        # 设置块的最大个数(回车为一个块)
        # 如果超过了这个块的个数，前面的块会消失
        pte.setMaximumBlockCount(10)

        # 获取块个数
        print(pte.blockCount())

    btn.clicked.connect(cao)

# 放大缩小
def zoom():
    def cao1():
        pte.zoomIn()

    def cao2():
        pte.zoomOut()

    btn.clicked.connect(cao1)
    btn1.clicked.connect(cao2)

# 滚动
def scroll():

    def cao():
        # 保持光标在文本中间
        # 如果光标不在屏幕上，可以定位到光标所在位置
        # pte.centerCursor()

        # 让光标移动最短距离，让光标可见
        pte.ensureCursorVisible()

        # 滚动时光标可见
        # pte.setCenterOnScroll(True)

        # 获取焦点
        pte.setFocus()


    btn.clicked.connect(cao)

# block()
# zoom()
scroll()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

"""
API
    setBlockCharFormat(QTextCharFormat)
        设置要格式化的当前块(或选择中包含的所有块)的块char格式
    setBlockFormat(QTextBlockFormat)
        设置当前块的块格式进行格式化
    setCharFormat(QTextCharFormat)
        将光标的当前字符格式设置为给定格式（如果光标有选中文字可用于给选中文字设置效果）
    mergeBlockCharFormat(QTextCharFormat)
        合并当前块的char格式
    mergeBlockFormat(QTextBlockFormat)
        合并当前块的格式
    mergeCharFormat(QTextCharFormat)
        合并当前字符格式

注意
    也是通过光标设置块和块的字符格式
    所以也是需要先获取文本光标对象
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("格式设置合并")
w.resize(500, 500)

te = QTextEdit(w)
te.move(100, 100)

btn = QPushButton('确定', w)
btn.move(200, 300)


# 设置块的char格式
def setBChar():
    # 获取文本光标对象
    tcf = te.textCursor()

    def cao():
        # 创建块char格式对象
        obj = QTextCharFormat()

        # 字体
        obj.setFontFamily('幼圆')

        # 设置尺寸
        obj.setFontPointSize(20)

        # 设置下划线
        obj.setFontUnderline(True)

        tcf.setBlockCharFormat(obj)

        # 获取焦点
        te.setFocus()

    btn.clicked.connect(cao)


# 设置块的格式
def setB():
    # 获取文本光标对象
    tcf = te.textCursor()

    def cao():
        # 创建块格式对象
        obj = QTextBlockFormat()

        # 设置右对齐
        obj.setAlignment(Qt.AlignRight)

        # 设置缩进
        obj.setIndent(1)

        tcf.setBlockFormat(obj)

    btn.clicked.connect(cao)


# 设置光标字符格式（可用于光标选中文字设置效果）
def setsurosorChar():
    def cao():
        tcf = te.textCursor()
        # 创建对象
        obj = QTextCharFormat()

        # 设置当前光标字符格式
        obj.setFontPointSize(20)
        obj.setFontUnderline(True)

        tcf.setCharFormat(obj)

    btn.clicked.connect(cao)


# setBChar()
# setB()
setsurosorChar()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

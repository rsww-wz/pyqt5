"""
普通文本
    setPlainText(str)
        设置内容首先会清空原本的内容，光标会停留在文本之前
    insertPlainText(str)
        在原来文本之前插入新的文本
    toPlianText()  str

HTML
    setHtml(str)
    insertHtml(str)
    toHtml()  会返回HTML文本的基本模板（包括头标签，样式标签）

设置文本（自动判定）
    setText()
    会自动判断是普通文本还是HTML文本

追加文本
    append(str)：可以追加HTML文本
    会自动换行添加内容
清空文本
    clear()
粘贴文本

光标移动
"""


from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("内容设置")
w.resize(500,500)

te = QTextEdit(w)
te.move(120,150)

# 普通文本
def plainText():
    # 设置普通文本
    te.setPlainText('hello world\n')

    # 设置HTML文本
    # 在原来文本之前插入新的文本
    te.insertPlainText('<h1>这是一个HTML的h1标签<h1>')

    # 获取文本
    print(te.toPlainText())

# HTML文本
def HTMLText():
    # 设置HTML文本
    te.setHtml('<h1>这是一个HTML的h1标签<h1>')

    # 插入HTML文本
    te.insertHtml('<h2>this is h2<h2>')

    # 获取HTML文本
    print(te.toHtml())

# 自动判断
def autoinfer():
    # te.setText('hello world')
    te.setText('<h3>hello world<h3>')

# 追加和清空文本
def addandclear():
    te.setText('hello')

    # 追加文本
    te.append('world')

    btn = QPushButton('清空',w)
    btn.move(200,200)

    # 清空文本
    btn.clicked.connect(lambda :te.clear())

# plainText()
# HTMLText()
# autoinfer()
addandclear()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

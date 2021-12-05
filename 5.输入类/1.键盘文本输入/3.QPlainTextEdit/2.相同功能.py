from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("相同功能")
w.resize(500,500)

# 创建纯文本控件
pte = QPlainTextEdit(w)
pte.move(150,150)
pte.resize(150,150)
pte.setStyleSheet('background-color:pink;')

btn = QPushButton('确定',w)
btn.move(200,350)

btn1 = QPushButton('测试',w)
btn1.move(200,400)


# 设置占位文本
pte.setPlaceholderText('只能输入字符文本')

# 设置只读属性
pte.setReadOnly(False)

# 设置字符格式(支持光标选中文本设置格式)
def set_format():

    def cao():
        obj = QTextCharFormat()

        obj.setFontFamily('宋体')
        obj.setFontPointSize(15)
        obj.setFontUnderline(True)
        obj.setUnderlineColor(QColor(20,200,40))

        pte.setCurrentCharFormat(obj)

    btn.clicked.connect(cao)

# 设置换行模式
def set_Wrap():
    # 不设置换行
    pte.setLineWrapMode(QPlainTextEdit.NoWrap)

# 设置覆盖模式
def set_over():
    # 设置成insert模式，但是有编码问题，因为中文是两个字节，英文是一个字节，所以不同的文字一般是不能覆盖的
    # 而且就算是同一种文本，也不能连打，否则不会当成一个文字
    pte.setOverwriteMode(True)

# 设置tab键
def set_tab():
    # 设置tab改变焦点
    # pte.setTabChangesFocus(True)

    # 设置tab缩进距离
    pte.setTabStopWidth(2)

# 设置文本操作
def set_text():
    def cao1():
        # 设置普通文本
        pte.setPlainText('hello world')

    def cao2():
        # 插入普通文本
        pte.insertPlainText('Good morning')

    def cao3():
        # 追加文本
        pte.appendPlainText('Good evening')

    def cao4():
        # 追加HTML文本(不是所有的标签都支持)
        pte.appendHtml("<h1>hello world<h1>")


    btn1.clicked.connect(cao1)
    # btn1.clicked.connect(cao2)
    # btn1.clicked.connect(cao3)
    # btn1.clicked.connect(cao4)


set_format()
set_Wrap()
set_over()
set_tab()
set_text()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())


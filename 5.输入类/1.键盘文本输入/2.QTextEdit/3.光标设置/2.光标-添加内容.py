"""
添加内容
    插入文本
        insertText(str):插入普通文本
        insertText(QString,QText(CharFormat format))
        insertHtml(html_str):插入HTML字符串

    插入图片
        光标对象.insertImage(QTextImageFormat)
        过期，不建议使用
            光标对象.insertImage(QTextImageFormat,QTextFrameFormat.position)
            文本对象.insertImage(name_str)
            光标对象.insertImage(QImage,name_str = None)

    插入句子
        insertFragment(QTextDocumentFragment)
        QTextDocumentFragment里面的方法都是类方法

    插入列表
        insertList(QTextListFormat)
            返回：QTextList对象
            效果：在当前位置插入新块，并使其成为具有给定格式的新创建列表的第一个列表项，返回创建的列表
        insertList(QTextListFormat.Style)
            返回：QTextList
            效果：在当前位置插入一个新块，并使其成为具有给定格式的新创建列表的第一个列表项，返回创建的列表
        createList(QTextListFormat)
            返回：QTextList
            效果：创建并返回具有给定格式的新列表，并是当前段落的光标位于第一个列表项中
        createList(QTextListFormat.Style)
            返回：QTextList
            效果：创建并返回具有给定格式的新列表，并是当前段落的光标位于第一个列表项中

        补充
        QTextListFormat
            setIndent(int)
            setNumberPrefix(str)
            setNumberSuffix(str)

        setStyle(QTextListFormat_Style)
            QTextListFormat.ListDisc:圆
            QTextListFormat.ListCircle:一个空的圆
            QTextListFormat.ListSquare:一个方块
            QTextListFormat.ListDecimal:十进制升序排列
            QTextListFormat.ListLowerAlpha:小写拉丁字符字母列表
            QTextListFormat.ListUpperAlpha:大写拉丁字符字母列表
            QTextListFormat.ListLowerRoman:小写罗马数字
            QTextListFormat.ListUpperRoman:大写罗马数字

    插入表格
        insertTable(int rows,int coloums)
            返回：QTextTable
        insertTable(int rows,int coloums,QTextTableFormat)
            返回：QTextTable

        补充
            QTextTableFormat

    插入文本块
        insertBlock()
            插入一个空的文本块
        insertBlock(QTextBlockFormat)
            插入文本块的同时，设置文本格式
        insertBlock(QTextBlockFormat,QTextCharFormat)
            插入文本块的同时，设置文本块格式和文本字符格式

    插入框架
        insertFrame(QTextFrameFormat)
            返回：QTextFormat

总结
    这些方法都是用光标传入对象
    首先需要用文本框函数获取光标对象
    然后根据插入的内容创建对象
    这些对象里面都有方法可以设置样式
    最后把对象传给光标对象就可以插入了

    插入的都是对象
    对象里面有方法可以设置插入对象的格式，样式等。

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("添加内容")
w.resize(500,500)

# 新建文本框
te = QTextEdit(w)
te.move(100,100)

# 新建按钮
btn = QPushButton('插入文本',w)
btn.move(180,300)

# 插入文本
def insertT():

    def cao():
        # 获取光标对象
        tc = te.textCursor()

        # 插入普通文本
        # tc.insertText("hello world")

        # 插入HTML文本
        tc.insertHtml('<h1>hello world<h1>')

    def cao1():
        tc = te.textCursor()

        # 获取字符格式对象
        tcf = QTextCharFormat()

        # 设置字符格式 -- 设置斜体
        tcf.setFontItalic(True)

        # 设置字体大小
        tcf.setFontPointSize(20)

        # 把格式传入对象
        tc.insertText('hello world',tcf)

    # btn.clicked.connect(cao)
    btn.clicked.connect(cao1)

# 插入图片
def insetPicture():
    # 图片必须用对象接收，然后把这个对象传进去
    # 即：insertImage(图片对象)

    def cao():
        # 创建光标对象
        tcf = te.textCursor()

        address = r"C:\Users\RONG\Pictures\Camera Roll\地图1.jpg"
        # 创建图片对象
        picture_obj = QTextImageFormat()

        # 插入图片地址
        picture_obj.setName(address)
        # 设置图片大小
        picture_obj.setWidth(100)
        picture_obj.setHeight(100)

        # 接收对象
        tcf.insertImage(picture_obj)

    def cao1():
        # 创建光标对象
        tcf = te.textCursor()

        address = r"C:\Users\RONG\Pictures\Camera Roll\地图1.jpg"
        # 创建图片对象
        picture_obj = QTextImageFormat()
        # 插入图片地址
        picture_obj.setName(address)
        # 设置图片大小
        picture_obj.setWidth(100)
        picture_obj.setHeight(100)

        # 接收对象,并设置插图图片位置
        tcf.insertImage(picture_obj,QTextFrameFormat.FloatRight)

    # btn.clicked.connect(cao)
    btn.clicked.connect(cao1)

# 插入片段
def insertFragment():
    # 句子也是一个对象，设置好格式，把对象传进光标对象即可

    def cao():
        # 创建光标对象
        tcf = te.textCursor()

        # QTextDocumentFragment都是类方法

        # 插入普通文本片段
        # sentence_obj = QTextDocumentFragment.fromPlainText('hello world')

        # 插入HTML片段
        sentence_obj = QTextDocumentFragment.fromHtml("<h1>hello<h1><br><p>world<p>")

        # 传入对象
        tcf.insertFragment(sentence_obj)

    btn.clicked.connect(cao)

# 插入列表
def insert_List():
    # 创建光标对象
    tcf = te.textCursor()

    def cao():
        # 使用类型枚举对象
        # 创建列表和样式
        tcf.insertList(QTextListFormat.ListDisc)
        # tcf.insertList(QTextListFormat.ListCircle)
        # tcf.insertList(QTextListFormat.ListSquare)
        # tcf.insertList(QTextListFormat.ListDecimal)
        # tcf.insertList(QTextListFormat.ListLowerAlpha)
        # tcf.insertList(QTextListFormat.ListLowerRoman)

    def cao1():
        tcf.createList(QTextListFormat.ListCircle)

    def cao2():
        # 创建类型对象
        obj = QTextListFormat()

        # 设置缩进，一个缩进是tab
        obj.setIndent(1)

        # 设置前缀
        obj.setNumberPrefix("*")

        # 设置后缀
        obj.setNumberSuffix("*")

        # 设置样式
        obj.setStyle(QTextListFormat.ListDecimal)

        # 传样式
        tcf.insertList(obj)

    # btn.clicked.connect(cao)
    # btn.clicked.connect(cao1)
    btn.clicked.connect(cao2)

# 插入表格
def insert_table():
    # 创建光标对象
    tcf = te.textCursor()

    def cao():
        # 插入三行三列的表格
        tcf.insertTable(3,3)

    def cao1():
        # 创建表格样式对象
        obj = QTextTableFormat()

        # 设置表格样式 -- 插入表格位置
        obj.setAlignment(Qt.AlignLeft)

        # 设置表格空格大小
        obj.setCellPadding(8)

        # 设置表格表框
        obj.setCellSpacing(1)

        tcf.insertTable(5,5,obj)


    # btn.clicked.connect(cao)
    btn.clicked.connect(cao1)

# 插入文本块
def insert_block():
    # 创建光标对象
    tcf = te.textCursor()

    def cao():
        # 插入文本块
        tcf.insertBlock()

        # 获取焦点
        te.setFocus()

    def cao1():
        # 创建文本块对象
        obj = QTextBlockFormat()

        # 设置文本块格式 -- 边距
        obj.setLeftMargin(10)
        obj.setRightMargin(10)
        obj.setTopMargin(10)
        obj.setBottomMargin(10)

        # 获取焦点
        te.setFocus()

        # 还可以添加字体样式对象
        tcf.insertBlock(obj)


    # btn.clicked.connect(cao)
    btn.clicked.connect(cao1)

# 插入文本框架
def insert_frame():
    # 创建光标对象
    tcf = te.textCursor()

    def cao():
        # 创建框架对象
        obj = QTextFrameFormat()

        # 设置框架样式 -- 边框
        obj.setBorder(10)

        # 颜色对象：RGB
        obj.setBorderBrush(QColor(100,50,50))

        tcf.insertFrame(obj)

    btn.clicked.connect(cao)


# insertT()
# insetPicture()
# insertFragment()
# insert_List()
# insert_table()
# insert_block()
insert_frame()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

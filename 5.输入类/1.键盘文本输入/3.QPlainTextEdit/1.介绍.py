"""
描述
    大致功能实现和QTextEdit差不多
        适用于段落字符
            段落是一个格式化的字符串，为了适应控制的穿度，会自动换行
            默认情况下，在读取纯文本时，一个换行符表示一个段落
            文档混杂零个或者多个段落组成，段落有硬线断开分割
        内容的编辑
            文本的选择有QTextCursor类处理，该类提供创建选择，检索文本内容或者删除选择的功能
            QPlianTextEdit包含一个QTextDocument对象，可以使用document()方法检索对象
    与QTextEdit的差异
        QPlianTextEidt是QTextEdit简略版本的类
            使用QTextEdit和QTextDocument作为背后实现的技术支持
        它的性能优于QTextEdit，主要是因为在文本文档中使用QPlainTextDocument.ayout简化文本布局
        纯文本文档布局不支持或嵌入框架，并使用逐行滚动方法替换像素精确高度计算

    理解
        性能比QTextEdit好
        QTextEdit是按像素处理的，速度比较慢，滚动的时候可以显示不完整的行
        QPlianTextEdit是按行处理的，滚动时只能显示完整的一行，性能比较高

        QTextEdit：是富文本编辑器
        QPlianTextEidt：是纯文本编辑器
        
继承：QAbstractSrcollArea

"""
from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("纯文本文本框")
w.resize(500,500)

pte = QPlainTextEdit(w)
pte.move(100,150)
pte.setStyleSheet('background-color:red')


# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

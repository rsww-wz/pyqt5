"""
QTextEdit
    描述
        是一个高级的文本编辑器，支持使用HTML样式标签的富文本格式
        它经过优化，可以处理大型文档并快速响应用户输入
        适用于段落和字符
        文本编辑可以加载纯文本和富文本文件

    继承：QAbstractScrollArea

"""

# 占位提示文本
"""
setPlaceholderText(str)
placehodeText()   str

文本框内容为空时，给用户的文本提示信息
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("占位文本")
w.resize(500,500)

te = QTextEdit(w)
te.move(200,200)
te.resize(200,200)

# 设置占位文本
te.setPlaceholderText('请输入文本')

# 获取占位文本
print(te.placeholderText())


# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

"""
输入类控件
    纯键盘文本输入
        QLineEdit
        QTextEdit
        QPlanTextEdit
        QKeySequenceEdit
    步长调整
        QAbstractSpinBox
    组合框
    滑块
    橡皮筋选中
    对话框
    日期


QLineEdit
    描述
        是一个单行文本编辑器
        允许用户输入和编辑单行纯文本
        自带一组编辑功能
            撤销，重做，剪切，粘贴，拖放
    继承：QWidget
    功能
        文本的设置和获取
        输出模式
        占位提示字符串
        清空按钮显示
        添加操作行为
        自动补全
        输入限制
        是否被编辑
        光标控制
        文本边距设置
        常用编辑功能
        对齐方式
    应用场景
        通过代码来控制输入文本内容
    信号

"""
from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("文本框")
w.resize(500,500)

# 创建文本框
textbox = QLineEdit(w)
textbox.move(200,200)

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

"""
QAbstractSpinBox是所有步长调节器的父类，是一个抽象的父类

描述：由一个步长调节器和单行文本框来调节和显示数据
继承：QWidget

功能作用
    使用
        1. 子类化此类
        2. 实现控制上下能用的方法
            stepEnable -> QAbstractSpinBox.StepEnable
                QAbstractSpinBox.StepNone: 都不能用
                QAbstractSpinBox.StepUpEnable: 上可用
                QAbstractSpinBox.StepDownEnable: 下可用
        3. 现实步长调整方法
            stepBy(p_int)

    长按调整步长加快频率
        setAccelerated(bool)
        isAccelerated() -> bool
        控制用户长按加减按钮后，内容调整频率

    只读
        setReadOnly(bool)
        isReadOnly  -> bool
        只允许用户通过步长调节器调节，不能使用键盘输入

    设置以及获取内容
        text() -> str
        lineEdit() -> QLineEdit()
            返回的单行文本编辑器可以设置内容和格式
        设置文本框内的文本内容，获取最终结果数据

    对齐方式
        setAlignment(Qt.Alignment)
        alignment() -> Qt.Alignment
        设置文本框中文的对齐方式（也可以用QLineEdit设置）

    设置周边框架
        setFrame(bool) 默认True
        hasFrame -> bool
        设置控件周边是否有框架，如果有，会有个边框显示

    清空文本框内容
        clear()

    内容验证
        重写两个方法
            validate(p_str,p_int)  验证规则
            fixup(self,p_str) 修复方法
        通过规则，验证用户输入的内容是否正确

    总结
        如果是设置步长调节的，需要实例化抽象类，然后单独设置调节模式
        如果是设置文本框的，可以先获取文本框对象，然后使用文本框对象设置，最后使用一个函数把文本框对齐传进来即可
        抽象类也有常见的设置，可以直接使用

信号
    继承父类
    editingFinished() : 结束编辑时使用
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("步长调节你器")
w.resize(500,500)

sb = QAbstractSpinBox(w)
sb.resize(100,30)
sb.move(200,200)


# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

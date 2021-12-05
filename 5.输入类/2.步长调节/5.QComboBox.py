"""
描述
    是一个组合控件，默认展示最小空间给用户操作
    可通过下拉选择界面，选区更多的预置选项
继承：QWidget
功能作用
    数据操作
        添加条目项
            addItme(str)
            addItem(QIcon)
            addItems(Iterable[str])
        插入项目符
            insertItem(int,str)
            insertItme(int,QIcon,str)
            insertItems(int,Iterable[str])
        设置条目项
            setItemIcon(int,QIcon)
            setItemText(int,str)
            setItemData(int)
        删除条目项
            removeItem(int,index)
        插分割线
            insertSeparator(int index)
        设置当前编辑文本
            setCurrentIndex(int index)
            setCurrentText(QString text)
            setEditText(QString text)

    常用数据获取
    数据限制
    常规操作
信号
案例
相关子类

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("组合框")
w.resize(500,500)

cb = QComboBox(w)
cb.move(200,200)

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

"""
QAbstractScrollArea
    描述：是滚动区域的低级抽象
    继承：QFrame
    功能作用
        设置水平和垂直滚动条(基本不用)
            设置水平和垂直滚动条
                setHorizontalScrollBar(QScrollBar * scrollBar)
                setVericalScrollBar(QScrollBar * scrollBar)
            获取水平和垂直滚动条
                horizontalScrollBar() QScrollBar
                verticalScrollBar()   QScrollBar

        滚动条策略
            setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy)
            setVerticalScrollBarPolicy(Qt.ScrollBarPolicy)
                Qt.ScrollBarAsNeeded:默认值
                Qt.ScrollBarAlwaysoff:不显示滚动条
                Qt.ScrollBarAlwaysOn:一直显示滚动条，具有瞬态滚动条的习俗会忽略此属性

            horizonScrollBarPolicy() QScrooBar
            verticalcrollBarPolicy() QScrooBar

        角落控件
            setCornerWidget(QWidget * widget)
            cornerWidget()  QWidget

    信号：继承父类
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("滚动条")
w.resize(500,500)

te = QTextEdit(w)
te.move(200,200)
te.resize(100,100)

# 打开水平滚动条
te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

# 关闭垂直滚动条
te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

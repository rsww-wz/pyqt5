"""
QFrame
    描述
        是一个基类，可以选择直接使用
        主要是用来控制一些边框样式
            凸起，下凹，引用，线宽

    继承：QWidget
    信号:继承父类

"""
# 框架形状
"""
setFrameShape(QFrame.Shape)
    QFrame.NoFrame:什么都没有画
    QFrame.Box:绘制一个框
    QFrame.Panel：绘制一个面板，使得内容凸起或者凹陷
    QFrame.HLine：绘制一个没有框架的水平线
    QFrame.VLine：绘制一条没有框架的垂直线
    QFrame.StyledPanel：绘制一个矩形面板，其外观取决于当前GUI样式
    QFrame.WinPanel:(几乎不用)
        绘制一个可以像Windows 2000中那样凸起或者凹陷的
        指定此形状可将线宽设置为2像素
        对于GUI样式独立性，建议使用StylePanel
frameShape()
    获取框架形状返回值
"""

# 框架阴影
"""
setFrameShadow(QFrame.Shadow)
    QFrame.Plain：框架和内容周围呈现水平
    QFrame.Raised：框架和内容出现；使用当前颜色组的浅色和深色绘制3D凸起线
    QFrame.Sunken：框架和内容下凹；使用当前颜色组的浅色和深色绘制3D凹起线
FrameShadow()
    获取框架阴影
"""

# 框架线宽
"""

外线宽度
    setLineWidth(int width)
    lineWidth()
中线宽度
    setMidLineWidth()
    midLineWidth()
获取总线宽
    frameWidth()
应用场景：通过控制线宽，来达到不同的组合效果
"""

# 框架样式和框架矩形
"""
框架样式
    setFrameStyle(int style)
        形状和阴影的组合
    frameStyle

框架矩形
    setFrameRect(QRect)
    frameRect()
"""


from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("QFrame")
w.resize(500,500)

frame = QFrame(w)
frame.move(200,200)
frame.resize(100,100)
frame.setStyleSheet('background-color:cyan;')

# 外框形状
def set_frame():
    frame.setFrameShape(QFrame.Box)
    # frame.setFrameShape(QFrame.Panel)
    # frame.setFrameShape(QFrame.HLine)
    # frame.setFrameShape(QFrame.VLine)
    # frame.setFrameShape(QFrame.StyledPanel)

# 设置阴影
def set_Shadow():
    # frame.setFrameShadow(QFrame.Plain)
    # frame.setFrameShadow(QFrame.Raised)
    frame.setFrameShadow(QFrame.Sunken)

# 设置线宽
def set_LineWidth():
    # 外线宽
    # frame.setLineWidth(10)

    # 中线宽
    frame.setMidLineWidth(10)

    # 获取总线宽
    print(frame.frameWidth())

# 框架样式
def set_styleSheet():
    # 样式是预设的形状和阴影的组合
    frame.setFrameStyle(5)

    # 获取框架样式
    print(frame.frameStyle())

# 框架形状
def set_shape():
    # 设置形状
    frame.setFrameRect(QRect(20,20,20,20))

    # 获取形状
    print(frame.frameRect())

set_frame()
set_Shadow()
set_LineWidth()
set_styleSheet()
set_shape()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

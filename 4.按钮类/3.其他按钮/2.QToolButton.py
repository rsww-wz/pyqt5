"""
描述
    提供了一个快速访问按钮
    通常是在工具栏内部使用
    工具按钮通常不显示文本标签，而是现实图标

理解
    只显示图标，不显示文字的工具栏按钮
    如果同时有文本和图标只显示图标

继承：QAbstractButton

功能
    创建按钮
    设置文本，图标，工具提示
        setText(str)
        setIcon(QIcon)
        setIconsize(QSize)
        setToolTip(str)

    按钮格式
        setToolButtonStyle()
            Qt.ToolButtonIconOnly:仅显示图标
            Qt.ToolButtonTextBesideIcon:文本显示在图标旁边
            Qt.ToolButtonTextUnderIcon:文本显示在图标下方
            Qt.ToolButtonFollowStyle:遵循风格
        toolButtonStyle()
            获取图标风格

    设置箭头
        把按钮变成一个具备特殊箭头的图标工具
        setArrowType()
            Qt.NoArrow:无箭头
            Qt.UpArrow:向上箭头
            Qt.DownArrow:向下箭头
            Qt.LeftArrow:向左箭头
            Qt.RightArrow:向右箭头
        arrowType()
            获取箭头信息

    自动提升
        setAutoRaise(bool)
        atuoRaise()

        在自动提升模式下，该按钮仅在鼠标指向时才绘制3D帧
        在工具栏（QToolBar）中，默认就是自动提升
        其实可以理解为就是设置扁平化
    菜单
        setMenu(QMenu)
            通过菜单展示更多选项
        menu()

    菜单弹出模式：设置菜单弹出的触发模式
        setPopupMode(QToolButton.ToolButtonPopupMode)
            QToolButton.DelayedPopup
                鼠标按住一会才显示
                类似于浏览器后退按钮
            QToolButton.MenuButtonPopup
                有一个专门的指示箭头
                点击箭头才会显示
            QToolButton.InstantPopup
                点了按钮就显示
                点击信号不会发射

        popupMode()
            获取菜单弹出模式

信号
    trggered(QAction)
        当点击某个action时触发，并会将action传递进来
        技巧：QAction对象可以通过
            setData(任何类型的数据):绑定数据
            data：获取数据
    其他信号都是继承的

练习
    自己做一个菜单栏
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("QToolButton")
w.resize(500,500)

# 创建按钮
btn = QToolButton(w)
btn.move(200,200)

# 设置图标
address = r"C:\Users\RONG\Pictures\Camera Roll\地图2.jpg"
Icon = QIcon(address)
btn.setIcon(Icon)

# 设置提示信息
btn.setToolTip('这是一个图标按钮')

# 设置文本
btn.setText('hello world')

# 设置按钮风格
btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

# 获取图标风格
print(btn.toolButtonStyle())

# 设置箭头风格
btn.setArrowType(Qt.DownArrow)

# 获取箭头风格信息
print(btn.arrowType())

# 设置扁平化,鼠标经过也会显示3D效果
btn.setAutoRaise(True)

# 获取是否设置扁平化
print(btn.autoRaise())

# 只有箭头的按钮
def onlyarrow():
    btn1 = QToolButton(w)
    btn1.setArrowType(Qt.RightArrow)

onlyarrow()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

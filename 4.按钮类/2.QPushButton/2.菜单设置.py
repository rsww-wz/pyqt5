"""
API
    setMenu(QMenu):设置菜单
    menu():获取菜单
    showMenu：展示菜单

应用场景
    可以设置点击按钮展示下拉菜单

补充（QMenu）
    添加子菜单：addMenu(QMenu)
    添加分割线：addSeparator()
    添加行为动作：addAction(QAction)

    QMenu控件设置
        setTitle(str)
        setIcon(QIcon)

    QAction设置
        setText(str)
        setIcon(QIcon)
        信号：triggered

理解
    Qmenu是设置菜单
    QAction是设置菜单行为
    按钮添加菜单，菜单添加行为，菜单是menu，行为是action
    流程
        创建按钮——设置按钮
        创建菜单——设置菜单
        创建行为——设置行为（行为也可以是打开另一个新的菜单，即二级目录）
"""

from PyQt5.Qt import *
import sys

# 创建程序对象

app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("菜单设置")
w.resize(500, 500)

# 创建按钮
btn = QPushButton('文件', w)

# 创建菜单
menu = QMenu()

# 创建行为
new_file_action = QAction('新建文件', menu)
open_file_action = QAction('打开文件', menu)
exit_file_action = QAction('退出文件', menu)

# 具体行为
new_file_action.triggered.connect(lambda: print('新建文件'))
open_file_action.triggered.connect(lambda: print('打开文件'))
exit_file_action.triggered.connect(lambda: print('退出文件'))

# 菜单添加行为
menu.addAction(new_file_action)
menu.addSeparator()
menu.addAction(open_file_action)
menu.addSeparator()
menu.addAction(exit_file_action)

# 按钮添加菜单
btn.setMenu(menu)

# 展示控件
w.show()

# 自动打开菜单
btn.showMenu()

# 程序循环
sys.exit(app.exec_())

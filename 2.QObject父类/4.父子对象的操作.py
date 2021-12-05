"""
API
    setParent(parent)
        设置父对象
        父对象只能设置一个

    parent()
        获取父对象

    children()
        获取所有直接子对象

    findChild(参数1，参数2，参数3)

    findChildren(参数1，参数2，参数3)

应用场景
    涉及到Qt对象内存管理机制
        QObject继承树
            所有的对象都是直接或者间接的继承自QObject
            QObject在一个对象树中组织它自己
            当创建一个QObject时，如果使用了其他对象作为其父对象，它就会被添加到父对象的children()列表中
            当父对象被销毁时，这个QObject也会被销毁

        QWidget
            当一个空间设置了父子控件
                会包含在父控件内部
                受父控件区域裁剪
                父控件被删除，子控件也会被删除
            场景案例
                一个对话框，上面有很多操作按钮，按钮和对话框本身是父子控件关系
                操作的时候，是操作对话框控件本身，而不是其内部的子控件
                当对话框被删除时，内部的字控件也会自动删除

    如果一个控件没有任何父控件，那么就会被当做顶层控件（窗口）
    如果想要一个控件被包含在另外一个控件内部，就需要设置父子关系
        显示位置会受到父控件的约束
        生命周期也会被父对象接管



"""

# setParent(parent)
# 作用：设置父对象

from PyQt5.Qt import *

obj1 = QObject()
obj2 = QObject()

# 把obj1设置为obj2的父亲
obj2.setParent(obj1)

print('obj1', obj1)
print('obj2', obj2)

# 查看对象的父亲
print(obj2.parent())

"""
练习
obj1
    obj1
        obj3
    obj2
        obj4
        obj5
"""

# 创建对象
obj0 = QObject()
obj1 = QObject()
obj2 = QObject()
obj3 = QObject()
obj4 = QObject()
obj5 = QObject()

# 设置父子关系
# 注意一个对象只能设置一个父对象，如果有两个，会以最后一个设置的为父对象
obj4.setParent(obj2)
obj5.setParent(obj2)

obj3.setParent(obj1)

obj1.setParent(obj0)
obj2.setParent(obj0)
print('*' * 60)

# 检查是否设置正确
print(obj1.parent())
print(obj2.parent())
print(obj3.parent())
print(obj4.parent())
print(obj5.parent())
print('*' * 60)

# 获取所有子对象
# 只能获取直接的子对象
print(obj0.children())
print('*' * 60)

# findChild()
# 作用：获取某一个指定名称和类型的子对象
# 参数1
#   元组类型
#   确定查找子对象的类型

# 参数2：
#   要查找子对象的名称

# 参数3：查找顺序
#   Qt.FindChildrenRecursively:查找默认是递归，即先查找一个对象下面的子对象
#   Qt.FindDirectChildrenOnly:只查找父对象直接的子对象

# findchildren()
# 作用：查找多个子对象

print(obj0.findChildren(QObject))

# 控件父子关系
import sys

app = QApplication(sys.argv)

"""
没有父子关系，都是顶层控件,独立的控件
win1 = QWidget()
win1.setStyleSheet('background-color:red')
win1.show()

win2 = QWidget()
win2.setStyleSheet('background-color:green')
win2.show()
"""

win1 = QWidget()
win1.setStyleSheet('background-color:red')
win1.resize(500, 500)
win1.show()

win2 = QWidget()
win2.setStyleSheet('background-color:green')
win2.resize(400, 400)
# 子控件不能超过父控件的范围
# win2.resize(600,600)

# 设置父子关系
win2.setParent(win1)
win2.show()

sys.exit(app.exec_())

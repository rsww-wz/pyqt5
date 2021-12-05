"""
API
    是否可用
        setEnabled(bool)
            设置控件是否禁用
        isEnabled
            获取控件是否可用
    是否显示/隐藏
        setVisible(boo)
            设置控件是否可见，传递的参数值为True也不一定可见（如果父控件没有被展示）
            马甲
                setHidden(bool)
                show()：展示控件
                hide()：隐藏控件
        isHidden()
            判定控件是否隐藏
            可理解为相对于父控件是否可见
            即如果控件是可以被看见的，自己是否是被隐藏的,如果是可见的是False
        isVisble()
            获取控件最终状态是否可见
            被其他控件遮挡也属于可见
            可见的是False

    是否编辑
        设置窗口标题
        setWindowModified(bool)
            被编辑状态 显示
            没有被编辑 不显示
        isWindowModified
            窗口是否被编辑状态

    是否活跃窗口
    关闭
        close()
        setAttribute(Qt.WA_DeleteOnClose,True)
    注意
应用场景

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("交互状态")
w.resize(500, 500)


def btn():
    btn = QPushButton(w)
    btn.setText('确定')
    btn.pressed.connect(lambda: print('按钮被点击了'))
    btn.destroyed.connect(lambda: print('按钮被释放了'))

    # 关闭控件，只是隐藏了控件，并没有释放控件
    # btn.close()
    # btn.deleteLater()

    # 可以用setAttribute()函数设置，如果设置后使用close函数就会释放控件
    btn.setAttribute(Qt.WA_DeleteOnClose, True)
    btn.close()


def show_():
    btn()

    # 按钮不可用
    # btn.setEnabled(False)         #控件不可用
    # btn.setEnabled(True)          #控件可用
    print(btn.isEnabled())

    # 隐藏显示控件
    # btn.setVisible(True)       #显示控件
    # btn.setVisible((False))    #隐藏控件
    # btn.setHidden(True)        #隐藏控件
    # btn.setHidden(False)       #显示控件

    print(btn.isVisible())
    print(btn.isHidden())


def Title_edit():
    # 只能是中括号里面放*，不能是其他的符号
    # 编辑的时候会显示*，不编辑就不会显示
    w.setWindowTitle("交互状态[*]")
    w.setWindowModified(True)
    # 查看是否被修改
    print(w.isWindowModified())


# window = QWidget()
# window.show()

# show_()
Title_edit()
# 展示控件
w.show()

# # 在最上面的窗口不一定能获得焦点
# window.raise_()
# # 查看窗口是否活跃，即是否获得焦点
# print(window.isActiveWindow())

# 程序循环
sys.exit(app.exec_())

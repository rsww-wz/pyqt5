"""
API
单个控件角度
    setFoucs():指定控件获取焦点
    setFoucusPolicy(Policy)
        设置焦点获取策略
        Policy
            Qt.TabFoucs:只能通过tab键获得焦点
            Qt.ClickFocus:只能通过单击获得焦点
            Qt.StrongFoucs:通过上面两种方式获得焦点
            Qt.NoFocus:不能通过上面两种方式获得焦点
    clearFoucs():取消焦点
父控件角度
    focusWidget():获取子控件中当前聚焦控件
    focusNextChild():聚焦下一个子控件
    focusPreviousChild()：聚焦上一个子控件
    focusNextPreveChild(bool)
        True:下一个
        False：上一个
    setTabOrder(pre_widget,next_next_widget)
        静态方法
        设置子控件获取焦点的先后顺序

应用场景
    登录账号的时候，按tab可以切换焦点


"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("焦点控制")
w.resize(500, 500)


def single_focus():
    edit1 = QLineEdit(w)
    edit1.move(150, 100)

    edit2 = QLineEdit(w)
    edit2.move(150, 200)

    edit3 = QLineEdit(w)
    edit3.move(150, 300)

    # 默认是第一个文本框得到焦点，按tab切换焦点，shift+tab切换上一个焦点
    # 设置焦点
    edit2.setFocus()
    # 设置得到焦点的方式
    edit2.setFocusPolicy(Qt.StrongFocus)

    # 清除焦点
    edit2.clearFocus()


def father_focus():
    edit1 = QLineEdit(w)
    edit1.move(150, 100)

    edit2 = QLineEdit(w)
    edit2.move(150, 200)

    edit3 = QLineEdit(w)
    edit3.move(150, 300)

    # 设置焦点
    edit2.setFocus()
    # 获取当前窗口内部，所有子控件当中获取焦点的那个控件
    # print(w.focusWidget())
    # 获取当前焦点的下一个控件的焦点
    # w.focusNextChild()
    # 获取当前焦点的上一个控件的焦点
    # w.focusPreviousChild()
    # 通过布尔值控制上下控件的焦点;True是下一个；False是上一个
    # w.focusNextPrevChild(True)
    w.focusNextPrevChild(False)

    # 设置控件获得焦点顺序,只能接受两个参数
    w.setTabOrder(edit2, edit1)
    w.setTabOrder(edit1, edit3)


# single_focus()
father_focus()
# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

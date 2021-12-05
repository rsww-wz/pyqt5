"""
API
    设置鼠标形状
    setCursor()
    参数
        Qt.ArrowCursor：正常鼠标指针
        Qt.UpArrowCursor：向上箭头
        Qt.CrossCursor：十字架
        Qt.IBeamCursor：选择文本时候的光标
        Qt.WaitCursor：转圈
        Qt.BusyCursor：鼠标指针和转圈
        Qt.ForbidenCursor：禁止符号
        Qt.PointingHandCursor：手指
        Qt.WhatsThisCursor：鼠标指针和问号
        Qt.SizeVerCursor：上下双箭头（上下拉窗口）
        Qt.SizeHorCursor：左右双箭头（左右拉窗口）
        Qt.SizeBDiagCursor：斜双箭头（拉窗口的角）
        Qt.SizeAllCursor：十字架箭头
        Qt.SplitVCursor:上下分离箭头
        Qt.SplitHCursor：左右分离箭头
        Qt.OpenHandCursor：巴掌
        Qt.ClosedHandCursor：缩小版巴掌
        Qt.BlankCursor：白色指针

    QCursor对象
        自定义鼠标形状

    重置形状
        unsetCorsor()
            重置鼠标对象

    获取鼠标
        cursor()对象里面的方法，一般用不到，有兴趣自己看

    鼠标跟踪
        hasMouseTracking()
            判定是否设置了鼠标跟踪
        setMouseTrackKing(bool)
            设置鼠标是否跟踪
            所谓的鼠标根据就是设置检测鼠标移动事件的条件
            不跟踪
                鼠标移动时，必须处于按下状态，才会触发mouseMoveEvent事件
            跟踪
                鼠标移动时，不处于按下状态，也会触发mouseMoveEvent事件
"""

from PyQt5.Qt import *
import sys


# 重写父类方法
class Window(QWidget):
    def mouseMoveEvent(self, mv):
        print('鼠标移动了', mv.localPos())
        label = self.findChild(QLabel)
        label.move(mv.localPos().x(), mv.localPos().y())


# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = Window()

# 设置控件
w.setWindowTitle("鼠标操作")
w.resize(500, 500)


# 系统鼠标指针
def setMouse():
    w.setCursor(Qt.ArrowCursor)
    # w.setCursor(Qt.UpArrowCursor)
    # w.setCursor(Qt.CrossCursor)
    # w.setCursor(Qt.IBeamCursor)
    # w.setCursor(Qt.WaitCursor)
    # w.setCursor(Qt.BusyCursor)
    # w.setCursor(Qt.ForbiddenCursor)
    # w.setCursor(Qt.PointingHandCursor)
    # w.setCursor(Qt.WhatsThisCursor)
    # w.setCursor(Qt.SizeVerCursor)
    # w.setCursor(Qt.SizeHorCursor)
    # w.setCursor(Qt.SizeBDiagCursor)
    # w.setCursor(Qt.SizeAllCursor)
    # w.setCursor(Qt.SplitVCursor)
    # w.setCursor(Qt.SplitHCursor)
    # w.setCursor(Qt.OpenHandCursor)
    # w.setCursor(Qt.ClosedHandCursor)
    # w.setCursor(Qt.BlankCursor)


# 自定义指针
def MyMouse():
    # 创建图形路径对象
    address = r"C:\Users\RONG\Pictures\Camera Roll\地图2.jpg"
    pixmap = QPixmap(address)

    # 缩放图片大小,通过返回值得到缩放尺寸后的图片
    pixmap = pixmap.scaled(20, 20)

    # 创建自定义形状对象
    # 默认以图片的中心为鼠标指针的位置
    # 可以设置图片中某个位置为鼠标的指针位置位置
    cursor = QCursor(pixmap, 0, 0)

    w.setCursor(cursor)


# 鼠标跟踪
def moveMouse():
    label = QLabel(w)
    label.move(200, 200)
    label.setText('hello world')
    label.setStyleSheet('background-color:cyan;')

    # 设置鼠标跟踪
    # 设置了鼠标根据就是自动触发mouseMoveEvent函数
    w.setMouseTracking(True)


# setMouse()
# MyMouse()
moveMouse()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

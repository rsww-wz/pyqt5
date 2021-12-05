"""
API
    图标
        设置：setWindowIcon(address)
        查看：windowIcon()
    标题
        设置：setWindowTitle(str)
        查看：windowTitle()
    不透明度
        设置：setWindowOpacity(float)（0.0-1.0）
        查看：windowOpacity()
    窗口状态
        设置：setWindowState(state)
            Qt.WindowNoStat：无状态
            Qt.WindowMinimized：最小化
            Qt.WindowMaxmized：最大化
            Qt.WindowFullScreen：全屏(用户区域全屏，不显示标题栏)
            Qt.WindowActive：活动窗口（显示在最前面，活动焦点）
        查看：windowState()
    展示最大化最小化
        控制
            showFullScreen()：全屏
            showMaximized()：最大
            showMinimized()：最小
            showNormal():正常
        判定
            isMaximized()
            isMinimized()
            isFullScreen()
    窗口标志
        window.setWindowFlags(Qt.WindowStaysOnTopHint)
            窗口样式
                Qt.Widget
                Qt.Window
                Qt.Dialog
                Qt.Sheet
                Qt.Drawer
                Qt.Popup
                Qt.Tool
                Qt.ToolTip
                Qt.SplashScreen
                Qt.SubWindow
            顶层窗口外观标志
                Qt.MSWindowsFixedSizeDialogHint:囱口无法调整大小
                Qt.FramelessWindowHint:口无边框
                Qt.CustomizeWindowHint:有边框但无标题栏和按钮，不能移动和拖动
                Qt.WindowTitleHint:添加标题栏和一个关闭按钮
                Qt.WindowSystemMenuHint:添加系统目录和一个关闭按钮
                Qt.WindowaximizeButtonHint:激活最大化和关闭按钮，禁止最小化按钮
                Qt.WindowMinimizeButtonHint:激活最小化和关闭按钮，禁止最大化按钮
                Qt.WindowMinMaxButtonsHint:激活最小化，最大化和关闭按钮
                Qt.WindowCloseButtonHint:添加一个关闭按钮
                Qt.WindowContextHelpButtonHint:添加问号和关闭按钮，同对话框
                Qt.WindowStaysOnTopHint:窗口始终处于顶层位置

应用场景
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.resize(500,500)

def windowIcon():
    # 设置标题并查看
    w.setWindowTitle('顶层窗口')
    print(w.windowTitle())


    # 创建窗口图标对象
    address = r"C:\Users\RONG\Pictures\Camera Roll\地图2.jpg"
    Icon = QIcon(address)
    # 设置窗口图标
    w.setWindowIcon(Icon)
    # 查看图标
    print(w.windowIcon())


    #设置，查看
    w.setWindowOpacity(0.8)
    print(w.windowOpacity())

    #设置，查看窗口状态
    # w.setWindowState(Qt.WindowMaximized)
    # w.setWindowState(Qt.WindowFullScreen)
    w.setWindowState(Qt.WindowActive)
    print(w.windowState())

    # 展示最大化，最小化
    w.showNormal()
    # w.showMaximized()
    # w.showMinimized()
    # w.showFullScreen()

# 无边框无标题栏
def window_example1():
    #可以直接在创建窗口的时候设置flags标志位，也可以后面再调用方法设置
    w.setWindowFlags(Qt.FramelessWindowHint)

# 自定义window最大化最小化，关闭按钮
def window_example2():

    top_margin = 1
    btn_w = 60
    btn_h = 20

    close_btn = QPushButton(w)
    close_btn.setText('关闭')
    close_btn_width = close_btn.width()
    window_width = w.width()
    close_btn_x = window_width - btn_w
    close_btn_y = top_margin
    close_btn.move(close_btn_x,close_btn_y)
    close_btn.resize(btn_w,btn_h)

    close_btn.pressed.connect(w.close)

    w.setWindowFlags(Qt.FramelessWindowHint)
    max_btn = QPushButton(w)
    max_btn.setText('最大化')
    max_btn_x = close_btn_x - btn_w
    max_btn_y = top_margin
    max_btn.move(max_btn_x,max_btn_y)
    max_btn.resize(btn_w, btn_h)

    def cao():
        if w.isMaximized():
            w.showNormal()
            max_btn.setText('最大化')
        else:
            w.showMaximized()
            max_btn.setText('恢复')

    max_btn.pressed.connect(cao)

    min_btn = QPushButton(w)
    min_btn.setText('最小化')
    min_btn_x = max_btn_x - btn_w
    min_btn_y = top_margin
    min_btn.move(min_btn_x, min_btn_y)
    min_btn.resize(btn_w, btn_h)

    min_btn.pressed.connect(w.showMinimized)
# windowIcon()
# window_example1()
window_example2()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())


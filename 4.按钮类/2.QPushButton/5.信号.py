"""
信号都是继承下来的

QAbstractButton
    pressed():按下鼠标
    released()：释放鼠标
    clikcedchecked()：按下+释放
    toggled(bool checked)：切换信号

QWidget
    windowTitleChanged(QString)：窗口标题更改信号
    windowIconChange(QIcon)：窗口图标更改信号
    customContextMenuRequested(QPoint)：自定义上下文菜单请求信号
        setContextMenu(Qt.CustomContextMenu)
        Qt.DefaultContextMenu：调用对象方法ContextMenuEvent()
        Qt.CustomContextMenu:发射信号

"""
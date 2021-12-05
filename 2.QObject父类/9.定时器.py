"""
API
    starTimer(ms,Qt.timerType)--返回值：timer_id
        功能：开启一个定时器
        参数：Qt.TimerType
            Qt.PreciseTimer:精确定时器：尽可能保持毫秒精确
            Qt.CoarseTimer：粗定时器：5%的误差时间间隔
            Qt.VertCoarseTimer:很粗的定时器，只能到秒级
        返回值：timer_id
            定时器的唯一标识

    KillTimer(timer_id)
        根据定时器ID，杀死定时器
    timerEvent
        定时器执行事件

应用场景

"""
from PyQt5.Qt import *
import sys


class MyObject(QObject):
    # 重写父类方法
    def timerEvent(self, evt):
        print(evt)


# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("定时器的使用")
w.resize(500, 500)

obj = MyObject()

# 启动定时器
timer_id = obj.startTimer(1000)

# 杀死定时器
obj.killTimer(timer_id)

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

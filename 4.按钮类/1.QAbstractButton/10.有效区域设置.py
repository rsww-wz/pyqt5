"""
API
    重写hitButton(QPoint)
        有效返回True
        无效返回False
应用场景
    指定用户点击某个区域有效，而不是单一的矩形

练习
    设置一个正方形的按钮，只有点击正方形的内切圆范围内才有效
"""

from PyQt5.Qt import *
import sys

# 重写hitButton类
class Btn(QPushButton):
    def hitButton(self,point):

        # 坐标是以按钮左上角为坐标原点
        # print(point)

        if point.x() > self.width() / 2:
            # 返回True，该点击的区域是有效区域
            return True

        else:
            # 返回False，该点击的区域是无效区域
            return False

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("有效区域设置")
w.resize(500,500)

btn = Btn(w)
btn.move(200,200)
btn.setText('点击')
btn.pressed.connect(lambda :print('按钮被点击了'))


# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())


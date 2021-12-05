"""
描述
    用来描述一个键位序列
    键位序列描述必须一起使用以执行某些操作的键组合

键位序列分类
    标准键位序列
    自定义键位序列
        字符串："Ctrl+S"
        枚举值：Qt.Ctrl + Qt.Key_S
    注意
        优先使用标准键位序列
        自定义键位序列，保证可读，尽可能不使用枚举值对应整型数字

功能作用
    构造函数
        QKeySequence(key_str)
        QKeySequence(QKeySequence.StandardKey Key)
        QKeySequence(int k1,int k2)
        静态方法：fromString(key_str)
    转换成可读字符串
        tostring()  -> str

    键位个数：count()


"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("快捷键设置")
w.resize(500, 500)

kse = QKeySequenceEdit(w)
kse.move(200, 200)

btn = QPushButton('获取快捷键', w)
btn.move(200, 250)

# 创建快捷键对象
# 自定义
# obj = QKeySequence("Ctrl+S")

# 标准
obj = QKeySequence(QKeySequence.Copy)

# 使用枚举值
obj = QKeySequence(Qt.CTRL + Qt.Key_S, Qt.CTRL + Qt.Key_C)
kse.setKeySequence(obj)


# 获取快捷键
def cao():
    obj = kse.keySequence()
    obj = obj.toString()
    print(obj)


btn.clicked.connect(cao)

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

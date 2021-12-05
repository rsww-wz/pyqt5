"""
描述
    浮点类型步长调节器
        0.00 - 99.99
        1.00% - 99.99%

    即可以通过步长调节器调整数据，也可以文本框直接编辑

继承：QAbstractSpinBox
功能大致和QSpinBox相同，在设置精度上会稍有不同
    设置数值范围：同QSpinBox  换成浮点数
    设置步长：同QSpinBox  换成浮点数
    设置数值循环：同上
    设置前后缀：同上
    设置最小值文本：同上

    设置小数位数
        setDecimals(int)
        decimals() -> int

        设置支持更高精度的数据

    清除数据
        cleanText() -> str
        返回的是字符串类型，不包括前后缀和空格

    其他功能相同

信号：相同

"""
from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

# 创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("QDoubleSpinBox")
w.resize(500, 500)

# 默认范围：0.00 - 99.99
# 默认步长：1.0
dsp = QDoubleSpinBox(w)
dsp.resize(100, 20)
dsp.move(200, 200)


# 功能测试
def func_text():
    # 设置最大值
    dsp.setMaximum(3.14)

    # 设置范围
    dsp.setRange(-3.14, 3.14)

    # 设置步长
    dsp.setSingleStep(0.2)

    # 设置循环
    dsp.setWrapping(True)

    # 设置小数位数
    dsp.setDecimals(1)

    # 获取小数位数
    print(dsp.decimals())


func_text()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

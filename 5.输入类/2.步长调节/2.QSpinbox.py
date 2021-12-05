"""
描述
    主要处理整数和离散值集
    允许用户通过单击向上向下或者键盘上下按键来选择值
    旋转框支持整数，也可以子类化此类实现更多支持

继承：QAbstractSpinBox

功能设置
    设置数值范围
        setMaximum():设置最大值
        setMinimum():设置最小值

        maximum() -> int
        minimum() -> int

        setRange(min_mum,max_num): 设置数值区间

    数值循环
        setWrapping(bool)
        wrapping() -> bool
        设置数值达到最大或者最小值时，跳转到最大或者最小值

    设置步长
        setSingleStep(step_int)
        singleStep()  -> int
        设置步长调节器，单步步长

    前缀和后缀
        setPrefix('str')：设置前缀作为展示
        prefix() -> str

        setSuffix('str') :设置后缀作为展示
        suffix() -> str

    最小值特殊文本
        setSpecialValueText(str)
            父类中的方法
            当数据到达最小值时，会显示此字符串
        设置特殊含义的数值字符串

    显示基数(进制)
        setDisplayIntegerBase(int)  默认是10
        displayIntegerBase() -> int

        控制文本框内容的显示基数，以几进制的跨市进行显示

    设置和获取数值
        setValue(int)
        value() -> int
        设置以及获取数据,只会获取数值，不会获取文本框中的文本

    自定义展示格式
        重写：textFromValue(p_int) -> format_str
        展示数值之前，调用此方法，转换成对应的格式字符串进行展示

信号
    valueChanged[参数类型]()
        对象.valueChanged[str/int]().connect(槽函数)
"""
from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("QSpinBox")
w.resize(500,500)

# 创建控件: 可以直接使用上下调节按钮，最小值默认为零
sb = QSpinBox(w)
sb.resize(100,20)
sb.move(200,200)


# 设置数据范围
def func_text():

    # 设置最大值
    sb.setMaximum(20)

    # 设置最小值
    sb.setMinimum(-20)

    # 设置范围
    sb.setRange(-30,30)

    # 获取范围
    print(sb.maximum())
    print(sb.minimum())

    # 数值循环：设置达到最大或者最小值后是否跳转数值
    sb.setWrapping(True)

    # 查看是否设置数值循环
    print(sb.wrapping())

    # 设置步长
    sb.setSingleStep(5)

    # 查看步长
    print(sb.singleStep())

    # 设置前缀
    sb.setPrefix('第')

    # 设置后缀
    sb.setSuffix('天')

    # 查看前后缀
    print(sb.prefix())
    print(sb.suffix())

    # 设置最小值文本
    sb.setSpecialValueText('不能再小了')

    # 设置进制
    sb.setDisplayIntegerBase(10)

    # 设置数值
    sb.setValue(12)

    # 获取数据
    print(sb.value())


func_text()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

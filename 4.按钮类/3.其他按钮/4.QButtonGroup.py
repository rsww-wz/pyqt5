"""
描述
    提供一个抽象的按钮容器，可以将多个按钮划分为一组
    布局可视化效果
    一般的都是可以被检查的按钮

继承：QObject
功能
    创建按钮组
    添加按钮
        addButton(QAbstractButton，id = -1)
        如果id为-1，则为一个按钮分配一个id，
        如果自己分配id，请使用正值避免id冲突
    查看按钮
        buttons()
            查看该分组中所有按钮组中的按钮
        button(ID)
            根据ID获取对应按钮，没有则返回None
        checkedButton()
            获取选中的那个按钮
    移出按钮
        removeButton(QAbstractButton)
            不是从界面上移出，而是移出分组
    绑定和获取ID
        setId(QAbstractButton,int)
        id(QAbstractButton)
            指定按钮对应ID
            如果不存在此按钮，则返回-1
        checkedId()
            获取选中的ID
            如果没有选中按钮则返回-1
        应用场景
            设置ID，方便识别用户选项
    独占设置
        setExclusive(bool)
        exclusive()
        应用场景：统一设置按钮组中的按钮是否独占(选择互斥)

信号(功能基本差不多)
    buttonClicked(int/QAbstractButton):当按钮组中的按钮被点击时，发射此信号
    buttonpressed(int/QAbstractButton):当按钮组中的按钮按下时，发射此信号
    buttonReleased(int/QAbstractButton):当按钮组中的按钮释放时，发射此信号
    buttonToggled(int/QAbstractButton):当按钮组中的按钮被切换状态时，发射此信号

    注意
        如果一个对象向外界提供的信号名称一样，单参数不一样，外接在使用信号时，可以使用如下格式进行选择
        signal_name[type]
            signal_name:信号名称
            type:参数类型
"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("QButtonGroup")
w.resize(500,500)

# 创建按钮
btn1 = QRadioButton('男',w)
btn1.move(100,100)
btn2 = QRadioButton('女',w)
btn2.move(100,150)

btn3 = QRadioButton('是',w)
btn3.move(200,100)
btn4 = QRadioButton('否',w)
btn4.move(200,150)

# 创建按钮组
sex_group = QButtonGroup(w)
answer_group = QButtonGroup(w)

# 添加分组
sex_group.addButton(btn1)
sex_group.addButton(btn2)

# 查看分组
print(sex_group.buttons())
print(answer_group.buttons())

# 统一设置ID
answer_group.addButton(btn3,3)
answer_group.addButton(btn4,4)

# 手动设置ID
sex_group.setId(btn1,1)
sex_group.setId(btn2,2)

# 获取ID
print(sex_group.id(btn1))
print(sex_group.id(btn2))

# 根据ID查看按钮
print(answer_group.button(3))

# 设置按钮被选中
btn4.setChecked(True)

# 查看被选中的按钮
print(answer_group.checkedButton())

# 获取选中按钮的ID
print(answer_group.checkedId())

# 设置按钮组中的按钮是否互斥
# False是不互斥，True是互斥
answer_group.setExclusive(False)

# 移出分组
sex_group.removeButton(btn1)
print(sex_group.buttons())

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

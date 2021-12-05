"""
API
    内容长度
        setMaxLength(int):设置限制输入的长度
        maxLength(): 获取输入长度
    只读限制
        setReadOnly(bool)
        isReadOnly()
    规则验证
        setValidator(QValidator):设置验证器
        setInputMask(mask_str)：掩码验证
    判断输入文本是否通过验证
        hasAcceptableInput()

应用场景
    限制用户在文本框中输入的内容

"""

# 设置验证器
"""
QValidator
    描述
        用于验证用户输入数据的合法性
        如果一个输入框设置了验证器
            会首先将内容传递给验证器验证
                validate(self,input_text,pos)  --- 返回一个元组，有三个元素
                    return(QValidator.Acceptable,input_text,pos):验证通过
                    return(QValidator.Intermediate,input_text,pos)：暂不作判断是否通过验证
                    return(QValidator.Invalid,input_text,pos):验证不通过

            如果输入框结束输入后，上述的验证状态并非有效，则会调用修复方法
                fixup(self,input_text)
                return 修正后文本

            是一个抽象类，使用前需要进行子类化操作
                自定义子类
                系统提供子类
                    QIntValidator(bottom,top,parent)：限制整型数据范围
                    QDoubleValidator
                        浮点类型数据限制范围
                    QRegExpValidator：通过正则表达式限定

    使用
        第一个
            子类化此类
        第二步
            validate(self,input_text,pos)
            fixup(self.input_text)

    QValidator使用逻辑总结
        QValidator是一个验证器，里面设置验证规则
        但是它是一个抽象类，不能直接实例化，要自己新建一个类，继承这个类，才能实例化
        如果建好规则，直接调用setValidator函数，把实例化对象传进来就可以给文本框设置输入规则了

        QValidator可以自定义子类；或者使用QValidator提供了三个子类；实例化QValidator

        如果使用的是自定义子类提供了两个函数
            validate(self,input_text,pos)  根据状态(合法，待处理，非法)，限制文本框的输入
            fixup(self,input_text)         对于中间态数据的处理

        如果使用系统提供的子类，就不需要自己创建子类了，系统提供的子类就是已经子类化的类的
            限制整型数据范围：QIntValidator(上限，下限，模式)
            限制整型数据范围：QDoubleValidator
            通过正则表达式限定：QRegExpValidator

"""

# 掩码验证
"""
掩码
    含义
        掩码可以指定固定位置的固定数据类型，达到一个格式上限制
        例如
            座机号码：四位区号-七号电话
            IP地址：xxx.xxx.xxx.xxx
        掩码有一串掩码字符和分隔符组成
        不同的掩码字符代表不同的规则和格式
        掩码字符串类似于正则表达式
        
    setInputMask(掩码表达式)
"""


from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("输入限制")
w.resize(500,500)


le = QLineEdit(w)
le.move(200,200)
le.setClearButtonEnabled(True)
le.setPlaceholderText('请输入密码')

le1 = QLineEdit(w)
le1.move(200,250)


# 长度限制,超过长度就不输入了
def maxlength():
    le.setMaxLength(6)

    # 获取最大输入长度
    print(le.maxLength())

# 只读限制,不能输入，文本框变灰
def readonly():
    le.setReadOnly(True)

    # 获取读写限制
    print(le.isReadOnly())

# 验证器
# 显示18-180的范围输入
def rules():

    # 应用写一个类，然后继承这个类，才能实例化，也就是子类实例化
    # validator = QValidator()        QValidator是抽象类，不能直接实例化

    # 自定义子类 实例化QValidator抽象类
    class temp_validator(QValidator):
        # input_str:输入的字符串
        # pos_str：光标位置
        def validate(self,input_str,pos_str):
            print(input_str,pos_str)

            # 先判断字符串是否全部有数字组成

            if 18 <= int(input_str) <= 180:
                # pos_str：控制输入的光标位置，如果是一个固定值，每次都输入光标都在那个位置
                # 合法数据会展示在文本框中
                return (QValidator.Acceptable,input_str,pos_str)

            elif 1 <= int(input_str) <= 17:
                # 中间状态，不做处理
                return (QValidator.Intermediate,input_str,pos_str)

            else:
                # 不合法数据不会展示在文本框中
                return (QValidator.Invalid,input_str,pos_str)


        def fixup(self,p_str):

            # 失去焦点的是否对中间态数据做处理
            if int(p_str) < 18:
                return '18'


    # 把对象传进来即可，难点是这个对象如何创建，并实现具体的规则
    # le.setValidator(validator)

    # 使用系统提供的子类
    # le.setValidator(QIntValidator(18,180))

    # 使用系统提供的正则表达式子类
    # QRegExp(reg)
    # QRegExpValidator(QRegExp)
    # setValidator(QRegExpValidator)

    # 18-19 20-99 100-179 180
    reg = r'1[8-9]|[2-9][0-9]|1[0-7][0-9]|180'
    le.setValidator(QRegExpValidator(QRegExp(reg)))

# 掩码
# 规则：共5位，左边两位（必须是大写字母），中间-，右边两位（必须是数字）
def mask():
    # setInputMask(掩码表达式)
    # 必须以">"开头，A表示大写字母，9表示数字
    # #表示占位符
    le1.setInputMask(">AA-99;#")

# maxlength()
# readonly()
rules()
mask()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

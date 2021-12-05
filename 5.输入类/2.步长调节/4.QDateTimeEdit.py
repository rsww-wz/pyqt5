"""
描述
    编辑日期和时间的单行文本框
    即可以用箭头调节，也可以使用键盘编辑输入，可以单独调节某个部分(年月日或者时分秒)

继承：QAbstractSpinBox

功能作用
    构造函数
        QDateTimeEdit(parent: QWidget = None)
        QDateTimeEdit(Union[QDateTime, datetime.datetime], parent: QWidget = None)
        QDateTimeEdit(Union[QDate, datetime.date], parent: QWidget = None)
        QDateTimeEdit(Union[QTime, datetime.time], parent: QWidget = None)

    日历选择
        是否弹出日历选择器
            setCalenDarPopup(bool)
            calendarPopup()
        自定义日历选择控件
            setCalendarWidget(QCalendarWidget)
            calendarWidget() -> QCalendarWidget

    获取日期和时间
        dateTime() -> QDateTime
        date() -> QDate
        time() -> QTime
信号
    dateTimeChanged(QDateTime datetime)
    dateChanged(QDate date)
    timeChanged(QTime time)

补充
    QDateTime
        描述：日期时间对象，它是QDate和QTime类的组合，包括年月日，时分秒毫秒

    QDate
        描述：日期对象，包括年月日

    QTime
        描述：时间对象，包括时分秒毫秒

"""

# 显示格式
"""
setDisplayFormat(format_str) : 设置日期时间显示格式
displaymat() ->  : 获取日期时间显示格式

日期
    d：没有前导零的数字的日期（1到31）
    dd：有前导零的数字的日期（01到31）
    ddd：缩写的本地化日期名称（例如Mon到Sun
    dddd：完整本地化的日明名称（如q“星期一”到"星期日”）

    M：没有前导零的数字的月份（1-12）
    MM：月份为前导零的数字（01-12）
    MMM：缩写的本地化月份名称（例如Jan'到Dec"）
    MMMM：完整的本地化月份名称（例如“1月”到“12月”）

    yy:年份为两位数字（00-99）
    yyyy：年份为四位数字

时间
    h：没有前导零的小时（如果显示AM/PM，则为0到23或1到12）
    hh：前导零的小时（如果AM/PM显示，则为00到2301到12）
    H：没有前导零的小时（0到23，即便有AM/PM显示）
    HH：前导零的小时（00到23，即便有AM/PM显示）
    m:没有前导零的分钟（0到59）
    mm:前导零（00到59）的分钟
    s:整秒没有前导零（0到59）
    ss:带有前导零（00到59）
    z:第二个小数部分，没有尾随零的毫秒（0到999）
    zzz:第二个小数部分，有尼随零的毫秒（000到999
    AP/A:便用AM/PM显示
    ap/a:使用am/pm显示
    t:时区
"""

# 最大和最小日期时间
"""
日期时间
    最大
        setMaximumDateTime(QDateTime) 
        maximumDateTime()
        clearMaximumDateTime()
    最小
        setMinimumDateTime(QDateTime)
        minimumDateTime() -> QDateTime
        clearMinimumDateTime()
    范围
        setDateTimeRange(min,max)
        
日期
    和日期时间的用法一样
    函数名中的DateTime改为Date即可
       
时间
    DateTime改为Time即可
"""

# QDateTime -- 日期时间对象
"""
描述
    日期时间对象
    它是QDate和QTime类的组合，包括年月日，时分秒毫秒
    
构造日期时间对象
    QDateTime()
    QDateTime(Union[QDateTime, datetime.datetime])
    QDateTime(Union[QDate, datetime.date])
    QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], timeSpec: Qt.TimeSpec = Qt.LocalTime)
    QDateTime(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)
    QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], Qt.TimeSpec, int)
    QDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], QTimeZone)

    currentDateTime()     当前时间
    currentDateTimeUtc()  世界标准时间

调整日期时间
    addYears(int)
    addMonths(int)
    addDays(int)
    addSecs(int)
    addMSecs(int)
    setDate(const QDate &date)
    setTime(const QTime &time)

计算时间差
    offsetFromUtc()
    secsTo(QDateTime)
    msecsTo(QDateTime)
"""

# QDate
"""
日期对象
    QDate()
    QDate(int, int, int)
    currentDate()
    
调整日期
    setDate(int,int,int)
    addYears(int)
    addMonths(int)
    addDays(int)
    
计算时间差
    daysTo()
    
获取时间
    day()：这一个月的第几天
    month()：第几天
    year()：第几年
    dayOfWeek()：这一周的第几天
    dayOfYear()：这一年总共多少天
    daysInMonth()：这一月总共多少天
    daysYear()：这一年总共几天

"""

# QTime
"""
时间对象
    QTime()
    QTime(int,int,int,int)
    currentTime()
    
调整时间
    addSecs(int)
    addMSecs(int)
    
计算机时间差
    secsTo(QTime)
    
计时
    start()
    restart()
    elapsed():以上两个方法启动后，至此方法调用时，经历的毫秒数
    
获取时间
    hour()
    minute()
    second()


"""

# 相关子类
"""
QDateEdit
    基于QDateTimeEdit控件的小控件
    主要操作日期部分
    继承：QDateTimeEdit
    
QTimeEdit
    基于QDateTimeEdit控件的小控件
    主要操作时间部分
    继承：QDateTimeEdit
    
QDateEdit和QTimeEdit的使用方法大致和QDateTimeEdit相同，函数名会有所不同

总结
    QDataTimeEdit：可以同时设置，年月日，时分秒
    QDataEdit：只能设置年月日
    QTimeEdit：只能设置时分秒

"""

from PyQt5.Qt import *
import sys

# 创建程序对象
app = QApplication(sys.argv)

#创建控件
w = QWidget()

# 设置控件
w.setWindowTitle("QDataTimeEdit")
w.resize(500,500)

# QDateTime  -- 时间日期对象
def dateTime():

    # 设置日期时间
    setDateTime = QDateTime(2020,11,11,12,00,00)

    # 创建控件并导入对象
    dte = QDateTimeEdit(setDateTime, w)
    dte.move(200, 200)

dateTime()

# 展示控件
w.show()

# 程序循环
sys.exit(app.exec_())

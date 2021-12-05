"""
1.大致了解PyQt5
2.基本程序结构
3.各种空间的特性和使用
4.控件的样式
5.资源的加载
6.控件的布局
7.事件和信号
8.动画特效
9.界面跳转
10.设计工具使用
11.其他
    网络
    多线程
    数据库
    文件操作
    绘图
    多媒体
    定时器
    定位
    国际化


1.PyQt5的结构
    PyQt5具备的功能很多，每个功能都是一个或者多个模块，不可能全部学过
    需要哪个模块就学习哪个模块
    查看模块网址：https://www.riverbankcomputing.com/static/Docs/PyQt5/sip-classes.html
    官网：https://pypi.org/project/pyqt5-tools/

常用模块
    QtWidgets：包含了一整套UI元素控件，用于建立符合系统的界面
    QtGui：涵盖了多种基本图形功能的类
        字体，图标，颜色，图形……
    QtCore：涵盖了包的核心的非GUI功能
        时间，文件，目录，链接，线程进程……

使用方法
    一般使用的都是类，到导入类就需要搞清楚这个类属于哪个模块的
    可以在官网中根据类找到所属模块
    但是有时候很多类不在同一个模块中，导入起来会非常麻烦，所以有一个专门的模块，就叫Qt
    这个模块将基本全部模块的类综合到一个单一的模块中
        好处：不用关心这个类在那个模块
        坏处：占用内存（不使用的类会占用内存）
"""
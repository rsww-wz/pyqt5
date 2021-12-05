"""
API
    对象.deleteLater()
        删除一个对象时，也会接触它与父对象的关系
        deleteLater()并没有将对象立即销毁，而是向主消息循环发送了一个event，下一次主消息循环受到这个event之后才会销毁对象
        这样做的好处是可以在这些延迟删除时间内完成一些操作，坏处就是内存释放不及时

应用场景
    想要移出某一个对象的时候使用

"""

from PyQt5.Qt import *

obj1 = QObject()
obj2 = QObject()
obj3 = QObject()

obj2.setParent(obj1)
obj3.setParent(obj2)

print(obj2.parent())

# 删除时会接触父子关系,并且不会立刻删除
# 删除控件不能用del语句删除，而应该使用deletelater函数
obj2.deleteLater()
print(obj1.children())
print(obj2)
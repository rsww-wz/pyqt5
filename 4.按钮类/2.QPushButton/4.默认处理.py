"""
API
    setAutoDefault(bool)
        设置自动默认按钮
        在某些GUI样式中，默认按钮被绘制，其周围有一个额外的框架，最多3个像素或更多
        Qt会自动在默认按钮周围保留此空间，即自动默认按钮可能会稍大的提示
        对于具有QDialog父级按钮，此属性默认值为True，反之
    autoDefault()
    setDefault(bool)
    isDefault()

应用场景
    一般是在对话框中使用

理解
    打开窗口的时候，焦点默认在某个按钮上

"""
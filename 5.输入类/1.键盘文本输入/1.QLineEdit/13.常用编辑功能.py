"""
退格：backspace()
删除：del_()
清空：clear()
复制：copy()
剪切：cut()
粘贴：paste()
撤销：undo()
重做：redo()
拖放：setDragEnabled(bool)

作用：通过代码控制编辑功能

有很多是右键标准菜单中已经有了的

选中文本(可以通过光标控制)
    setSelection(start_pos,length):选择指定区间文本
    selectAll()
    deselect():取消选中文本
    hasSelectedText():是否有选中文本
    selectionStart():选中的开始位置
    selectionEnd():选中的结束位置
    selectionLength：选中的长度

"""
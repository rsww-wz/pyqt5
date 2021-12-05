# 常用功能
"""
copy()
paste()
canPaste() -> bool
setUndoRedoEnabled(bool)
redo()
undo()
selectAll()
find(str,有参数)
    自己查

"""

# 其他功能
"""
滚动
    scrollToAnchor(p_str)

只读设置
    setReadOnly(bool)
    isReadOnly()  -> bool
    
tab控制
    setTabChangeFoucs(bool)
        控制tab键位的功能，是否改变焦点
        默认是false
    setTabStopDistance(p_str)
        制表位的距离
        默认是80像素
    setTabStopWidth(p_int)
        功能同上
    tabStopDistance() -> float
        获取距离
    tabStopWidth()  -> int
        获取宽度
        
锚点获取
    anchorAt(QPoint) ->str
    应用场景：返回位置pos处的锚点的引用，如果该点不存在锚点，则返回空字符串
"""
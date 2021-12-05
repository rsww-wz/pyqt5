# 自动格式化
"""
API
    setAutoFormattiog(QTextEdit.AutoFormatting)
        QTextEdit.AutoNone:不要做任何自动格式化
        QTextEdit.AutoBulletList:自动创建项目符号列表
        QTextEdit.AutoAll:应用所有自动格式
应用场景
    输入一些特点字符，会转化成对应的效果
"""

# 转换行模式
"""
API
    setLineWrapMode(QTextEdit.LineWrapMode)
        设置转换行模式
    lineWrapMode
        返回：QTextEdit.LineWrapMode
        获取转行模式
    setWordWrapMode(self,QTextOption.wrapMode)
        设置单词换行模式
    WordWrapMode(self)
        返回：QTextOption.wrapMode
        获取单词换行模式

补充
    QTextEdit.LineWrapMode
        QTextEdit.NoWrap:没有软换行，超过宽度后产生水平滚动条
        QTextEdit.WidgetWidth:
            以空间的宽度为限制
            但会保持单词的完整性
        QTextEdit.FixedPixelWidth
            填充像素宽度
            配置
                setLineWrapColumnOrWidth(int)
                LineWrapColumnOrWidth()  -> int
        QTextEdit.FixecdColumnWidth
            填充列的宽度
            配置
                setLineWrapColumnOrWidth(int)
                LineWrapColumnOrWidth()  -> int
    QTextOption.wrapMode
        QTextOption.NoWrap:文本根本没有包装
        QTextOption.WordWrap:保持单词完整性
        QTextOption.ManualWrap:与QTextOption.NoWrap相同
        QTextOption.WrapAnywhere:宽度够了后，随意在任何位置换行
        QTextOption.WrapAtWordBounddaryOrAnywhere:尽可能赶在单词的边界，否则就会任意位置换行

"""

# 覆盖模式
"""
API
    setOverwriteMode(bool)
    overwriteMode()  -> bool
    
应用场景
    切换覆盖模式，修改文本内容
    
    覆盖模式：insert键吃掉都面的词
    
"""

# 光标设置
"""
API
    光标宽度
        setCursorWidth(int)
        cursorWidth() -> int
    光标矩形
        cursorRectangle()  -> QRect
        
应用场景
    一般是结合覆盖模式来做，标识光标的宽度，给用户提醒
"""

# 对齐方式
"""
API
    setAlignment(Qt.Alignment)
        Qt.AlignLeft
        Qt.AlignRight
        Qt.AlignCenter
    alignment()  -> Qt.Alignment
"""
# 字体格式
"""
字体家族
    setFontFamily(family_str)
    fontFamily()
    技巧
        QFontDialog.getFont():查看可用的字体

字体样式
    字体粗细
        setFontWeight(int)
            QFont.Thin
            QFont.ExtrLight
            QFont.Light
            QFont.Normal
            QFont.Medium
            QFont.DemiBold
            QFont.Bold
            QFont.ExtraBold
            QFont.Black
        fontWeight()

    斜体
        setFontItalic(bool)
        fontItalic()

    下划线
        setFontUnderline(bool)
        fontUnderline()

    字体尺寸
        setFontPointSize(float)
        FontPointSize()

统一设置QFont
    setCurrentFont(QFont)
    currentFont()  -> QFont
"""

# 字体颜色
"""
背景颜色
    setTextBackgroundColor(QColor)
        将当前格式的文本背景颜色设置为指定颜色
    textBackgroundColor()   -> QColor
    
文本颜色
    setTextColor(QColor)
        将当前格式的文本颜色设置为指定颜色
    textColor()   -> QColor
"""

# 字符格式
"""
API
    setCurrentCharFormat(QTextCharFormat)
    mergeCurrentCharFormat(QTextCharFormat)
    currentCharFormat()  -> QTextCharFormat
应用场景
    针对于部分字符，设置特定的格式
    将新文本插入格式时使用的char格式
    如果编辑器有选择文本内容，则char格式直接应用于选择
    
补充
    QTextCharFormat
        里面有很多方法，需要的自己去查
"""

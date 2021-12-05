"""
选中
    setPosition(int pos,QTextCursor.Mode = MoveAnchor)
        设置光标位置
        需要反向设置回去
    movePosition(QTextCursor.ModeOperation,QTextCursor.Mode = MoveAnchor,int n = 1)
        移动指定长度后
        需要反向设置回去
    select(QTextCursor.SelectionType)
        需要反向设置回去

补充
    QTextCursor.MoveMode
        QTextCursor.MoveAnchor:将锚点移动到与光标本身相同的位置
        QTextCursor.KeepAnchor:将锚点固定在原处
    QTextCursor.MoveOperation
        QTextCursor.NoMove:将光标保持在原位
        QTextCursor.Stat:移动到文本开头
        QTextCursor.StatOfLine
        QTextCursor.StatOfBlock
        QTextCursor.StatOfWord
        QTextCursor.PreviousBlock：
        QTextCursor.PreviousCharacter
        QTextCursor.PreviousWord
        QTextCursor.Up
        QTextCursor.Left
        QTextCursor.WordLeft
        QTextCursor.End
        QTextCursor.EndOfLine
        QTextCursor.EndOfWord
        QTextCursor.EndOfBlock
        QTextCursor.EndBlock
        ……

    QTextCursor.SelectionType
        QTextCursor.Doucment:选中整个文档
        QTextCursor.BlockUnderCursor:选择光标下的文本块
        QTextCursor.LineUnderCursor:选中光标下单文本行
        QTextCursor.WordUnderCursor:选中光标下的单词

理解
    当选中文本时
        锚点：选中文本的开始位置
        光标：选中文本的结束位置
        锚点和光标之间的文本就是被选中的文本
"""
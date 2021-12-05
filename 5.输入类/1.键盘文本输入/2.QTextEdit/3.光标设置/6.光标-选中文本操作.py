"""
选中内容获取
    selectedText()
        str
    selection()
        QTextDocumentFragement
    selectedTableCells
        (int FirstRow,int numTows,int firstColumn,int unmColumns)

选中文本移出
    removeSelectedText()

选中的位置获取
    selectionStart()
        int
    selectionEnd()
        int

清空和判定
    clearSelection()
        取消文本选中
        需要反向设置
    hasSelection()
        bool
        是否有文本选中

删除内容
    deleteChar()
        如果没有选中文本，删除文本光标后的一个字符
        如果有选中文本，则删除选中文本

    deletePreviousChar()
        如果没有选中文本，删除文本光标前一个字符
        如果选中文本，则删除选中文本

位置相关
    atBlockEnd()      -- 是否在文本块末尾
    atBlockStart()    -- 是否在文本块开始
    atEnd()           -- 是否在文本末尾
    atStat()          -- 是否在文本开始
    columnNumber()    -- 在第几列
    position()        -- 光标位置
    positionInBlock() -- 在文本块中的位置

开始和结束编辑标识
    beginEditBlock()
    endEditBlock()
"""
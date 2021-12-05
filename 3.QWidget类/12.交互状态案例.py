from PyQt5.Qt import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("交互状态的案例")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        #要求：标签隐藏，文本框和按钮显示，按钮设置为不可用状态
        #当文本框有内容时，让按钮可用，否则不可用
        #当文本框内容为hello,点击按钮显示标签，并展示文本框为登录成功，否则登录失败

        #设置三个控件
        label = QLabel(self)
        label.setText("标签")
        label.move(100,50)
        label.hide()

        edit = QLineEdit(self)
        edit.setText("")
        edit.move(100,100)

        btn = QPushButton(self)
        btn.setText('登录')
        btn.move(100,150)
        btn.setEnabled(False)

        def text_cao(text):
            print('文本内容发生了改变',text)
            if len(text) > 0:
                btn.setEnabled(True)
            else:
                btn.setEnabled(False)

        edit.textChanged.connect(text_cao)

        def check():
            # 获取文本框内容
            content = edit.text()

            # 判断文本框内容
            if content == 'hello':
                # btn.setEnabled(True)
                label.show()
                label.setText('登录成功')
                label.adjustSize()
            else:
                # btn.setEnabled(True)
                label.show()
                label.setText('登录失败')
                label.adjustSize()

        btn.pressed.connect(check)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())

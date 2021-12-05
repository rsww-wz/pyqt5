"""
API
    isModified()
    setModified(bool)

应用场景
    标识文本内容是否被修改
"""

from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('是否被编辑')
window.resize(600,600)

le = QLineEdit(window)
le.move(200,200)
le.setPlaceholderText('请输入文本内容')
le.setClearButtonEnabled(True)

def edit():

    btn = QPushButton('确定',window)
    btn.move(200,250)

    def cao():
        # 是否被编辑过
        print(le.isModified())

        # 设置文本没有被编辑过
        le.setModified(False)

    btn.clicked.connect(cao)

edit()

window.show()
sys.exit(app.exec_())
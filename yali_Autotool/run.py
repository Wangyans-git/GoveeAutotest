from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget, QApplication
from yali_Autotool.package_main.handle_main import HandleMian


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon("config/touxiang.ico"))
    program = HandleMian()
    program.ui.show()
    app.exec_()
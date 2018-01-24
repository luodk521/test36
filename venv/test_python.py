from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from test import Ui_TestForm    # 导入生成form.py里生成的类
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_TestForm()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())#test11111

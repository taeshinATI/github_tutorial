import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QCheckBox, QPushButton
from PyQt5 import Qt, QtCore


class TableWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Checkbox in Table'
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.numRow = 5
        self.numCol = 5

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.numRow)
        self.tableWidget.setColumnCount(self.numCol)
        self.tableWidget.move(0, 0)

        self.InsertTable()

    def InsertTable(self):
        self.checkBoxList = []
        self.checkBoxList2 = []
        for i in range(self.numRow):
            ckbox = QPushButton(f"{i}")
            ckbox2 = QPushButton(f"{i+100}")
            self.checkBoxList.append(ckbox)
            self.checkBoxList2.append(ckbox2)

        for i in range(self.numRow):
            self.tableWidget.setCellWidget(i, 0, self.checkBoxList[i])
            self.tableWidget.setCellWidget(i, 1, self.checkBoxList2[i])

        self.checkBoxList2[0].clicked.connect(self.test)
        # self.showList(partial())
        self.tableWidget.move(0, 0)

    def showList(self, list_):
        print(list_)

    def test(self):
        print(self.checkBoxList[0].text())
        self.checkBoxList[0].setText('clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TableWidget()
    sys.exit(app.exec_())
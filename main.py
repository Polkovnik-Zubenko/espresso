import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("espresso.db")
        cur = self.connection.cursor()
        self.result = cur.execute("""SELECT * FROM ingredient""")
        self.pushButton.clicked.connect(self.func)
        self.pushButton.setText('Загрузить')
        self.setWindowTitle('Эспрессо')

    def func(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'Название сорта', 'Степень обжарки',
                                                    'Молотый/в зернах', 'Описание вкуса', 'Цена', 'Объем упаковки'])
        for i, row in enumerate(self.result):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())
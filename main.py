import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QMessageBox


class AddCoffeeDlg(QDialog):
    def __init__(self):
        super(AddCoffeeDlg, self).__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.setWindowTitle("Добавить кофе")

    def accept(self) -> None:
        data = ({"Name": self.NameLineEdit.text(),
                 "Roasting": self.RoastingLineEdit.text(),
                 "Type": self.TypeLineEdit.text(),
                 "Taste": self.TasteLineEdit.text(),
                 "Price": self.PriceLineEdit.text(),
                 "Size": self.SizeLineEdit.text()})
        for key in data.keys():
            if len(data[key].strip()) == 0:
                QMessageBox.warning(self, "Проверка данных", f'Не все поля заполнены',
                                    QMessageBox.Close)
                return

        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute('INSERT INTO coffee(Name, Roasting, Type, Taste, Price, Size) VALUES (?,?,?,?,?,?)',
                    [self.NameLineEdit.text(), self.RoastingLineEdit.text(), self.TypeLineEdit.text(),
                     self.TasteLineEdit.text(), self.PriceLineEdit.text(), self.SizeLineEdit.text()])
        con.commit()
        con.close()
        self.done(1)

    def reject(self) -> None:
        self.done(0)


class EditCoffeeDlg(QDialog):
    def __init__(self, data):
        super(EditCoffeeDlg, self).__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.ID = None
        self.set_data(data)
        self.setWindowTitle("Редактировать кофе")

    def set_data(self, data):
        self.ID = data["ID"]
        self.NameLineEdit.setText(data["Name"])
        self.RoastingLineEdit.setText(data["Roasting"])
        self.TypeLineEdit.setText(data["Type"])
        self.TasteLineEdit.setText(data["Taste"])
        self.PriceLineEdit.setText(data["Price"])
        self.SizeLineEdit.setText(data["Size"])

    def accept(self) -> None:
        modified = ({"Name": self.NameLineEdit.text(),
                     "Roasting": self.RoastingLineEdit.text(),
                     "Type": self.TypeLineEdit.text(),
                     "Taste": self.TasteLineEdit.text(),
                     "Price": self.PriceLineEdit.text(),
                     "Size": self.SizeLineEdit.text()})

        for key in modified.keys():
            if len(modified[key].strip()) == 0:
                QMessageBox.warning(self, "Проверка данных", f'Не все поля заполнены',
                                    QMessageBox.Close)
                return
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        que = "UPDATE coffee SET\n"
        que += ", ".join([f"{key}='{modified.get(key)}'"
                          for key in modified.keys()])
        que += "WHERE id = ?"
        cur.execute(que, (self.ID,))
        con.commit()
        con.close()
        self.done(1)

    def reject(self) -> None:
        self.done(0)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Капучино")
        self.db_name = 'coffee.sqlite'
        self.table()
        self.addInfoButton.clicked.connect(self.addInfoButton_clicked)
        self.editInfoButton.clicked.connect(self.editInfoButton_clicked)

    def addInfoButton_clicked(self):
        try:
            add_dlg = AddCoffeeDlg()
            add_dlg.show()
            if add_dlg.exec() == 1:
                self.table()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка добавления кофе в БД", e.__str__(),
                                 QMessageBox.Close)

    def editInfoButton_clicked(self):
        try:
            row_num = self.tableWidget.currentRow()
            if row_num < 0:
                return
            edit_data = dict({"ID": int(self.tableWidget.item(row_num, 0).text()),
                              "Name": self.tableWidget.item(row_num, 1).text(),
                              "Roasting": self.tableWidget.item(row_num, 2).text(),
                              "Type": self.tableWidget.item(row_num, 3).text(),
                              "Taste": self.tableWidget.item(row_num, 4).text(),
                              "Price": self.tableWidget.item(row_num, 5).text(),
                              "Size": self.tableWidget.item(row_num, 6).text()})
            edit_dlg = EditCoffeeDlg(edit_data)
            edit_dlg.show()
            if edit_dlg.exec() == 1:
                self.table()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка редактирования кофе в БД", e.__str__(),
                                 QMessageBox.Close)

    def table(self):
        try:
            con = sqlite3.connect(self.db_name)
            cur = con.cursor()
            cur.execute(f"""SELECT * FROM coffee""")
            db = cur.fetchall()
            self.tableWidget.setColumnCount(len(db[0]))
            self.tableWidget.setRowCount(len(db))
            self.tableWidget.setHorizontalHeaderLabels(
                ["ID", "Название сорта", "Степень обжарки", "Молотый/в зернах", "Описание вкуса", "Цена",
                 "Объем упаковки"])
            for i, elemi in enumerate(db):
                for j, elemj in enumerate(elemi[0:]):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elemj)))
            con.close()
            self.tableWidget.resizeColumnsToContents()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка подключения к БД", e.__str__(),
                                 QMessageBox.Close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

import sys
import design
from PyQt5 import QtWidgets, QtSql
import sqlite3
import os

db_path = '/home/redlance/Geekbrains/Python  prepare/Repository/Python-dev-Interview-prep/Lesson_6/db1'


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.current_table = None
        self.db_file = None
        self.setupUi(self)

        self.addButton.clicked.connect(self.add_row)
        self.delButton.clicked.connect(self.del_row)
        self.get_db_button.clicked.connect(self.get_db)

        self.actionCategories.triggered.connect(self.select_categories_table)
        self.actionVendors.triggered.connect(self.select_vendors_table)
        self.actionUnits.triggered.connect(self.select_units_table)
        self.actionGoods.triggered.connect(self.select_goods_table)
        self.actionPositions.triggered.connect(self.select_positions_table)
        self.actionEmployees.triggered.connect(self.select_employees_table)

    def get_db(self):
        self.db_file = os.path.abspath(str(QtWidgets.QFileDialog.getOpenFileName(
            self, "Выберите файл")[0]))

        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.db_file)

        self.label_2.setText(self.db_file)

        self.actionCategories.setEnabled(True)
        self.actionEmployees.setEnabled(True)
        self.actionGoods.setEnabled(True)
        self.actionPositions.setEnabled(True)
        self.actionUnits.setEnabled(True)
        self.actionVendors.setEnabled(True)

        connect = sqlite3.connect(self.db_file)
        cursor = connect.cursor()
        cursor.execute(
            "SELECT category_name AS Категория, category_description AS Описание FROM categories")
        result = cursor.fetchall()

    def add_item(self, cat, descr):
        connect = sqlite3.connect(db_path)
        cursor = connect.cursor()
        sql = "insert into categories (category_name, category_description) values (?, ?)"

        cursor.execute(sql, (cat, descr))
        connect.commit()

    def select_categories_table(self):
        if self.db.close():
            self.db.open()

        model = QtSql.QSqlTableModel()
        model.setTable('categories')
        self.current_table = 'categories'
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()

        self.tableView.setModel(model)

    def select_employees_table(self):
        if self.db.close():
            self.db.open()

        model = QtSql.QSqlTableModel()
        model.setTable('employees')
        self.current_table = 'employees'
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()

        self.tableView.setModel(model)

    def select_goods_table(self):
        if self.db.close():
            self.db.open()

        model = QtSql.QSqlTableModel()
        model.setTable('goods')
        self.current_table = 'goods'
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()

        self.tableView.setModel(model)

    def select_positions_table(self):
        if self.db.close():
            self.db.open()

        model = QtSql.QSqlTableModel()
        model.setTable('positions')
        self.current_table = 'positions'
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()

        self.tableView.setModel(model)

    def select_units_table(self):
        if self.db.close():
            self.db.open()

        model = QtSql.QSqlTableModel()
        model.setTable('units')
        self.current_table = 'units'
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()

        self.tableView.setModel(model)

    def select_vendors_table(self):
        if self.db.close():
            self.db.open()

        model = QtSql.QSqlTableModel()
        model.setTable('vendors')
        self.current_table = 'vendors'
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()

        self.tableView.setModel(model)

        # self.db.close()

    def add_row(self):
        model = QtSql.QSqlTableModel()
        model.setTable(self.current_table)
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        result = model.insertRows(model.rowCount(), 1)
        print(result)
        self.tableView.setModel(model)

    def del_row(self):
        print(
            f'Строка номер {self.tableView.currentIndex().row()} таблицы {self.current_table} удалена')
        model = QtSql.QSqlTableModel()
        model.setTable(self.current_table)
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()

        indices = self.tableView.selectionModel().selectedRows()
        for i in sorted(indices):
            model.removeRow(i.row())

        self.tableView.setModel(model)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

import os, re, docxtpl, pandas
from datetime import datetime

from PySide6 import QtWidgets, QtGui

from controls._functions import open_file, open_folder, preview_word, full_date, short_name
from controls._messages import ask_for_delete, export_xlsx_success, path_doesnt_exists, file_permission_denied
from controls._widgets import ContractsTableWidgetItem
from controls.create_docx_control import CreateDocxControl
from controls.edit_addictions_control import EditAddictionsControl
from controls.print_docx_control import PrintDocxControl

from dbm import DatabaseModel
from resources_rc import documents_path
from views.main_window import Ui_MainWindow


class MainControl(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, widget: QtWidgets.QMainWindow):
        super().__init__()
        self.widget = widget
        self.ask_for_delete = True
        self.filter_with_hidden_columns = True
        self.show_contract_info = True
        self.dbm = DatabaseModel()
        self.setupUi(widget)
        self.connectUi()
        self.loadData()

    def setupUi(self, widget):
        super().setupUi(widget)
        self.le_filter.setMinimumWidth(225)
        self.tw_contracts.setSortingEnabled(True)
        self.tw_contracts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tw_contracts.sortByColumn(0, QtGui.Qt.SortOrder.DescendingOrder)
        self.a_ask_for_delete.setChecked(self.ask_for_delete)
        self.a_filter_with_hidden_columns.setChecked(self.filter_with_hidden_columns)
        self.a_show_contract_info.setChecked(self.show_contract_info)
        self.l_contract_info.setVisible(self.show_contract_info)
        self.te_contract_info.setVisible(self.show_contract_info)
        visible_columns = self.dbm.prop.get_visible_columns()
        for column in range(14):
            if column in visible_columns: self.widget.findChild(QtGui.QAction, f'a_column_{column}').setChecked(True)
            else: self.tw_contracts.hideColumn(column)

    def connectUi(self):
        self.pb_create.clicked.connect(self.create_contract)
        self.pb_delete.clicked.connect(lambda: self.delete_contract(self.tw_contracts.currentRow()))
        self.pb_edit.clicked.connect(lambda: self.edit_contract(self.get_column(0)))
        self.pb_duplicate.clicked.connect(lambda: self.duplicate_contract(self.get_column(0)))
        self.pb_open_file.clicked.connect(lambda: self.file_action(self.get_column(13), open_file))
        self.pb_open_folder.clicked.connect(lambda: self.file_action(self.get_column(13), open_folder))
        self.pb_edit_contract_addictions.clicked.connect(lambda: self.edit_contract_addictions(self.get_column(0)))
        self.pb_preview_docx.clicked.connect(lambda: self.file_action(self.get_column(13), preview_word))
        self.pb_export_to_xlsx.clicked.connect(self.export_to_xlsx)
        self.pb_adjust.clicked.connect(self.adjust_contracts_table)
        self.pb_print.clicked.connect(lambda: self.print_docx(self.get_column(0)))
        self.tw_contracts.itemClicked.connect(self.print_contract_info)
        self.le_filter.textChanged.connect(self.filter_contracts_table)
        self.a_column_0.changed.connect(lambda: self.toggle_column_visible(0))
        self.a_column_1.changed.connect(lambda: self.toggle_column_visible(1))
        self.a_column_2.changed.connect(lambda: self.toggle_column_visible(2))
        self.a_column_3.changed.connect(lambda: self.toggle_column_visible(3))
        self.a_column_4.changed.connect(lambda: self.toggle_column_visible(4))
        self.a_column_5.changed.connect(lambda: self.toggle_column_visible(5))
        self.a_column_6.changed.connect(lambda: self.toggle_column_visible(6))
        self.a_column_7.changed.connect(lambda: self.toggle_column_visible(7))
        self.a_column_8.changed.connect(lambda: self.toggle_column_visible(8))
        self.a_column_9.changed.connect(lambda: self.toggle_column_visible(9))
        self.a_column_10.changed.connect(lambda: self.toggle_column_visible(10))
        self.a_column_11.changed.connect(lambda: self.toggle_column_visible(11))
        self.a_column_12.changed.connect(lambda: self.toggle_column_visible(12))
        self.a_column_13.changed.connect(lambda: self.toggle_column_visible(13))
        self.a_ask_for_delete.changed.connect(self.toggle_ask_for_delete)
        self.a_filter_with_hidden_columns.changed.connect(self.toggle_filter_with_hidden_columns)
        self.a_show_contract_info.changed.connect(self.toggle_show_contract_info)

    def loadData(self):
        contracts = self.dbm.contracts.get_all()
        for contract in contracts: self.add_contract(contract)
        self.ask_for_delete = self.dbm.prop.get_ask_for_delete()
        self.filter_with_hidden_columns = self.dbm.prop.get_filter_with_hidden_columns()
        self.show_contract_info = self.dbm.prop.get_show_contract_info()
        self.adjust_contracts_table()

    def add_contract(self, data):
        self.tw_contracts.setSortingEnabled(False)
        self.tw_contracts.model().insertRow(0)
        for column in range(self.tw_contracts.model().columnCount()):
            item = ContractsTableWidgetItem(data[column] if data[column] != '' else '-')
            self.tw_contracts.setItem(0, column, item)
            self.tw_contracts.setItem(10000, 1000000, 0)
        self.tw_contracts.setSortingEnabled(True)

    def delete_contract(self, row):
        if -1 < row < self.tw_contracts.rowCount():
            delete = True
            if self.ask_for_delete:
                delete = ask_for_delete(self.get_contract_info(self.get_column(0, row), True)) == 1
            if delete:
                self.dbm.contracts.delete(self.get_column(0, row))
                self.tw_contracts.removeRow(row)
                self.print_contract_info()

    def update_contract(self, contract):
        row = self.find_row_by_number(contract[0])
        for column in range(14):
            self.tw_contracts.item(row, column).setText(contract[column] if contract[column] != '' else '-')

    def create_contract(self):
        dialog = QtWidgets.QDialog(f=QtGui.Qt.WindowType.Window)
        CreateDocxControl(dialog, self)
        dialog.exec()
        self.adjust_contracts_table()

    def edit_contract(self, number):
        if self.tw_contracts.currentRow() != -1:
            dialog = QtWidgets.QDialog(f=QtGui.Qt.WindowType.Window)
            context = ['' if field == '-' else field for field in self.get_contract_info(number)]
            CreateDocxControl(dialog, self, context[1:12], context[0], context[13])
            dialog.exec()

    def duplicate_contract(self, number):
        if self.tw_contracts.currentRow() != -1:
            dialog = QtWidgets.QDialog(f=QtGui.Qt.WindowType.Window)
            context = ['' if field == '-' else field for field in self.get_contract_info(number)]
            CreateDocxControl(dialog, self, context[1:12])
            dialog.exec()

    def file_action(self, path, action):
        path_exists = action(path)
        row = self.tw_contracts.currentRow()
        number = self.get_column(0)
        if path_exists == 0:
            path_action = path_doesnt_exists(path)
            if path_action == 0: return
            dialog = ''
            if path_action == 1:
                dialog = QtWidgets.QFileDialog.getOpenFileName(self, f'Выберите новый путь для контракта {self.get_column(0, row)}', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
                if dialog == '': return
            elif path_action == 2:
                dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Восстановить контракт {self.get_column(0, row)}', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
                if dialog != '':
                    data = [field if field != '-' else '' for field in self.get_contract_info(self.get_column(0, row))[1:12]]
                    passport = [field if field != '-' else '' for field in re.split(' от |, к/п |, ', data[5])]
                    tpl = 1 if data[8] != '' else 2
                    docx = docxtpl.DocxTemplate(os.path.abspath(f'templates/contract{tpl}_tpl.docx'))
                    docx.render({
                        'service': data[0], 'phone': data[4], 'birthday': data[6], 'price': data[7],
                        'company_1': data[1], 'company_2': data[3], 'company_3': data[1],
                        'short_date_1': data[2], 'short_date_2': data[2],
                        'full_date_1': full_date(datetime.strptime(data[2], '%d.%m.%Y')), 'full_date_2': full_date(datetime.strptime(data[2], '%d.%m.%Y')), 'full_date_3': full_date(datetime.strptime(data[2], '%d.%m.%Y')), 'full_date_4': full_date(datetime.strptime(data[2], '%d.%m.%Y')),
                        'agent_1': short_name(data[3]), 'agent_2': short_name(data[3]), 'agent_3': short_name(data[3]), 'agent_4': short_name(data[3]), 'agent_5': short_name(data[3]),
                        'passport_code': passport[0] if passport[0] else '', 'passport_date': passport[1] if passport[1] else '', 'passport_kp': passport[2] if passport[2] else '', 'passport_issue': passport[3] if passport[3] else '',
                        'first_price': data[8], 'second_price': data[9], 'date_end': data[10]
                    })
                    try:
                        docx.save(dialog)
                    except PermissionError:
                        file_permission_denied()
                        return
                else: return
            name = dialog.rsplit('\\', 1)[-1][:-5]
            path = dialog
            self.tw_contracts.item(row, 12).setText(name)
            self.tw_contracts.item(row, 13).setText(path)
            self.dbm.contracts.update_name(name, number)
            self.dbm.contracts.update_path(path, number)
            self.print_contract_info()

    def edit_contract_addictions(self, number):
        if self.tw_contracts.currentRow() != -1:
            dialog = QtWidgets.QDialog(f=QtGui.Qt.WindowType.Window)
            context = ['' if field == '-' else field for field in self.get_contract_info(number)]
            EditAddictionsControl(dialog, self, context)
            dialog.exec()

    def print_docx(self, number):
        if self.tw_contracts.currentRow() != -1:
            dialog = QtWidgets.QDialog(f=QtGui.Qt.WindowType.Window)
            PrintDocxControl(dialog, self, number)
            dialog.exec()

    def export_to_xlsx(self):
        dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Экспорт в Excel', documents_path, 'Книга Microsoft Excel (*.xlsx)')[0]
        if dialog != '':
            table = [[self.tw_contracts.item(row, column).text() for column in range(self.tw_contracts.columnCount())]
                     for row in range(self.tw_contracts.rowCount())]
            header = [self.tw_contracts.horizontalHeaderItem(column).text() for column in
                      range(self.tw_contracts.columnCount())]
            try:
                excel_writer = pandas.ExcelWriter(dialog)
                data_frame = pandas.DataFrame(table, None, header)
                data_frame.to_excel(excel_writer, sheet_name='Контракты', index=False, na_rep='NaN')
                for column in data_frame:
                    column_width = max(data_frame[column].astype(str).map(len).max(), len(column)) + 1.5
                    column_index = data_frame.columns.get_loc(column)
                    excel_writer.sheets['Контракты'].set_column(column_index, column_index, column_width)
                excel_writer.close()
            except PermissionError:
                file_permission_denied()
            else:
                if export_xlsx_success(dialog) == 1:
                    open_file(dialog)

    def print_contract_info(self):
        def html(text):
            return '<!DOCTYPE HTML><html><head><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style="font-size:8.25pt; font-weight:400; font-style:normal;">' + text + '</body></html>'
        def p(text):
            return '<p style="margin: 0px;">' + text + '</p>'
        def bold(text):
            return '<span style="font-weight:800; text-decoration: underline;">' + text + '</span>'
        contract_info = self.get_contract_info(self.get_column(0), True)
        if contract_info is not None:
            self.te_contract_info.setHtml(html('\n'.join(f'{p(bold(field[0] + ":"))} {p(field[1])}' for field in contract_info)))
        else:
            self.te_contract_info.setHtml(html(''))

    def filter_contracts_table(self):
        string = self.le_filter.text()
        for row in range(self.tw_contracts.rowCount()):
            self.tw_contracts.hideRow(row)
            for column in range(
                    self.tw_contracts.columnCount()) if self.filter_with_hidden_columns else self.dbm.prop.get_visible_columns():
                if string in self.tw_contracts.item(row, column).text():
                    self.tw_contracts.showRow(row)
                    break

    def adjust_contracts_table(self):
        self.tw_contracts.setVisible(False)
        self.tw_contracts.resizeColumnsToContents()
        self.tw_contracts.resizeRowsToContents()
        self.tw_contracts.setVisible(True)

    def find_row_by_number(self, number):
        for n in range(self.tw_contracts.rowCount()):
            item = self.tw_contracts.item(n, 0)
            if item.text() == number:
                return self.tw_contracts.row(item)

    def get_column(self, column, row=None):
        if row is None:
            row = self.tw_contracts.currentRow()
        if row != -1:
            return self.tw_contracts.item(row, column).text()

    def get_contract_info(self, number, with_titles=False):
        contract_info = []
        row = self.find_row_by_number(number)
        if row is not None:
            for column in range(self.tw_contracts.columnCount()):
                contract_info.append((self.tw_contracts.horizontalHeaderItem(column).text(), self.tw_contracts.item(row, column).text()) if with_titles else self.tw_contracts.item(row, column).text())
            return contract_info

    def toggle_column_visible(self, column):
        self.dbm.prop.toggle_column_visible(column)
        self.tw_contracts.showColumn(column) if self.dbm.prop.get_column_visible(column) else self.tw_contracts.hideColumn(column)
        self.filter_contracts_table()

    def toggle_ask_for_delete(self):
        self.dbm.prop.toggle_ask_for_delete()
        self.ask_for_delete = self.dbm.prop.get_ask_for_delete()

    def toggle_filter_with_hidden_columns(self):
        self.dbm.prop.toggle_filter_with_hidden_columns()
        self.filter_with_hidden_columns = self.dbm.prop.get_filter_with_hidden_columns()
        self.filter_contracts_table()

    def toggle_show_contract_info(self):
        self.dbm.prop.toggle_show_contract_info()
        self.show_contract_info = self.dbm.prop.get_show_contract_info()
        self.l_contract_info.setVisible(self.show_contract_info)
        self.te_contract_info.setVisible(self.show_contract_info)

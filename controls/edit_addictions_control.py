import os, re, docxtpl

from PySide6 import QtWidgets, QtCore, QtGui

from controls._functions import full_date, short_name, get_price_text, open_file, open_folder, preview_word, month
from controls._messages import empty_fields, path_doesnt_exists, success, file_permission_denied

from dbm import DatabaseModel
from resources_rc import documents_path
from views.edit_addictions_window import Ui_EditAddictionsWindow


class EditAddictionsControl(QtWidgets.QMainWindow, Ui_EditAddictionsWindow):
    def __init__(self, widget: QtWidgets.QDialog, main, context):
        super().__init__()
        self.widget = widget
        self.main = main
        self.number = context[0]
        self.company = context[2]
        self.no = 'Заказчик отказался от услуг по собственной инициативе'
        self.dbm = DatabaseModel()
        self.setupUi(widget)
        self.connectUi()
        self.loadServices()
        self.pushContext(context)
        self.loadData()

    def setupUi(self, widget):
        super().setupUi(widget)
        validator = QtGui.QDoubleValidator(0.0, 1.7976931348623157e+308, 2)
        validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        self.le_af_price.setValidator(validator)
        self.le_coef_price.setValidator(validator)
        self.le_corf1_price.setValidator(validator)
        self.le_corf2_price.setValidator(validator)
        self.widget.setMaximumHeight(self.height())
        self.de_af_date.setDate(QtCore.QDate.currentDate())
        self.de_coef_date.setDate(QtCore.QDate.currentDate())
        self.de_corf1_date.setDate(QtCore.QDate.currentDate())
        self.de_corf2_date.setDate(QtCore.QDate.currentDate())
        self.pb_corf2_toggle_service.clearFocus()

    def connectUi(self):
        self.le_af_price.textChanged.connect(lambda: self.print_price_text(self.le_af_price, self.le_af_price_text))
        self.le_coef_price.textChanged.connect(lambda: self.print_price_text(self.le_coef_price, self.le_coef_price_text))
        self.le_corf1_price.textChanged.connect(lambda: self.print_price_text(self.le_corf1_price, self.le_corf1_price_text))
        self.le_corf2_price.textChanged.connect(lambda: self.print_price_text(self.le_corf2_price, self.le_corf2_price_text))
        self.cmb_af_service.currentTextChanged.connect(lambda: self.cmb_service_text_changed(self.cmb_af_service, self.pb_af_toggle_service, self.af_add_service, self.af_delete_service))
        self.cmb_coef_service.currentTextChanged.connect(lambda: self.cmb_service_text_changed(self.cmb_coef_service, self.pb_coef_toggle_service, self.coef_add_service, self.coef_delete_service))
        self.cmb_corf1_service.currentTextChanged.connect(lambda: self.cmb_service_text_changed(self.cmb_corf1_service, self.pb_corf1_toggle_service, self.corf1_add_service, self.corf1_delete_service))
        self.cmb_corf2_service.currentTextChanged.connect(lambda: self.cmb_service_text_changed(self.cmb_corf2_service, self.pb_corf2_toggle_service, self.corf2_add_service, self.corf2_delete_service))
        self.pb_af_save.clicked.connect(self.save_af)
        self.pb_af_open_file.clicked.connect(lambda: self.file_action(self.l_af_path.text()[6:], open_file))
        self.pb_af_open_folder.clicked.connect(lambda: self.file_action(self.l_af_path.text()[6:], open_folder))
        self.pb_af_docx.clicked.connect(lambda: self.file_action(self.l_af_path.text()[6:], preview_word, t='af'))
        self.pb_coef_save.clicked.connect(self.save_coef)
        self.pb_coef_open_file.clicked.connect(lambda: self.file_action(self.l_coef_path.text()[6:], open_file))
        self.pb_coef_open_folder.clicked.connect(lambda: self.file_action(self.l_coef_path.text()[6:], open_folder))
        self.pb_coef_docx.clicked.connect(lambda: self.file_action(self.l_coef_path.text()[6:], preview_word, t='coef'))
        self.pb_corf1_save.clicked.connect(self.save_corf1)
        self.pb_corf1_open_file.clicked.connect(lambda: self.file_action(self.l_corf1_path.text()[6:], open_file))
        self.pb_corf1_open_folder.clicked.connect(lambda: self.file_action(self.l_corf1_path.text()[6:], open_folder))
        self.pb_corf1_docx.clicked.connect(lambda: self.file_action(self.l_corf1_path.text()[6:], preview_word, t='coef'))
        self.pb_corf2_save.clicked.connect(self.save_corf2)
        self.pb_corf2_open_file.clicked.connect(lambda: self.file_action(self.l_corf2_path.text()[6:], open_file))
        self.pb_corf2_open_folder.clicked.connect(lambda: self.file_action(self.l_corf2_path.text()[6:], open_folder))
        self.pb_corf2_docx.clicked.connect(lambda: self.file_action(self.l_corf2_path.text()[6:], preview_word, t='coef'))

    def loadServices(self):
        services = ([self.no] if self.no not in self.dbm.services.get_all() else []) + self.dbm.services.get_all()
        for combo_box in self.widget.findChildren(QtWidgets.QComboBox):
            for service in services:
                combo_box.addItem(str(service))

    def pushContext(self, context):
        self.l_contract_number.setText(f'Контракт: {context[0] if context[0] else "-"}')
        self.l_contract_service.setText(f'Услуга: {context[1] if context[1] else "-"}')
        self.l_contract_price.setText(f'Оплата: {context[8] + " рублей" if context[8] else "-"}' + (f' (предоплата {context[9]}, доплата {context[10]})' if context[9] else ''))
        self.l_contract_path.setText(f'Путь: {context[13] if context[13] else "-"}')
        for agent in self.widget.findChildren(QtWidgets.QLineEdit, QtCore.QRegularExpression('^.+agent$')):
            agent.setText(context[4])
        for price in self.widget.findChildren(QtWidgets.QLineEdit, QtCore.QRegularExpression('^.+price$')):
            price.setText(context[8])
        for combo_box in self.widget.findChildren(QtWidgets.QComboBox):
            combo_box.setCurrentText(context[1])
        self.le_af_company.setText(self.company)
        passport = [field if field != '-' else '' for field in re.split(' от |, к/п |, ', context[6])]
        self.le_coef_document.setText('Паспорт')
        self.le_coef_document_code.setText(passport[0] if passport[0] else '')
        self.de_coef_document_issue_date.setDate(QtCore.QDate.fromString(passport[1], 'dd.MM.yyyy'))
        self.le_coef_document_issue_place.setText(passport[3] if passport[3] else '')
        if context[9]:
            self.le_corf1_price.setText(context[9])
            self.le_corf2_price.setText(context[10])
        else:
            self.hide_corf2()
        for line_edit in self.widget.findChildren(QtWidgets.QLineEdit):
            line_edit.setCursorPosition(0)

    def loadData(self):
        act = self.dbm.acts.get(self.number)
        ce_order = self.dbm.ce_orders.get(self.number)
        cr_orders = self.dbm.cr_orders.get(self.number)
        if act:
            for button in self.t_act_form.findChildren(QtWidgets.QPushButton, QtCore.QRegularExpression('^.+_af_.+$')):
                button.setEnabled(True)
            self.cmb_af_service.setCurrentText(act[1])
            self.de_af_date.setDate(QtCore.QDate(QtCore.QDate.fromString(act[2], 'dd.MM.yyyy')))
            self.le_af_agent.setText(act[3])
            self.le_af_company.setText(act[4])
            self.le_af_price.setText(act[5].replace(',', '.'))
            self.l_af_path.setText('Путь: ' + act[6])
        if ce_order:
            for button in self.t_cash_order_expense_form.findChildren(QtWidgets.QPushButton, QtCore.QRegularExpression('^.+_coef_.+$')):
                button.setEnabled(True)
            self.cmb_coef_service.setCurrentText(ce_order[1])
            self.de_coef_date.setDate(QtCore.QDate.fromString(ce_order[2], 'dd.MM.yyyy'))
            self.le_coef_agent.setText(ce_order[3])
            self.le_coef_price.setText(ce_order[4].replace(',', '.'))
            self.pte_coef_addiction.setPlainText(ce_order[5])
            self.le_coef_document.setText(ce_order[6])
            self.le_coef_document_code.setText(ce_order[7])
            self.de_coef_document_issue_date.setDate(QtCore.QDate.fromString(ce_order[8], 'dd.MM.yyyy'))
            self.le_coef_document_issue_place.setText(ce_order[9])
            self.l_coef_path.setText('Путь: ' + ce_order[10])
        for cr_order in cr_orders:
            t = cr_order[1]
            for button in self.t_cash_order_receipt_forms.findChildren(QtWidgets.QPushButton, QtCore.QRegularExpression(f'^.+_corf{t}_.+$')):
                button.setEnabled(True)
            self.t_cash_order_receipt_forms.findChild(QtWidgets.QComboBox, f'cmb_corf{t}_service').setCurrentText(cr_order[2])
            self.t_cash_order_receipt_forms.findChild(QtWidgets.QDateEdit, f'de_corf{t}_date').setDate(QtCore.QDate.fromString(cr_order[3], 'dd.MM.yyyy'))
            self.t_cash_order_receipt_forms.findChild(QtWidgets.QLineEdit, f'le_corf{t}_agent').setText(cr_order[4])
            self.t_cash_order_receipt_forms.findChild(QtWidgets.QLineEdit, f'le_corf{t}_price').setText(cr_order[5])
            self.t_cash_order_receipt_forms.findChild(QtWidgets.QLabel, f'l_corf{t}_path').setText('Путь: ' + cr_order[6])

    def file_action(self, path, action, t=None):
        path_exists = action(path, t)
        if path_exists == 0:
            path_action = path_doesnt_exists(path)
            if path_action == 1:
                dialog = QtWidgets.QFileDialog.getOpenFileName(self, f'Выберите новый путь для контракта {self.number}', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
                if dialog != '':
                    path = dialog.replace('/', '\\')
                    self.dbm.acts.update_path(path)
            elif path_action == 2:
                pass

    def save_af(self):
        if self.cmb_af_service.currentText() == '' or self.le_af_agent.text() == '' or self.le_af_company.text() == '' or self.le_af_price.text() == '':
            if empty_fields() == 0: return
        if self.l_af_path.text() != 'Путь:':
            dialog = self.l_af_path.text()[6:]
            act_action = self.dbm.acts.update
            is_new = False
        else:
            dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Создать акт', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
            act_action = self.dbm.acts.add
            is_new = True
        if dialog != '':
            data = [
                self.number,
                self.cmb_af_service.currentText(),
                self.de_af_date.date().toString('dd.MM.yyyy'),
                self.le_af_agent.text(),
                self.le_af_company.text(),
                self.le_af_price.text() if '.' in self.le_af_price.text() else self.le_af_price.text() + '.00',
                dialog,
            ]
            docx = docxtpl.DocxTemplate(os.path.abspath(f'templates/act_tpl.docx'))
            docx.render({
                'n': data[0], 'service': data[1],
                'date_full': full_date(self.de_af_date.date().toPython()),
                'agent_1': short_name(data[3]), 'agent_2': short_name(data[3]), 'company': data[4],
                'price_1': data[5], 'price_2': data[5], 'price_3': data[5],
                'price_text': self.le_af_price_text.text()
            })
            try:
                docx.save(dialog)
            except PermissionError:
                file_permission_denied()
                return
            act_action(data)
            if success(is_new) == 2:
                dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Выберите новый путь для акта {self.number}', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
                if dialog != '':
                    self.dbm.acts.update_path(dialog, self.number)
                    self.l_af_path.setText(dialog)
            self.pb_af_open_file.setEnabled(True)
            self.pb_af_open_folder.setEnabled(True)
            self.pb_af_docx.setEnabled(True)
            self.l_af_path.setText(f'Путь: {dialog}')

    def save_coef(self):
        if self.cmb_coef_service.currentText() == '' or self.le_coef_agent.text() == '' or self.le_coef_price.text() == '' or self.le_coef_document.text() == '' or self.le_coef_document_code.text() == '' or self.le_coef_document_code.text() == '':
            if empty_fields() == 0: return
        if self.l_coef_path.text() != 'Путь:':
            dialog = self.l_coef_path.text()[6:]
            coef_action = self.dbm.ce_orders.update
            is_new = False
        else:
            dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Создать расходный кассовый ордер', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
            coef_action = self.dbm.ce_orders.add
            is_new = True
        if dialog != '':
            data = [
                self.number,
                self.cmb_coef_service.currentText(),
                self.de_coef_date.date().toString('dd.MM.yyyy'),
                self.le_coef_agent.text(),
                self.le_coef_price.text() if '.' in self.le_coef_price.text() else self.le_coef_price.text() + '.00',
                self.pte_coef_addiction.toPlainText(),
                self.le_coef_document.text(),
                self.le_coef_document_code.text(),
                self.de_coef_document_issue_date.date().toString('dd.MM.yyyy'),
                self.le_coef_document_issue_place.text(),
                dialog,
            ]
            docx = docxtpl.DocxTemplate(os.path.abspath(f'templates/cash_expense_order_tpl.docx'))
            docx.render({
                'n': data[0], 'service': data[1], 'addiction': data[5],
                'date': data[2], 'd': data[2][:2], 'm': month(int(data[2][3:5])), 'y': data[2][6:],
                'agent_full': data[3], 'agent_requisites': ', '.join(data[6:10]),
                'price': data[4], 'price_text_1': self.le_af_price_text.text().rsplit(' ', 3)[0], 'price_text_2': self.le_af_price_text.text().rsplit(' ', 3)[0],
            })
            try:
                docx.save(dialog)
            except PermissionError:
                file_permission_denied()
                return
            coef_action(data)
            if success(is_new) == 2:
                dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Выберите новый путь для расходного кассового ордера {self.number}', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
                if dialog != '':
                    self.dbm.acts.update_path(dialog, self.number)
                    self.l_coef_path.setText(dialog)
            self.pb_coef_open_file.setEnabled(True)
            self.pb_coef_open_folder.setEnabled(True)
            self.pb_coef_docx.setEnabled(True)
            self.l_coef_path.setText(f'Путь: {dialog}')

    def save_corf1(self):
        if self.cmb_corf1_service.currentText() == '' or self.le_corf1_agent.text() == '' or self.le_corf1_price.text() == '':
            if empty_fields() == 0: return
        if self.l_corf1_path.text() != 'Путь:':
            dialog = self.l_corf1_path.text()[6:]
            corf1_action = self.dbm.cr_orders.update
            is_new = False
        else:
            dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Создать приходный кассовый ордер', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
            corf1_action = self.dbm.cr_orders.add
            is_new = True
        if dialog != '':
            data = [
                self.number,
                '1',
                self.cmb_corf1_service.currentText(),
                self.de_corf1_date.date().toString('dd.MM.yyyy'),
                self.le_corf1_agent.text(),
                self.le_corf1_price.text() if '.' in self.le_corf1_price.text() else self.le_corf1_price.text() + '.00',
                dialog,
            ]
            docx = docxtpl.DocxTemplate(os.path.abspath(f'templates/cash_receipt_order_tpl.docx'))
            docx.render({
                'n_1': data[0], 'n_2': data[0], 'service_1': data[2], 'service_2': data[2],
                'date': data[3], 'd': data[3][:2], 'm': month(int(data[3][3:5])), 'y': data[3][6:],
                'agent_1': short_name(data[4]), 'agent_2': short_name(data[4]),
                'price_1': data[5], 'price_2': data[5][:-3],
                'price_text_1': self.le_corf1_price_text.text().rsplit(' ', 3)[0], 'price_text_2': self.le_corf1_price_text.text().rsplit(' ', 3)[0],
            })
            try:
                docx.save(dialog)
            except PermissionError:
                file_permission_denied()
                return
            corf1_action(data)
            if success(is_new) == 2:
                dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Выберите новый путь для приходного кассового ордера {self.number}/1', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
                if dialog != '':
                    self.dbm.acts.update_path(dialog, self.number)
                    self.l_coef_path.setText(dialog)
            self.pb_corf1_open_file.setEnabled(True)
            self.pb_corf1_open_folder.setEnabled(True)
            self.pb_corf1_docx.setEnabled(True)
            self.l_corf1_path.setText(f'Путь: {dialog}')

    def save_corf2(self):
        if self.cmb_corf2_service.currentText() == '' or self.le_corf2_agent.text() == '' or self.le_corf2_price.text() == '':
            if empty_fields() == 0: return
        if self.l_corf2_path.text() != 'Путь:':
            dialog = self.l_corf2_path.text()[6:]
            corf2_action = self.dbm.cr_orders.update
            is_new = False
        else:
            dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Создать приходный кассовый ордер', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
            corf2_action = self.dbm.cr_orders.add
            is_new = True
        if dialog != '':
            data = [
                self.number,
                '2',
                self.cmb_corf2_service.currentText(),
                self.de_corf2_date.date().toString('dd.MM.yyyy'),
                self.le_corf2_agent.text(),
                self.le_corf2_price.text() if '.' in self.le_corf2_price.text() else self.le_corf2_price.text() + '.00',
                dialog,
            ]
            docx = docxtpl.DocxTemplate(os.path.abspath(f'templates/cash_receipt_order_tpl.docx'))
            docx.render({
                'n_1': data[0], 'n_2': data[0], 'service_1': data[2], 'service_2': data[2],
                'date': data[3], 'd': data[3][:2], 'm': month(int(data[3][3:5])), 'y': data[3][6:],
                'agent_1': short_name(data[4]), 'agent_2': short_name(data[4]),
                'price_1': data[5], 'price_2': data[5][:-3],
                'price_text_1': self.le_corf2_price_text.text().rsplit(' ', 3)[0], 'price_text_2': self.le_corf2_price_text.text().rsplit(' ', 3)[0],
            })
            try:
                docx.save(dialog)
            except PermissionError:
                file_permission_denied()
                return
            corf2_action(data)
            if success(is_new) == 2:
                dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Выберите новый путь для приходного кассового ордера {self.number}/2', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
                if dialog != '':
                    self.dbm.acts.update_path(dialog, self.number)
                    self.l_coef_path.setText(dialog)
            self.pb_corf2_open_file.setEnabled(True)
            self.pb_corf2_open_folder.setEnabled(True)
            self.pb_corf2_docx.setEnabled(True)
            self.l_corf2_path.setText(f'Путь: {dialog}')

    def hide_corf2(self):
        self.l_corf1.setText('Приходный кассовый ордер')
        self.w_corf2_actions.setVisible(False)
        self.w_corf2.setVisible(False)

    def print_price_text(self, price, price_text):
        price_text.setText(get_price_text(price.text()))
        price_text.setCursorPosition(0)

    def cmb_service_text_changed(self, combo_box, button, add, delete):
        if combo_box.currentText() == '' or (combo_box.currentText() == self.no and self.no not in self.dbm.services.get_all()):
            button.setEnabled(False)
        else:
            button.setEnabled(True)
            while True:
                try: button.clicked.disconnect(add)
                except: break
            while True:
                try: button.clicked.disconnect(delete)
                except: break
            if combo_box.currentText() not in [combo_box.itemText(index) for index in range(combo_box.count())]:
                button.setIcon(QtGui.QIcon(":/icons/icons/plus.ico"))
                button.clicked.connect(add)
            else:
                button.setIcon(QtGui.QIcon(":/icons/icons/minus.ico"))
                button.clicked.connect(delete)

    def add_service(self, current_combo_box):
        current_text = current_combo_box.currentText()
        self.dbm.services.add(current_text)
        services = ([self.no] if self.no not in self.dbm.services.get_all() else []) + self.dbm.services.get_all()
        for combo_box in self.widget.findChildren(QtWidgets.QComboBox):
            combo_box.clear()
            for service in services:
                combo_box.addItem(str(service))
            combo_box.setCurrentText(current_text)
        self.cmb_text_changed()

    def delete_service(self, current_combo_box):
        self.dbm.services.delete(current_combo_box.currentText())
        services = ([self.no] if self.no not in [] else []) + self.dbm.services.get_all()
        for combo_box in self.widget.findChildren(QtWidgets.QComboBox):
            combo_box.clear()
            for service in services:
                combo_box.addItem(str(service))
        self.cmb_text_changed()

    def cmb_text_changed(self):
        self.cmb_service_text_changed(self.cmb_af_service, self.pb_af_toggle_service, self.af_add_service, self.af_delete_service)
        self.cmb_service_text_changed(self.cmb_coef_service, self.pb_coef_toggle_service, self.coef_add_service, self.coef_delete_service)
        self.cmb_service_text_changed(self.cmb_corf1_service, self.pb_corf1_toggle_service, self.corf1_add_service, self.corf1_delete_service)
        self.cmb_service_text_changed(self.cmb_corf2_service, self.pb_corf2_toggle_service, self.corf2_add_service, self.corf2_delete_service)

    def af_add_service(self):
        return self.add_service(self.cmb_af_service)

    def coef_add_service(self):
        return self.add_service(self.cmb_coef_service)

    def corf1_add_service(self):
        return self.add_service(self.cmb_corf1_service)

    def corf2_add_service(self):
        return self.add_service(self.cmb_corf2_service)

    def af_delete_service(self):
        return self.delete_service(self.cmb_af_service)

    def coef_delete_service(self):
        return self.delete_service(self.cmb_coef_service)

    def corf1_delete_service(self):
        return self.delete_service(self.cmb_corf1_service)

    def corf2_delete_service(self):
        return self.delete_service(self.cmb_corf2_service)

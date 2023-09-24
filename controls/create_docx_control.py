import os.path, re, docxtpl

from PySide6 import QtWidgets, QtCore, QtGui

from controls._functions import full_date, short_name
from controls._messages import empty_fields, ask_for_save, file_permission_denied

from dbm import DatabaseModel
from resources_rc import documents_path
from views.create_docx_window import Ui_CreateDocxWindow


class CreateDocxControl(QtWidgets.QMainWindow, Ui_CreateDocxWindow):
    def __init__(self, widget: QtWidgets.QDialog, main, context=None, number=None, path=None):
        super().__init__()
        self.widget = widget
        self.main = main
        self.number = number
        self.path = path
        self.dbm = DatabaseModel()
        self.setupUi(widget)
        self.connectUi()
        self.loadServices()
        self.pushContext(context)

    def setupUi(self, widget):
        super().setupUi(widget)
        validator = QtGui.QDoubleValidator(0.0, 1.7976931348623157e+308, 2)
        validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        if self.path is not None:
            self.widget.setWindowTitle(f'Изменить контракт {self.number} - {self.path}')
            self.pb_create.setText('Изменить')
        self.widget.setMaximumHeight(self.widget.height())
        self.le_price.setValidator(validator)
        self.le_first_price.setValidator(validator)
        self.le_second_price.setValidator(validator)
        self.pb_create.setDefault(True)
        self.de_contract_date.setDate(QtCore.QDate.currentDate())
        self.de_contract_end_date.setDate(QtCore.QDate.currentDate())
        self.widget.focusWidget()

    def connectUi(self):
        self.cmb_service.currentTextChanged.connect(self.cmb_text_changed)
        self.cb_part_price.stateChanged.connect(lambda state: self.toggle_part_price(state == 2))
        self.cb_agent.stateChanged.connect(lambda state: self.toggle_agent(state == 2))
        self.le_company.textChanged.connect(lambda: self.le_company.setText(self.le_company.text().title()))
        self.le_agent.textChanged.connect(lambda: self.le_agent.setText(self.le_agent.text().title()))
        self.le_price.textChanged.connect(self.price_changed)
        self.le_first_price.textChanged.connect(self.first_price_changed)
        self.pb_clear.clicked.connect(self.clear_all)
        self.pb_create.clicked.connect(self.create_contract)

    def loadServices(self):
        for service in self.dbm.services.get_all():
            self.cmb_service.addItem(str(service))
        self.cmb_service.setCurrentText('')

    def pushContext(self, context):
        if context is not None:
            context = [field if field != '-' else '' for field in context]
            self.cmb_service.setCurrentText(context[0])
            self.cmb_text_changed()
            self.le_company.setText(context[1])
            self.de_contract_date.setDate(QtCore.QDate.fromString(context[2], 'dd.MM.yyyy'))
            if context[3] != context[1]:
                self.cb_agent.setChecked(True)
                self.le_agent.setText(context[3])
            self.le_phone.setText(context[4])
            passport = [field if field != '-' else '' for field in re.split(' от |, к/п |, ', context[5])]
            self.le_passport_code.setText(passport[0] if passport[0] else '')
            self.de_passport_issue_date.setDate(QtCore.QDate.fromString(passport[1], 'dd.MM.yyyy'))
            self.le_passport_kp.setText(passport[2] if passport[2] else '')
            self.pte_passport_issue_place.setPlainText(passport[3] if passport[3] else '')
            self.de_birthday.setDate(QtCore.QDate.fromString(context[6], 'dd.MM.yyyy'))
            self.le_price.setText(context[7])
            self.cb_part_price.setChecked(context[8].isdecimal())
            self.le_first_price.setText(context[8])
            self.de_contract_end_date.setDate(QtCore.QDate.fromString(context[10], 'dd.MM.yyyy'))

    def create_contract(self):
        if self.le_company.text() == '' or self.le_price.text() == '' or (self.cb_part_price.isChecked() and self.le_first_price.text() == '') or (self.cb_agent.isChecked() and self.le_agent.text() == '') or self.le_phone.text() == '8 ()  ' or self.le_passport_code.text() == '  ' or self.le_passport_kp.text() == '-' or self.pte_passport_issue_place.toPlainText() == '' or self.cmb_service.currentText() == '':
            if empty_fields() != 1: return
        if self.path is None:
            dialog = QtWidgets.QFileDialog.getSaveFileName(self, f'Создать контракт', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
            number = str(self.dbm.contracts.get_number())
            contract_action = self.dbm.contracts.add
            table_action = self.main.add_contract
        else:
            dialog = self.path
            number = self.number
            contract_action = self.dbm.contracts.update
            table_action = self.main.update_contract
            message = ask_for_save()
            if message == 0: return
            if message == 2:
                dialog = QtWidgets.QFileDialog.getOpenFileName(self, f'Выберите новый путь для контракта {self.number}', documents_path, 'Документ Microsoft Word (*.docx)')[0].replace('/', '\\')
        if dialog != '':
            data = [
                number,
                self.cmb_service.currentText(),
                self.le_company.text(),
                self.de_contract_date.date().toString('dd.MM.yyyy'),
                self.le_agent.text() if self.cb_agent.isChecked() and self.le_agent.text() != '' else self.le_company.text(),
                self.le_phone.text() if self.le_phone.text() != '8 ()  ' else '',
                (self.le_passport_code.text() if self.le_passport_code.text() != '  ' else '-') + ' от ' + self.de_passport_issue_date.date().toString('dd.MM.yyyy') + ', к/п ' + (self.le_passport_kp.text() if self.le_passport_kp.text() != '' else '-') + ', ' + (self.pte_passport_issue_place.toPlainText() if self.pte_passport_issue_place.toPlainText() != '' else '-'),
                self.de_birthday.date().toString('dd.MM.yyyy'),
                self.le_price.text(),
                self.le_first_price.text() if self.cb_part_price.isChecked() else '',
                self.le_second_price.text() if self.cb_part_price.isChecked() else '',
                self.de_contract_end_date.date().toString('dd.MM.yyyy'),
                dialog.rsplit('\\', 1)[-1][:-5],
                dialog
            ]
            tpl = 1 if self.cb_part_price.isChecked() else 2
            docx = docxtpl.DocxTemplate(os.path.abspath(f'templates/contract{tpl}_tpl.docx'))
            docx.render({
                'service': data[1],
                'company_1': data[2], 'company_2': data[1] if data[2] == '' else data[4], 'company_3': data[2],
                'date_1': data[3], 'date_2': data[3],
                'date_full_1': full_date(self.de_contract_date.date().toPython()), 'date_full_2': full_date(self.de_contract_date.date().toPython()), 'date_full_3': full_date(self.de_contract_date.date().toPython()), 'date_full_4': full_date(self.de_contract_date.date().toPython()),
                'agent_1': short_name(data[4]), 'agent_2': short_name(data[4]), 'agent_3': short_name(data[4]), 'agent_4': short_name(data[4]), 'agent_5': short_name(data[4]),
                'phone': data[5],
                'passport_code': self.le_passport_code.text(), 'passport_date': self.de_passport_issue_date.date().toString('dd.MM.yyyy'), 'passport_kp': self.le_passport_kp.text(), 'passport_issue': self.pte_passport_issue_place.toPlainText(),
                'birthday': data[7],
                'price': data[8], 'first_price': data[9], 'second_price': data[10],
                'date_end': full_date(self.de_contract_end_date.date().toPython())
            })
            try:
                docx.save(dialog)
            except PermissionError:
                file_permission_denied()
            else:
                contract_action(data)
                table_action(data)
                self.widget.close()
                self.widget.destroy()

    def clear_all(self):
        self.cb_part_price.setChecked(False)
        self.cb_agent.setChecked(False)
        self.cmb_service.setCurrentText('')
        self.le_company.setText('')
        self.le_price.setText('')
        self.le_first_price.setText('')
        self.le_second_price.setText('')
        self.le_second_price.setStyleSheet('')
        self.le_phone.setText('')
        self.le_passport_code.setText('')
        self.le_passport_kp.setText('')
        self.pte_passport_issue_place.setPlainText('')
        self.de_birthday.setDate(QtCore.QDate(1970, 1, 1))
        self.de_passport_issue_date.setDate(QtCore.QDate(2020, 1, 1))
        self.setupUi(self)

    def toggle_part_price(self, state):
        self.le_first_price.setEnabled(state)
        self.le_second_price.setEnabled(state)
        self.l_contract_end_date.setEnabled(state)
        self.de_contract_end_date.setEnabled(state)

    def toggle_agent(self, state):
        self.le_agent.setEnabled(state)
        self.l_requisites.setText(f'Реквизиты {"представителя" if state else "заказчика"}')

    def refresh_services(self):
        current_text = self.cmb_service.currentText()
        self.cmb_service.clear()
        for service in self.dbm.services.get_all():
            self.cmb_service.addItem(str(service))
        self.cmb_service.setCurrentText(current_text)
        self.cmb_text_changed()

    def add_service(self):
        self.dbm.services.add(self.cmb_service.currentText())
        self.refresh_services()

    def delete_service(self):
        self.dbm.services.delete(self.cmb_service.currentText())
        self.refresh_services()

    def cmb_text_changed(self):
        if self.cmb_service.currentText() == '':
            self.pb_toggle_service.setEnabled(False)
        else:
            self.pb_toggle_service.setEnabled(True)
            while True:
                try: self.pb_toggle_service.clicked.disconnect(self.add_service)
                except: break
            while True:
                try: self.pb_toggle_service.clicked.disconnect(self.delete_service)
                except: break
            if self.cmb_service.currentText() not in [self.cmb_service.itemText(index) for index in range(self.cmb_service.count())]:
                self.pb_toggle_service.setIcon(QtGui.QIcon(":/icons/icons/plus.ico"))
                self.pb_toggle_service.clicked.connect(self.add_service)
            else:
                self.pb_toggle_service.setIcon(QtGui.QIcon(":/icons/icons/minus.ico"))
                self.pb_toggle_service.clicked.connect(self.delete_service)

    def correct_second_price(self):
        second_price = float(self.le_price.text().replace(',', '.')) - float(self.le_first_price.text().replace(',', '.'))
        if second_price < 0:
            self.le_second_price.setStyleSheet('color: red;')
        else:
            self.le_second_price.setStyleSheet('')
        second_price = str(second_price).split('.')
        if len(second_price) > 1:
            if second_price[1] == '' or second_price[1] == '0' or second_price[1] == '00':
                second_price.pop(1)
            else:
                second_price[1] = second_price[1][:2].ljust(2, '0')
        self.le_second_price.setText(','.join(second_price))

    def price_changed(self):
        if self.le_price.text() != '':
            validator = QtGui.QDoubleValidator(0.0, float(self.le_price.text().replace(',', '.')), 2)
            validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
            self.le_first_price.setValidator(validator)
            if self.le_first_price.text() != '':
                self.correct_second_price()
        else:
            self.le_second_price.setText('')

    def first_price_changed(self):
        if self.le_price.text() != '' and self.le_first_price.text() != '':
            self.correct_second_price()
        else:
            self.le_second_price.setText('')

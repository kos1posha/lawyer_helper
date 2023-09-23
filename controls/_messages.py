from PySide6 import QtWidgets, QtGui


class Result:
    def __init__(self):
        self.value = 0


def success(is_new):
    def click(button, r):
        r.value = 1 if button.text() == 'OK' else 0
    result = Result()
    checkbox = QtWidgets.QCheckBox('Выбрать новый путь для файла')
    message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information, 'Сообщение', ('Файл успешно сохранен.' if is_new else 'Изменения успешно сохранены.') + ' ' * 20)
    message.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/images/pngs/main-icon.png")))
    if not is_new: message.setCheckBox(checkbox)
    message.addButton(QtWidgets.QMessageBox.StandardButton.Ok)
    message.buttonClicked.connect(lambda button: click(button, result))
    message.exec()
    if result.value == 1:
        return 2 if checkbox.isChecked() else 1
    return 1


def ask_for_delete(info):
    def click(button, r):
        r.value = 1 if button.text() == 'Да' else 0
    result = Result()
    message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Warning, 'Сообщение', f'Вы уверены, что хотите удалить {info[0][1]} контракт? Данное действие нельзя отменить.')
    message.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/images/pngs/main-icon.png")))
    message.setInformativeText('\n'.join(f'{field[0]}: {field[1]}' for field in info))
    message.addButton('Да', QtWidgets.QMessageBox.ButtonRole.YesRole)
    message.addButton('Нет', QtWidgets.QMessageBox.ButtonRole.NoRole)
    message.buttonClicked.connect(lambda button: click(button, result))
    message.exec()
    return result.value


def ask_for_save():
    def click(button, r):
        r.value = 1 if button.text() == 'Да' else 0
    result = Result()
    checkbox = QtWidgets.QCheckBox('Выбрать новый путь для файла')
    message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Question, 'Сообщение', 'Сохранить изменения? Данное действие нельзя отменить.')
    message.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/images/pngs/main-icon.png")))
    message.setCheckBox(checkbox)
    message.addButton('Да', QtWidgets.QMessageBox.ButtonRole.YesRole)
    message.addButton('Отмена', QtWidgets.QMessageBox.ButtonRole.RejectRole)
    message.buttonClicked.connect(lambda button: click(button, result))
    message.exec()
    return (1 + checkbox.isChecked()) * result.value


# noinspection PyUnresolvedReferences
def path_doesnt_exists(path):
    def click(button, r):
        r.value = 1 if button.text() == 'OK' else 0
    result = Result()
    message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, 'Сообщение', f'Указанный файл не найден. Возможно он был удален или перемещен.\n\n{path}')
    message.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/images/pngs/main-icon.png")))
    message.setInformativeText('')
    message.setStandardButtons(QtWidgets.QMessageBox.StandardButton.NoButton)
    radio_layout = QtWidgets.QHBoxLayout()
    rb_new_path = QtWidgets.QRadioButton('Указать новый путь к файлу')
    rb_resurrect_file = QtWidgets.QRadioButton('Восстановить и сохранить')
    radio_layout.addWidget(rb_new_path)
    radio_layout.addWidget(rb_resurrect_file)
    message.findChild(QtWidgets.QGridLayout).addLayout(radio_layout, 1, 2)
    message.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    message.buttonClicked.connect(lambda button: click(button, result))
    message.exec()
    if result.value == 1:
        if rb_new_path.isChecked(): return 1
        elif rb_resurrect_file.isChecked(): return 2
    else: return 0


def file_permission_denied():
    message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, 'Сообщение', f'Запись данных невозможна, так как доступ к файлу запрещен.')
    message.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/images/pngs/main-icon.png")))
    message.setInformativeText('Если он открыт, закройте файл и повторите попытку.')
    message.addButton(QtWidgets.QMessageBox.StandardButton.Ok)
    message.exec()


def export_xlsx_success(path):
    def click(button, r):
        if button.text() == 'Открыть файл':
            r.value = 1
    result = Result()
    path = path.replace('/', '\\')
    message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information, 'Сообщение', f'Таблица успешно экспортирована в Excel.')
    message.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/images/pngs/main-icon.png")))
    message.setInformativeText(path)
    message.addButton('ОК', QtWidgets.QMessageBox.ButtonRole.ApplyRole)
    message.addButton('Открыть файл', QtWidgets.QMessageBox.ButtonRole.HelpRole)
    message.buttonClicked.connect(lambda button: click(button, result))
    message.exec()
    return result.value


def empty_fields():
    def click(button, r):
        r.value = 1 if button.text() == 'Да' else 0
    result = Result()
    message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Warning, 'Сообщение', f'В форме остались пустые поля. Продолжить?')
    message.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/images/pngs/main-icon.png")))
    message.addButton('Да', QtWidgets.QMessageBox.ButtonRole.YesRole)
    message.addButton('Отмена', QtWidgets.QMessageBox.ButtonRole.NoRole)
    message.buttonClicked.connect(lambda button: click(button, result))
    message.exec()
    return result.value


def not_implemented_yet():
    message = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, 'exception 501', f'not implemented yet', QtWidgets.QMessageBox.StandardButton.Ok)
    message.exec()

import os, subprocess
from number_to_string import get_string_by_number

from PySide6 import QtWidgets, QtGui

from controls._messages import file_permission_denied
from controls.word_preview_control import WordPreviewControl


def month(m):
    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    return months[m - 1]


def full_date(date):
    day = date.strftime('%d').lstrip('0')
    return date.strftime(f'{day} {month(date.month)} %Y г.')


def short_name(name):
    return ' '.join([n[0] + '.' if i > 0 else n for i, n in enumerate(name.split())])


def get_price_text(price):
    return get_string_by_number(float(price.replace(',', '.'))).replace('  ', ' ') if price != '' else ''


def open_explorer(action, path):
    if path is not None:
        if os.path.exists(path):
            try:
                s, bs = '/', '\\'
                subprocess.Popen(f'explorer /{action}, "{path.replace(s, bs)}"')
                return 1
            except PermissionError:
                file_permission_denied()
                return -1
        else:
            return 0


def open_file(path, t=None):
    return open_explorer('open', path)


def open_folder(path, t=None):
    return open_explorer('select', path)


def preview_word(path, t='main'):
    if path is not None:
        if os.path.exists(path):
            try:
                dialog = QtWidgets.QDialog(f=QtGui.Qt.WindowType.Window)
                WordPreviewControl(dialog, path, t)
                dialog.exec()
                return 1
            except PermissionError:
                file_permission_denied()
                return -1
        else:
            return 0

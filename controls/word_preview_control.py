import os, random, win32com.client

from PySide6 import QtWidgets, QtCore

from views.word_preview_window import Ui_WordPreviewWindow


class WordPreviewControl(QtWidgets.QMainWindow, Ui_WordPreviewWindow):
    def __init__(self, widget: QtWidgets.QDialog, path: str, t: str):
        super().__init__()
        super().setupUi(widget)
        self.widget = widget
        self.docx = path
        self.type = t
        self.setupUi(widget)

    def setupUi(self, widget):
        widget.setWindowTitle(QtCore.QCoreApplication.translate('WordPreviewWindow', self.docx, None))
        if self.type == 'main':
            self.widget.setGeometry(self.widget.x(), self.widget.y(), 800, self.widget.height())
            self.te_docx_html_preview.setMaximumHeight(7800)
        elif self.type == 'af':
            self.widget.setGeometry(self.widget.x(), self.widget.y(), 880, self.widget.height())
            self.te_docx_html_preview.setMinimumHeight(1200)
        elif self.type == 'coef':
            self.widget.setGeometry(self.widget.x(), self.widget.y(), 960, self.widget.height())
            self.te_docx_html_preview.setMinimumHeight(1050)
        elif self.type == 'corf':
            self.widget.setGeometry(self.widget.x(), self.widget.y(), 960, self.widget.height())
            self.te_docx_html_preview.setMinimumHeight(1050)
        self.te_docx_html_preview.setHtml(self.get_html(self.docx))

    def get_html(self, path):
        word = win32com.client.gencache.EnsureDispatch('Word.Application')
        docx = word.Documents.Open(path)
        temp_path = os.getcwd() + f'\\~preview_{random.randint(1000, 9999)}.html'
        docx.SaveAs(temp_path, 10)
        with open(temp_path) as temp_file:
            html = temp_file.read()
        docx.Close()
        word.Quit()
        os.remove(temp_path)
        return html

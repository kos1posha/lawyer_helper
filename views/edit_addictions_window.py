# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditAddictionsWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_EditAddictionsWindow(object):
    def setupUi(self, EditAddictionsWindow):
        if not EditAddictionsWindow.objectName():
            EditAddictionsWindow.setObjectName(u"EditAddictionsWindow")
        EditAddictionsWindow.resize(626, 438)
        icon = QIcon()
        icon.addFile(u":/images/pngs/main-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        EditAddictionsWindow.setWindowIcon(icon)
        self.vl_main = QVBoxLayout(EditAddictionsWindow)
        self.vl_main.setSpacing(3)
        self.vl_main.setObjectName(u"vl_main")
        self.l_contract_number = QLabel(EditAddictionsWindow)
        self.l_contract_number.setObjectName(u"l_contract_number")

        self.vl_main.addWidget(self.l_contract_number)

        self.l_contract_service = QLabel(EditAddictionsWindow)
        self.l_contract_service.setObjectName(u"l_contract_service")

        self.vl_main.addWidget(self.l_contract_service)

        self.l_contract_price = QLabel(EditAddictionsWindow)
        self.l_contract_price.setObjectName(u"l_contract_price")

        self.vl_main.addWidget(self.l_contract_price)

        self.l_contract_path = QLabel(EditAddictionsWindow)
        self.l_contract_path.setObjectName(u"l_contract_path")

        self.vl_main.addWidget(self.l_contract_path)

        self.tw_addictions = QTabWidget(EditAddictionsWindow)
        self.tw_addictions.setObjectName(u"tw_addictions")
        self.t_act_form = QWidget()
        self.t_act_form.setObjectName(u"t_act_form")
        self.t_act_form.setEnabled(True)
        self.gl_af = QGridLayout(self.t_act_form)
        self.gl_af.setObjectName(u"gl_af")
        self.gl_af.setSizeConstraint(QLayout.SetNoConstraint)
        self.w_af_actions = QWidget(self.t_act_form)
        self.w_af_actions.setObjectName(u"w_af_actions")
        self.w_af_actions.setMinimumSize(QSize(0, 35))
        self.w_af_actions.setMaximumSize(QSize(16777215, 35))
        self.gl_af_actions = QGridLayout(self.w_af_actions)
        self.gl_af_actions.setSpacing(3)
        self.gl_af_actions.setObjectName(u"gl_af_actions")
        self.gl_af_actions.setContentsMargins(0, 0, 0, 0)
        self.pb_af_save = QPushButton(self.w_af_actions)
        self.pb_af_save.setObjectName(u"pb_af_save")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_af_save.sizePolicy().hasHeightForWidth())
        self.pb_af_save.setSizePolicy(sizePolicy)
        self.pb_af_save.setMinimumSize(QSize(35, 35))
        self.pb_af_save.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/save-button.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_af_save.setIcon(icon1)
        self.pb_af_save.setIconSize(QSize(22, 22))

        self.gl_af_actions.addWidget(self.pb_af_save, 3, 1, 1, 1)

        self.line_af_1 = QFrame(self.w_af_actions)
        self.line_af_1.setObjectName(u"line_af_1")
        sizePolicy.setHeightForWidth(self.line_af_1.sizePolicy().hasHeightForWidth())
        self.line_af_1.setSizePolicy(sizePolicy)
        self.line_af_1.setMinimumSize(QSize(0, 35))
        self.line_af_1.setFrameShape(QFrame.VLine)
        self.line_af_1.setFrameShadow(QFrame.Sunken)

        self.gl_af_actions.addWidget(self.line_af_1, 3, 2, 1, 1)

        self.line_af_2 = QFrame(self.w_af_actions)
        self.line_af_2.setObjectName(u"line_af_2")
        sizePolicy.setHeightForWidth(self.line_af_2.sizePolicy().hasHeightForWidth())
        self.line_af_2.setSizePolicy(sizePolicy)
        self.line_af_2.setMinimumSize(QSize(0, 35))
        self.line_af_2.setFrameShape(QFrame.VLine)
        self.line_af_2.setFrameShadow(QFrame.Sunken)

        self.gl_af_actions.addWidget(self.line_af_2, 3, 5, 1, 1)

        self.pb_af_open_file = QPushButton(self.w_af_actions)
        self.pb_af_open_file.setObjectName(u"pb_af_open_file")
        self.pb_af_open_file.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_af_open_file.sizePolicy().hasHeightForWidth())
        self.pb_af_open_file.setSizePolicy(sizePolicy)
        self.pb_af_open_file.setMinimumSize(QSize(35, 35))
        self.pb_af_open_file.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/open-file.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_af_open_file.setIcon(icon2)
        self.pb_af_open_file.setIconSize(QSize(20, 20))

        self.gl_af_actions.addWidget(self.pb_af_open_file, 3, 3, 1, 1)

        self.pb_af_docx = QPushButton(self.w_af_actions)
        self.pb_af_docx.setObjectName(u"pb_af_docx")
        self.pb_af_docx.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_af_docx.sizePolicy().hasHeightForWidth())
        self.pb_af_docx.setSizePolicy(sizePolicy)
        self.pb_af_docx.setMinimumSize(QSize(35, 35))
        self.pb_af_docx.setMaximumSize(QSize(35, 35))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/eye.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_af_docx.setIcon(icon3)
        self.pb_af_docx.setIconSize(QSize(20, 20))

        self.gl_af_actions.addWidget(self.pb_af_docx, 3, 6, 1, 1)

        self.vl_af_title = QVBoxLayout()
        self.vl_af_title.setSpacing(2)
        self.vl_af_title.setObjectName(u"vl_af_title")
        self.vl_af_title.setContentsMargins(-1, 2, -1, -1)
        self.l_af = QLabel(self.w_af_actions)
        self.l_af.setObjectName(u"l_af")
        font = QFont()
        font.setPointSize(9)
        self.l_af.setFont(font)

        self.vl_af_title.addWidget(self.l_af)

        self.l_af_path = QLabel(self.w_af_actions)
        self.l_af_path.setObjectName(u"l_af_path")

        self.vl_af_title.addWidget(self.l_af_path)


        self.gl_af_actions.addLayout(self.vl_af_title, 3, 0, 1, 1)

        self.pb_af_open_folder = QPushButton(self.w_af_actions)
        self.pb_af_open_folder.setObjectName(u"pb_af_open_folder")
        self.pb_af_open_folder.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_af_open_folder.sizePolicy().hasHeightForWidth())
        self.pb_af_open_folder.setSizePolicy(sizePolicy)
        self.pb_af_open_folder.setMinimumSize(QSize(35, 35))
        self.pb_af_open_folder.setMaximumSize(QSize(35, 35))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/open-folder.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_af_open_folder.setIcon(icon4)
        self.pb_af_open_folder.setIconSize(QSize(24, 24))

        self.gl_af_actions.addWidget(self.pb_af_open_folder, 3, 4, 1, 1)


        self.gl_af.addWidget(self.w_af_actions, 1, 0, 1, 2)

        self.vs_af = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gl_af.addItem(self.vs_af, 5, 0, 1, 2)

        self.w_af = QWidget(self.t_act_form)
        self.w_af.setObjectName(u"w_af")
        self.w_af.setAcceptDrops(True)
        self.gl_w_af = QGridLayout(self.w_af)
        self.gl_w_af.setSpacing(6)
        self.gl_w_af.setObjectName(u"gl_w_af")
        self.gl_w_af.setContentsMargins(0, 0, 0, 0)
        self.l_af_price = QLabel(self.w_af)
        self.l_af_price.setObjectName(u"l_af_price")

        self.gl_w_af.addWidget(self.l_af_price, 3, 0, 1, 1)

        self.le_af_price = QLineEdit(self.w_af)
        self.le_af_price.setObjectName(u"le_af_price")
        self.le_af_price.setMinimumSize(QSize(0, 22))
        self.le_af_price.setMaximumSize(QSize(16777215, 22))
        self.le_af_price.setMouseTracking(False)
        self.le_af_price.setClearButtonEnabled(True)

        self.gl_w_af.addWidget(self.le_af_price, 4, 0, 1, 1)

        self.l_af_price_text = QLabel(self.w_af)
        self.l_af_price_text.setObjectName(u"l_af_price_text")

        self.gl_w_af.addWidget(self.l_af_price_text, 3, 1, 1, 1)

        self.de_af_date = QDateEdit(self.w_af)
        self.de_af_date.setObjectName(u"de_af_date")
        self.de_af_date.setMinimumSize(QSize(0, 22))
        self.de_af_date.setMaximumSize(QSize(16777215, 22))
        self.de_af_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_af_date.setDateTime(QDateTime(QDate(1970, 1, 1), QTime(0, 0, 0)))
        self.de_af_date.setCalendarPopup(True)

        self.gl_w_af.addWidget(self.de_af_date, 2, 1, 1, 1)

        self.l_af_agent = QLabel(self.w_af)
        self.l_af_agent.setObjectName(u"l_af_agent")

        self.gl_w_af.addWidget(self.l_af_agent, 1, 0, 1, 1)

        self.le_af_agent = QLineEdit(self.w_af)
        self.le_af_agent.setObjectName(u"le_af_agent")
        self.le_af_agent.setMinimumSize(QSize(0, 22))
        self.le_af_agent.setMaximumSize(QSize(16777215, 22))
        self.le_af_agent.setMouseTracking(False)
        self.le_af_agent.setClearButtonEnabled(True)

        self.gl_w_af.addWidget(self.le_af_agent, 2, 0, 1, 1)

        self.le_af_price_text = QLineEdit(self.w_af)
        self.le_af_price_text.setObjectName(u"le_af_price_text")
        self.le_af_price_text.setMinimumSize(QSize(0, 22))
        self.le_af_price_text.setMaximumSize(QSize(16777215, 22))
        self.le_af_price_text.setMouseTracking(False)
        self.le_af_price_text.setReadOnly(True)
        self.le_af_price_text.setClearButtonEnabled(True)

        self.gl_w_af.addWidget(self.le_af_price_text, 4, 1, 1, 1)

        self.l_af_date = QLabel(self.w_af)
        self.l_af_date.setObjectName(u"l_af_date")

        self.gl_w_af.addWidget(self.l_af_date, 1, 1, 1, 1)

        self.le_af_company = QLineEdit(self.w_af)
        self.le_af_company.setObjectName(u"le_af_company")
        self.le_af_company.setMinimumSize(QSize(0, 22))
        self.le_af_company.setMaximumSize(QSize(16777215, 22))
        self.le_af_company.setClearButtonEnabled(True)

        self.gl_w_af.addWidget(self.le_af_company, 9, 0, 1, 1)

        self.l_af_company = QLabel(self.w_af)
        self.l_af_company.setObjectName(u"l_af_company")

        self.gl_w_af.addWidget(self.l_af_company, 8, 0, 1, 1)

        self.w_af_services = QWidget(self.w_af)
        self.w_af_services.setObjectName(u"w_af_services")
        self.hl_act_services = QHBoxLayout(self.w_af_services)
        self.hl_act_services.setSpacing(3)
        self.hl_act_services.setObjectName(u"hl_act_services")
        self.hl_act_services.setContentsMargins(0, 0, 0, 0)
        self.cmb_af_service = QComboBox(self.w_af_services)
        self.cmb_af_service.setObjectName(u"cmb_af_service")
        self.cmb_af_service.setMinimumSize(QSize(0, 22))
        self.cmb_af_service.setMaximumSize(QSize(16777215, 22))
        self.cmb_af_service.setEditable(True)
        self.cmb_af_service.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.cmb_af_service.setDuplicatesEnabled(False)

        self.hl_act_services.addWidget(self.cmb_af_service)

        self.pb_af_toggle_service = QPushButton(self.w_af_services)
        self.pb_af_toggle_service.setObjectName(u"pb_af_toggle_service")
        self.pb_af_toggle_service.setMinimumSize(QSize(22, 22))
        self.pb_af_toggle_service.setMaximumSize(QSize(22, 22))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/plus.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_af_toggle_service.setIcon(icon5)
        self.pb_af_toggle_service.setIconSize(QSize(10, 10))

        self.hl_act_services.addWidget(self.pb_af_toggle_service)


        self.gl_w_af.addWidget(self.w_af_services, 6, 0, 1, 1)

        self.l_af_service = QLabel(self.w_af)
        self.l_af_service.setObjectName(u"l_af_service")
        self.l_af_service.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gl_w_af.addWidget(self.l_af_service, 5, 0, 1, 1)


        self.gl_af.addWidget(self.w_af, 2, 0, 1, 2)

        self.tw_addictions.addTab(self.t_act_form, "")
        self.t_cash_order_expense_form = QWidget()
        self.t_cash_order_expense_form.setObjectName(u"t_cash_order_expense_form")
        self.t_cash_order_expense_form.setEnabled(True)
        self.gl_coef = QGridLayout(self.t_cash_order_expense_form)
        self.gl_coef.setObjectName(u"gl_coef")
        self.vs_coef = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gl_coef.addItem(self.vs_coef, 3, 0, 1, 2)

        self.w_coef = QWidget(self.t_cash_order_expense_form)
        self.w_coef.setObjectName(u"w_coef")
        self.gl_w_coef = QGridLayout(self.w_coef)
        self.gl_w_coef.setSpacing(6)
        self.gl_w_coef.setObjectName(u"gl_w_coef")
        self.gl_w_coef.setContentsMargins(0, 0, 0, 0)
        self.w_coef_services = QWidget(self.w_coef)
        self.w_coef_services.setObjectName(u"w_coef_services")
        self.hl_coef_services = QHBoxLayout(self.w_coef_services)
        self.hl_coef_services.setSpacing(3)
        self.hl_coef_services.setObjectName(u"hl_coef_services")
        self.hl_coef_services.setContentsMargins(0, 0, 0, 0)
        self.cmb_coef_service = QComboBox(self.w_coef_services)
        self.cmb_coef_service.setObjectName(u"cmb_coef_service")
        self.cmb_coef_service.setMinimumSize(QSize(0, 22))
        self.cmb_coef_service.setMaximumSize(QSize(16777215, 22))
        self.cmb_coef_service.setEditable(True)
        self.cmb_coef_service.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.cmb_coef_service.setDuplicatesEnabled(False)

        self.hl_coef_services.addWidget(self.cmb_coef_service)

        self.pb_coef_toggle_service = QPushButton(self.w_coef_services)
        self.pb_coef_toggle_service.setObjectName(u"pb_coef_toggle_service")
        self.pb_coef_toggle_service.setMinimumSize(QSize(22, 22))
        self.pb_coef_toggle_service.setMaximumSize(QSize(22, 22))
        self.pb_coef_toggle_service.setIcon(icon5)
        self.pb_coef_toggle_service.setIconSize(QSize(10, 10))

        self.hl_coef_services.addWidget(self.pb_coef_toggle_service)


        self.gl_w_coef.addWidget(self.w_coef_services, 8, 0, 1, 1)

        self.le_coef_document_code = QLineEdit(self.w_coef)
        self.le_coef_document_code.setObjectName(u"le_coef_document_code")
        self.le_coef_document_code.setMinimumSize(QSize(0, 22))
        self.le_coef_document_code.setMaximumSize(QSize(16777215, 22))
        self.le_coef_document_code.setClearButtonEnabled(True)

        self.gl_w_coef.addWidget(self.le_coef_document_code, 10, 1, 1, 1)

        self.l_coef_document_issue_date = QLabel(self.w_coef)
        self.l_coef_document_issue_date.setObjectName(u"l_coef_document_issue_date")

        self.gl_w_coef.addWidget(self.l_coef_document_issue_date, 11, 0, 1, 1)

        self.l_coef_addiction = QLabel(self.w_coef)
        self.l_coef_addiction.setObjectName(u"l_coef_addiction")

        self.gl_w_coef.addWidget(self.l_coef_addiction, 13, 0, 1, 2)

        self.pte_coef_addiction = QPlainTextEdit(self.w_coef)
        self.pte_coef_addiction.setObjectName(u"pte_coef_addiction")
        self.pte_coef_addiction.setMinimumSize(QSize(0, 50))
        self.pte_coef_addiction.setMaximumSize(QSize(16777215, 50))
        self.pte_coef_addiction.setTabChangesFocus(True)

        self.gl_w_coef.addWidget(self.pte_coef_addiction, 14, 0, 1, 2)

        self.de_coef_date = QDateEdit(self.w_coef)
        self.de_coef_date.setObjectName(u"de_coef_date")
        self.de_coef_date.setMinimumSize(QSize(0, 22))
        self.de_coef_date.setMaximumSize(QSize(16777215, 22))
        self.de_coef_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_coef_date.setDateTime(QDateTime(QDate(1970, 1, 1), QTime(0, 0, 0)))
        self.de_coef_date.setCalendarPopup(True)

        self.gl_w_coef.addWidget(self.de_coef_date, 3, 1, 1, 1)

        self.de_coef_document_issue_date = QDateEdit(self.w_coef)
        self.de_coef_document_issue_date.setObjectName(u"de_coef_document_issue_date")
        self.de_coef_document_issue_date.setMinimumSize(QSize(0, 22))
        self.de_coef_document_issue_date.setMaximumSize(QSize(16777215, 22))
        self.de_coef_document_issue_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_coef_document_issue_date.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.de_coef_document_issue_date.setCalendarPopup(True)

        self.gl_w_coef.addWidget(self.de_coef_document_issue_date, 12, 0, 1, 1)

        self.le_coef_document = QLineEdit(self.w_coef)
        self.le_coef_document.setObjectName(u"le_coef_document")
        self.le_coef_document.setMinimumSize(QSize(0, 22))
        self.le_coef_document.setMaximumSize(QSize(16777215, 22))
        self.le_coef_document.setClearButtonEnabled(True)

        self.gl_w_coef.addWidget(self.le_coef_document, 10, 0, 1, 1)

        self.l_coef_price = QLabel(self.w_coef)
        self.l_coef_price.setObjectName(u"l_coef_price")

        self.gl_w_coef.addWidget(self.l_coef_price, 5, 0, 1, 1)

        self.l_coef_price_text = QLabel(self.w_coef)
        self.l_coef_price_text.setObjectName(u"l_coef_price_text")

        self.gl_w_coef.addWidget(self.l_coef_price_text, 5, 1, 1, 1)

        self.le_coef_agent = QLineEdit(self.w_coef)
        self.le_coef_agent.setObjectName(u"le_coef_agent")
        self.le_coef_agent.setMinimumSize(QSize(0, 22))
        self.le_coef_agent.setMaximumSize(QSize(16777215, 22))
        self.le_coef_agent.setClearButtonEnabled(True)

        self.gl_w_coef.addWidget(self.le_coef_agent, 3, 0, 1, 1)

        self.l_coef_document_code = QLabel(self.w_coef)
        self.l_coef_document_code.setObjectName(u"l_coef_document_code")

        self.gl_w_coef.addWidget(self.l_coef_document_code, 9, 1, 1, 1)

        self.le_coef_price = QLineEdit(self.w_coef)
        self.le_coef_price.setObjectName(u"le_coef_price")
        self.le_coef_price.setMinimumSize(QSize(0, 22))
        self.le_coef_price.setMaximumSize(QSize(16777215, 22))
        self.le_coef_price.setClearButtonEnabled(True)

        self.gl_w_coef.addWidget(self.le_coef_price, 6, 0, 1, 1)

        self.l_coef_service = QLabel(self.w_coef)
        self.l_coef_service.setObjectName(u"l_coef_service")
        self.l_coef_service.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gl_w_coef.addWidget(self.l_coef_service, 7, 0, 1, 1)

        self.le_coef_price_text = QLineEdit(self.w_coef)
        self.le_coef_price_text.setObjectName(u"le_coef_price_text")
        self.le_coef_price_text.setMinimumSize(QSize(0, 22))
        self.le_coef_price_text.setMaximumSize(QSize(16777215, 22))
        self.le_coef_price_text.setReadOnly(True)
        self.le_coef_price_text.setClearButtonEnabled(True)

        self.gl_w_coef.addWidget(self.le_coef_price_text, 6, 1, 1, 1)

        self.l_coef_document_issue_place = QLabel(self.w_coef)
        self.l_coef_document_issue_place.setObjectName(u"l_coef_document_issue_place")

        self.gl_w_coef.addWidget(self.l_coef_document_issue_place, 11, 1, 1, 1)

        self.l_coef_document = QLabel(self.w_coef)
        self.l_coef_document.setObjectName(u"l_coef_document")

        self.gl_w_coef.addWidget(self.l_coef_document, 9, 0, 1, 1)

        self.le_coef_document_issue_place = QLineEdit(self.w_coef)
        self.le_coef_document_issue_place.setObjectName(u"le_coef_document_issue_place")
        self.le_coef_document_issue_place.setMinimumSize(QSize(0, 22))
        self.le_coef_document_issue_place.setMaximumSize(QSize(16777215, 22))
        self.le_coef_document_issue_place.setClearButtonEnabled(True)

        self.gl_w_coef.addWidget(self.le_coef_document_issue_place, 12, 1, 1, 1)

        self.l_coef_date = QLabel(self.w_coef)
        self.l_coef_date.setObjectName(u"l_coef_date")

        self.gl_w_coef.addWidget(self.l_coef_date, 2, 1, 1, 1)

        self.l_coef_agent = QLabel(self.w_coef)
        self.l_coef_agent.setObjectName(u"l_coef_agent")

        self.gl_w_coef.addWidget(self.l_coef_agent, 2, 0, 1, 1)


        self.gl_coef.addWidget(self.w_coef, 1, 0, 1, 2)

        self.w_coef_actions = QWidget(self.t_cash_order_expense_form)
        self.w_coef_actions.setObjectName(u"w_coef_actions")
        self.w_coef_actions.setMinimumSize(QSize(0, 35))
        self.w_coef_actions.setMaximumSize(QSize(16777215, 35))
        self.gl_coef_actions = QGridLayout(self.w_coef_actions)
        self.gl_coef_actions.setSpacing(3)
        self.gl_coef_actions.setObjectName(u"gl_coef_actions")
        self.gl_coef_actions.setContentsMargins(0, 0, 0, 0)
        self.pb_coef_open_file = QPushButton(self.w_coef_actions)
        self.pb_coef_open_file.setObjectName(u"pb_coef_open_file")
        self.pb_coef_open_file.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_coef_open_file.sizePolicy().hasHeightForWidth())
        self.pb_coef_open_file.setSizePolicy(sizePolicy)
        self.pb_coef_open_file.setMinimumSize(QSize(35, 35))
        self.pb_coef_open_file.setMaximumSize(QSize(35, 35))
        self.pb_coef_open_file.setIcon(icon2)
        self.pb_coef_open_file.setIconSize(QSize(20, 20))

        self.gl_coef_actions.addWidget(self.pb_coef_open_file, 3, 3, 1, 1)

        self.pb_coef_save = QPushButton(self.w_coef_actions)
        self.pb_coef_save.setObjectName(u"pb_coef_save")
        sizePolicy.setHeightForWidth(self.pb_coef_save.sizePolicy().hasHeightForWidth())
        self.pb_coef_save.setSizePolicy(sizePolicy)
        self.pb_coef_save.setMinimumSize(QSize(35, 35))
        self.pb_coef_save.setMaximumSize(QSize(35, 35))
        self.pb_coef_save.setIcon(icon1)
        self.pb_coef_save.setIconSize(QSize(22, 22))

        self.gl_coef_actions.addWidget(self.pb_coef_save, 3, 1, 1, 1)

        self.line_coef_1 = QFrame(self.w_coef_actions)
        self.line_coef_1.setObjectName(u"line_coef_1")
        sizePolicy.setHeightForWidth(self.line_coef_1.sizePolicy().hasHeightForWidth())
        self.line_coef_1.setSizePolicy(sizePolicy)
        self.line_coef_1.setMinimumSize(QSize(0, 35))
        self.line_coef_1.setFrameShape(QFrame.VLine)
        self.line_coef_1.setFrameShadow(QFrame.Sunken)

        self.gl_coef_actions.addWidget(self.line_coef_1, 3, 2, 1, 1)

        self.pb_coef_open_folder = QPushButton(self.w_coef_actions)
        self.pb_coef_open_folder.setObjectName(u"pb_coef_open_folder")
        self.pb_coef_open_folder.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_coef_open_folder.sizePolicy().hasHeightForWidth())
        self.pb_coef_open_folder.setSizePolicy(sizePolicy)
        self.pb_coef_open_folder.setMinimumSize(QSize(35, 35))
        self.pb_coef_open_folder.setMaximumSize(QSize(35, 35))
        self.pb_coef_open_folder.setIcon(icon4)
        self.pb_coef_open_folder.setIconSize(QSize(24, 24))

        self.gl_coef_actions.addWidget(self.pb_coef_open_folder, 3, 4, 1, 1)

        self.pb_coef_docx = QPushButton(self.w_coef_actions)
        self.pb_coef_docx.setObjectName(u"pb_coef_docx")
        self.pb_coef_docx.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_coef_docx.sizePolicy().hasHeightForWidth())
        self.pb_coef_docx.setSizePolicy(sizePolicy)
        self.pb_coef_docx.setMinimumSize(QSize(35, 35))
        self.pb_coef_docx.setMaximumSize(QSize(35, 35))
        self.pb_coef_docx.setIcon(icon3)
        self.pb_coef_docx.setIconSize(QSize(20, 20))

        self.gl_coef_actions.addWidget(self.pb_coef_docx, 3, 6, 1, 1)

        self.line_coef_2 = QFrame(self.w_coef_actions)
        self.line_coef_2.setObjectName(u"line_coef_2")
        sizePolicy.setHeightForWidth(self.line_coef_2.sizePolicy().hasHeightForWidth())
        self.line_coef_2.setSizePolicy(sizePolicy)
        self.line_coef_2.setMinimumSize(QSize(0, 35))
        self.line_coef_2.setFrameShape(QFrame.VLine)
        self.line_coef_2.setFrameShadow(QFrame.Sunken)

        self.gl_coef_actions.addWidget(self.line_coef_2, 3, 5, 1, 1)

        self.vl_coef_title = QVBoxLayout()
        self.vl_coef_title.setSpacing(2)
        self.vl_coef_title.setObjectName(u"vl_coef_title")
        self.vl_coef_title.setContentsMargins(-1, 2, -1, -1)
        self.l_coef = QLabel(self.w_coef_actions)
        self.l_coef.setObjectName(u"l_coef")
        self.l_coef.setFont(font)

        self.vl_coef_title.addWidget(self.l_coef)

        self.l_coef_path = QLabel(self.w_coef_actions)
        self.l_coef_path.setObjectName(u"l_coef_path")

        self.vl_coef_title.addWidget(self.l_coef_path)


        self.gl_coef_actions.addLayout(self.vl_coef_title, 3, 0, 1, 1)


        self.gl_coef.addWidget(self.w_coef_actions, 0, 0, 1, 2)

        self.tw_addictions.addTab(self.t_cash_order_expense_form, "")
        self.t_cash_order_receipt_forms = QWidget()
        self.t_cash_order_receipt_forms.setObjectName(u"t_cash_order_receipt_forms")
        self.gl_t_corf = QGridLayout(self.t_cash_order_receipt_forms)
        self.gl_t_corf.setObjectName(u"gl_t_corf")
        self.w_corf1 = QWidget(self.t_cash_order_receipt_forms)
        self.w_corf1.setObjectName(u"w_corf1")
        self.w_corf1.setEnabled(True)
        self.gl_corf1 = QGridLayout(self.w_corf1)
        self.gl_corf1.setSpacing(6)
        self.gl_corf1.setObjectName(u"gl_corf1")
        self.gl_corf1.setContentsMargins(0, 0, 0, 0)
        self.w_corf1_services = QWidget(self.w_corf1)
        self.w_corf1_services.setObjectName(u"w_corf1_services")
        self.w_corf1_services.setEnabled(True)
        self.hl_corf1_services = QHBoxLayout(self.w_corf1_services)
        self.hl_corf1_services.setSpacing(3)
        self.hl_corf1_services.setObjectName(u"hl_corf1_services")
        self.hl_corf1_services.setContentsMargins(0, 0, 0, 0)
        self.cmb_corf1_service = QComboBox(self.w_corf1_services)
        self.cmb_corf1_service.setObjectName(u"cmb_corf1_service")
        self.cmb_corf1_service.setEnabled(True)
        self.cmb_corf1_service.setMinimumSize(QSize(0, 22))
        self.cmb_corf1_service.setMaximumSize(QSize(16777215, 22))
        self.cmb_corf1_service.setEditable(True)
        self.cmb_corf1_service.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.cmb_corf1_service.setDuplicatesEnabled(False)

        self.hl_corf1_services.addWidget(self.cmb_corf1_service)

        self.pb_corf1_toggle_service = QPushButton(self.w_corf1_services)
        self.pb_corf1_toggle_service.setObjectName(u"pb_corf1_toggle_service")
        self.pb_corf1_toggle_service.setEnabled(True)
        self.pb_corf1_toggle_service.setMinimumSize(QSize(22, 22))
        self.pb_corf1_toggle_service.setMaximumSize(QSize(22, 22))
        self.pb_corf1_toggle_service.setIcon(icon5)
        self.pb_corf1_toggle_service.setIconSize(QSize(10, 10))

        self.hl_corf1_services.addWidget(self.pb_corf1_toggle_service)


        self.gl_corf1.addWidget(self.w_corf1_services, 8, 0, 1, 1)

        self.le_corf1_price_text = QLineEdit(self.w_corf1)
        self.le_corf1_price_text.setObjectName(u"le_corf1_price_text")
        self.le_corf1_price_text.setEnabled(True)
        self.le_corf1_price_text.setMinimumSize(QSize(0, 22))
        self.le_corf1_price_text.setMaximumSize(QSize(16777215, 22))
        self.le_corf1_price_text.setReadOnly(True)
        self.le_corf1_price_text.setClearButtonEnabled(True)

        self.gl_corf1.addWidget(self.le_corf1_price_text, 6, 1, 1, 1)

        self.le_corf1_agent = QLineEdit(self.w_corf1)
        self.le_corf1_agent.setObjectName(u"le_corf1_agent")
        self.le_corf1_agent.setEnabled(True)
        self.le_corf1_agent.setMinimumSize(QSize(0, 22))
        self.le_corf1_agent.setMaximumSize(QSize(16777215, 22))
        self.le_corf1_agent.setClearButtonEnabled(True)

        self.gl_corf1.addWidget(self.le_corf1_agent, 4, 0, 1, 1)

        self.l_corf1_price_text = QLabel(self.w_corf1)
        self.l_corf1_price_text.setObjectName(u"l_corf1_price_text")
        self.l_corf1_price_text.setEnabled(True)

        self.gl_corf1.addWidget(self.l_corf1_price_text, 5, 1, 1, 1)

        self.l_corf1_price = QLabel(self.w_corf1)
        self.l_corf1_price.setObjectName(u"l_corf1_price")
        self.l_corf1_price.setEnabled(True)

        self.gl_corf1.addWidget(self.l_corf1_price, 5, 0, 1, 1)

        self.le_corf1_price = QLineEdit(self.w_corf1)
        self.le_corf1_price.setObjectName(u"le_corf1_price")
        self.le_corf1_price.setEnabled(True)
        self.le_corf1_price.setMinimumSize(QSize(0, 22))
        self.le_corf1_price.setMaximumSize(QSize(16777215, 22))
        self.le_corf1_price.setClearButtonEnabled(True)

        self.gl_corf1.addWidget(self.le_corf1_price, 6, 0, 1, 1)

        self.l_corf1_service = QLabel(self.w_corf1)
        self.l_corf1_service.setObjectName(u"l_corf1_service")
        self.l_corf1_service.setEnabled(True)
        self.l_corf1_service.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gl_corf1.addWidget(self.l_corf1_service, 7, 0, 1, 1)

        self.de_corf1_date = QDateEdit(self.w_corf1)
        self.de_corf1_date.setObjectName(u"de_corf1_date")
        self.de_corf1_date.setEnabled(True)
        self.de_corf1_date.setMinimumSize(QSize(0, 22))
        self.de_corf1_date.setMaximumSize(QSize(16777215, 22))
        self.de_corf1_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_corf1_date.setDateTime(QDateTime(QDate(1970, 1, 1), QTime(0, 0, 0)))
        self.de_corf1_date.setCalendarPopup(True)

        self.gl_corf1.addWidget(self.de_corf1_date, 4, 1, 1, 1)

        self.l_corf1_date = QLabel(self.w_corf1)
        self.l_corf1_date.setObjectName(u"l_corf1_date")
        self.l_corf1_date.setEnabled(True)

        self.gl_corf1.addWidget(self.l_corf1_date, 3, 1, 1, 1)

        self.l_corf1_agent = QLabel(self.w_corf1)
        self.l_corf1_agent.setObjectName(u"l_corf1_agent")
        self.l_corf1_agent.setEnabled(True)

        self.gl_corf1.addWidget(self.l_corf1_agent, 3, 0, 1, 1)


        self.gl_t_corf.addWidget(self.w_corf1, 1, 0, 1, 2)

        self.vs_corf = QSpacerItem(596, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gl_t_corf.addItem(self.vs_corf, 10, 0, 1, 2)

        self.w_corf1_actions = QWidget(self.t_cash_order_receipt_forms)
        self.w_corf1_actions.setObjectName(u"w_corf1_actions")
        self.w_corf1_actions.setEnabled(True)
        self.w_corf1_actions.setMinimumSize(QSize(0, 35))
        self.w_corf1_actions.setMaximumSize(QSize(16777215, 35))
        self.gl_corf1_actions = QGridLayout(self.w_corf1_actions)
        self.gl_corf1_actions.setSpacing(3)
        self.gl_corf1_actions.setObjectName(u"gl_corf1_actions")
        self.gl_corf1_actions.setContentsMargins(0, 0, 0, 0)
        self.pb_corf1_save = QPushButton(self.w_corf1_actions)
        self.pb_corf1_save.setObjectName(u"pb_corf1_save")
        self.pb_corf1_save.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_corf1_save.sizePolicy().hasHeightForWidth())
        self.pb_corf1_save.setSizePolicy(sizePolicy)
        self.pb_corf1_save.setMinimumSize(QSize(35, 35))
        self.pb_corf1_save.setMaximumSize(QSize(35, 35))
        self.pb_corf1_save.setIcon(icon1)
        self.pb_corf1_save.setIconSize(QSize(22, 22))

        self.gl_corf1_actions.addWidget(self.pb_corf1_save, 3, 1, 1, 1)

        self.line_corf1_1 = QFrame(self.w_corf1_actions)
        self.line_corf1_1.setObjectName(u"line_corf1_1")
        self.line_corf1_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.line_corf1_1.sizePolicy().hasHeightForWidth())
        self.line_corf1_1.setSizePolicy(sizePolicy)
        self.line_corf1_1.setMinimumSize(QSize(0, 35))
        self.line_corf1_1.setFrameShape(QFrame.VLine)
        self.line_corf1_1.setFrameShadow(QFrame.Sunken)

        self.gl_corf1_actions.addWidget(self.line_corf1_1, 3, 2, 1, 1)

        self.pb_corf1_open_file = QPushButton(self.w_corf1_actions)
        self.pb_corf1_open_file.setObjectName(u"pb_corf1_open_file")
        self.pb_corf1_open_file.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_corf1_open_file.sizePolicy().hasHeightForWidth())
        self.pb_corf1_open_file.setSizePolicy(sizePolicy)
        self.pb_corf1_open_file.setMinimumSize(QSize(35, 35))
        self.pb_corf1_open_file.setMaximumSize(QSize(35, 35))
        self.pb_corf1_open_file.setIcon(icon2)
        self.pb_corf1_open_file.setIconSize(QSize(20, 20))

        self.gl_corf1_actions.addWidget(self.pb_corf1_open_file, 3, 3, 1, 1)

        self.pb_corf1_docx = QPushButton(self.w_corf1_actions)
        self.pb_corf1_docx.setObjectName(u"pb_corf1_docx")
        self.pb_corf1_docx.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_corf1_docx.sizePolicy().hasHeightForWidth())
        self.pb_corf1_docx.setSizePolicy(sizePolicy)
        self.pb_corf1_docx.setMinimumSize(QSize(35, 35))
        self.pb_corf1_docx.setMaximumSize(QSize(35, 35))
        self.pb_corf1_docx.setIcon(icon3)
        self.pb_corf1_docx.setIconSize(QSize(20, 20))

        self.gl_corf1_actions.addWidget(self.pb_corf1_docx, 3, 6, 1, 1)

        self.line_corf1_2 = QFrame(self.w_corf1_actions)
        self.line_corf1_2.setObjectName(u"line_corf1_2")
        self.line_corf1_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.line_corf1_2.sizePolicy().hasHeightForWidth())
        self.line_corf1_2.setSizePolicy(sizePolicy)
        self.line_corf1_2.setMinimumSize(QSize(0, 35))
        self.line_corf1_2.setFrameShape(QFrame.VLine)
        self.line_corf1_2.setFrameShadow(QFrame.Sunken)

        self.gl_corf1_actions.addWidget(self.line_corf1_2, 3, 5, 1, 1)

        self.pb_corf1_open_folder = QPushButton(self.w_corf1_actions)
        self.pb_corf1_open_folder.setObjectName(u"pb_corf1_open_folder")
        self.pb_corf1_open_folder.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_corf1_open_folder.sizePolicy().hasHeightForWidth())
        self.pb_corf1_open_folder.setSizePolicy(sizePolicy)
        self.pb_corf1_open_folder.setMinimumSize(QSize(35, 35))
        self.pb_corf1_open_folder.setMaximumSize(QSize(35, 35))
        self.pb_corf1_open_folder.setIcon(icon4)
        self.pb_corf1_open_folder.setIconSize(QSize(24, 24))

        self.gl_corf1_actions.addWidget(self.pb_corf1_open_folder, 3, 4, 1, 1)

        self.vl_corf1_title = QVBoxLayout()
        self.vl_corf1_title.setSpacing(2)
        self.vl_corf1_title.setObjectName(u"vl_corf1_title")
        self.vl_corf1_title.setContentsMargins(-1, 2, -1, -1)
        self.l_corf1 = QLabel(self.w_corf1_actions)
        self.l_corf1.setObjectName(u"l_corf1")
        self.l_corf1.setEnabled(True)
        self.l_corf1.setFont(font)

        self.vl_corf1_title.addWidget(self.l_corf1)

        self.l_corf1_path = QLabel(self.w_corf1_actions)
        self.l_corf1_path.setObjectName(u"l_corf1_path")
        self.l_corf1_path.setEnabled(True)

        self.vl_corf1_title.addWidget(self.l_corf1_path)


        self.gl_corf1_actions.addLayout(self.vl_corf1_title, 3, 0, 1, 1)


        self.gl_t_corf.addWidget(self.w_corf1_actions, 0, 0, 1, 2)

        self.w_corf2 = QWidget(self.t_cash_order_receipt_forms)
        self.w_corf2.setObjectName(u"w_corf2")
        self.w_corf2.setEnabled(True)
        self.gl_corf2 = QGridLayout(self.w_corf2)
        self.gl_corf2.setSpacing(6)
        self.gl_corf2.setObjectName(u"gl_corf2")
        self.gl_corf2.setContentsMargins(0, 0, 0, 0)
        self.w_corf2_services = QWidget(self.w_corf2)
        self.w_corf2_services.setObjectName(u"w_corf2_services")
        self.w_corf2_services.setEnabled(True)
        self.hl_corf2_services = QHBoxLayout(self.w_corf2_services)
        self.hl_corf2_services.setSpacing(3)
        self.hl_corf2_services.setObjectName(u"hl_corf2_services")
        self.hl_corf2_services.setContentsMargins(0, 0, 0, 0)
        self.cmb_corf2_service = QComboBox(self.w_corf2_services)
        self.cmb_corf2_service.setObjectName(u"cmb_corf2_service")
        self.cmb_corf2_service.setEnabled(True)
        self.cmb_corf2_service.setMinimumSize(QSize(0, 22))
        self.cmb_corf2_service.setMaximumSize(QSize(16777215, 22))
        self.cmb_corf2_service.setEditable(True)
        self.cmb_corf2_service.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.cmb_corf2_service.setDuplicatesEnabled(False)

        self.hl_corf2_services.addWidget(self.cmb_corf2_service)

        self.pb_corf2_toggle_service = QPushButton(self.w_corf2_services)
        self.pb_corf2_toggle_service.setObjectName(u"pb_corf2_toggle_service")
        self.pb_corf2_toggle_service.setEnabled(True)
        self.pb_corf2_toggle_service.setMinimumSize(QSize(22, 22))
        self.pb_corf2_toggle_service.setMaximumSize(QSize(22, 22))
        self.pb_corf2_toggle_service.setIcon(icon5)
        self.pb_corf2_toggle_service.setIconSize(QSize(10, 10))

        self.hl_corf2_services.addWidget(self.pb_corf2_toggle_service)


        self.gl_corf2.addWidget(self.w_corf2_services, 5, 0, 1, 1)

        self.l_corf2_agent = QLabel(self.w_corf2)
        self.l_corf2_agent.setObjectName(u"l_corf2_agent")
        self.l_corf2_agent.setEnabled(True)

        self.gl_corf2.addWidget(self.l_corf2_agent, 0, 0, 1, 1)

        self.l_corf2_price = QLabel(self.w_corf2)
        self.l_corf2_price.setObjectName(u"l_corf2_price")
        self.l_corf2_price.setEnabled(True)

        self.gl_corf2.addWidget(self.l_corf2_price, 2, 0, 1, 1)

        self.l_corf2_date = QLabel(self.w_corf2)
        self.l_corf2_date.setObjectName(u"l_corf2_date")
        self.l_corf2_date.setEnabled(True)

        self.gl_corf2.addWidget(self.l_corf2_date, 0, 1, 1, 1)

        self.le_corf2_price_text = QLineEdit(self.w_corf2)
        self.le_corf2_price_text.setObjectName(u"le_corf2_price_text")
        self.le_corf2_price_text.setEnabled(True)
        self.le_corf2_price_text.setMinimumSize(QSize(0, 22))
        self.le_corf2_price_text.setMaximumSize(QSize(16777215, 22))
        self.le_corf2_price_text.setReadOnly(True)
        self.le_corf2_price_text.setClearButtonEnabled(True)

        self.gl_corf2.addWidget(self.le_corf2_price_text, 3, 1, 1, 1)

        self.le_corf2_price = QLineEdit(self.w_corf2)
        self.le_corf2_price.setObjectName(u"le_corf2_price")
        self.le_corf2_price.setEnabled(True)
        self.le_corf2_price.setMinimumSize(QSize(0, 22))
        self.le_corf2_price.setMaximumSize(QSize(16777215, 22))
        self.le_corf2_price.setClearButtonEnabled(True)

        self.gl_corf2.addWidget(self.le_corf2_price, 3, 0, 1, 1)

        self.l_corf2_price_text = QLabel(self.w_corf2)
        self.l_corf2_price_text.setObjectName(u"l_corf2_price_text")
        self.l_corf2_price_text.setEnabled(True)

        self.gl_corf2.addWidget(self.l_corf2_price_text, 2, 1, 1, 1)

        self.de_corf2_date = QDateEdit(self.w_corf2)
        self.de_corf2_date.setObjectName(u"de_corf2_date")
        self.de_corf2_date.setEnabled(True)
        self.de_corf2_date.setMinimumSize(QSize(0, 22))
        self.de_corf2_date.setMaximumSize(QSize(16777215, 22))
        self.de_corf2_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_corf2_date.setDateTime(QDateTime(QDate(1970, 1, 1), QTime(0, 0, 0)))
        self.de_corf2_date.setCalendarPopup(True)

        self.gl_corf2.addWidget(self.de_corf2_date, 1, 1, 1, 1)

        self.le_corf2_agent = QLineEdit(self.w_corf2)
        self.le_corf2_agent.setObjectName(u"le_corf2_agent")
        self.le_corf2_agent.setEnabled(True)
        self.le_corf2_agent.setMinimumSize(QSize(0, 22))
        self.le_corf2_agent.setMaximumSize(QSize(16777215, 22))
        self.le_corf2_agent.setClearButtonEnabled(True)

        self.gl_corf2.addWidget(self.le_corf2_agent, 1, 0, 1, 1)

        self.l_corf2_service = QLabel(self.w_corf2)
        self.l_corf2_service.setObjectName(u"l_corf2_service")
        self.l_corf2_service.setEnabled(True)
        self.l_corf2_service.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gl_corf2.addWidget(self.l_corf2_service, 4, 0, 1, 1)


        self.gl_t_corf.addWidget(self.w_corf2, 3, 0, 1, 2)

        self.w_corf2_actions = QWidget(self.t_cash_order_receipt_forms)
        self.w_corf2_actions.setObjectName(u"w_corf2_actions")
        self.w_corf2_actions.setEnabled(True)
        self.w_corf2_actions.setMinimumSize(QSize(0, 35))
        self.w_corf2_actions.setMaximumSize(QSize(16777215, 35))
        self.gl_corf2_actions = QGridLayout(self.w_corf2_actions)
        self.gl_corf2_actions.setSpacing(3)
        self.gl_corf2_actions.setObjectName(u"gl_corf2_actions")
        self.gl_corf2_actions.setContentsMargins(0, 0, 0, 0)
        self.pb_corf2_save = QPushButton(self.w_corf2_actions)
        self.pb_corf2_save.setObjectName(u"pb_corf2_save")
        self.pb_corf2_save.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pb_corf2_save.sizePolicy().hasHeightForWidth())
        self.pb_corf2_save.setSizePolicy(sizePolicy)
        self.pb_corf2_save.setMinimumSize(QSize(35, 35))
        self.pb_corf2_save.setMaximumSize(QSize(35, 35))
        self.pb_corf2_save.setIcon(icon1)
        self.pb_corf2_save.setIconSize(QSize(22, 22))

        self.gl_corf2_actions.addWidget(self.pb_corf2_save, 3, 1, 1, 1)

        self.pb_corf2_docx = QPushButton(self.w_corf2_actions)
        self.pb_corf2_docx.setObjectName(u"pb_corf2_docx")
        self.pb_corf2_docx.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_corf2_docx.sizePolicy().hasHeightForWidth())
        self.pb_corf2_docx.setSizePolicy(sizePolicy)
        self.pb_corf2_docx.setMinimumSize(QSize(35, 35))
        self.pb_corf2_docx.setMaximumSize(QSize(35, 35))
        self.pb_corf2_docx.setIcon(icon3)
        self.pb_corf2_docx.setIconSize(QSize(20, 20))

        self.gl_corf2_actions.addWidget(self.pb_corf2_docx, 3, 6, 1, 1)

        self.pb_corf2_open_folder = QPushButton(self.w_corf2_actions)
        self.pb_corf2_open_folder.setObjectName(u"pb_corf2_open_folder")
        self.pb_corf2_open_folder.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_corf2_open_folder.sizePolicy().hasHeightForWidth())
        self.pb_corf2_open_folder.setSizePolicy(sizePolicy)
        self.pb_corf2_open_folder.setMinimumSize(QSize(35, 35))
        self.pb_corf2_open_folder.setMaximumSize(QSize(35, 35))
        self.pb_corf2_open_folder.setIcon(icon4)
        self.pb_corf2_open_folder.setIconSize(QSize(24, 24))

        self.gl_corf2_actions.addWidget(self.pb_corf2_open_folder, 3, 4, 1, 1)

        self.pb_corf2_open_file = QPushButton(self.w_corf2_actions)
        self.pb_corf2_open_file.setObjectName(u"pb_corf2_open_file")
        self.pb_corf2_open_file.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pb_corf2_open_file.sizePolicy().hasHeightForWidth())
        self.pb_corf2_open_file.setSizePolicy(sizePolicy)
        self.pb_corf2_open_file.setMinimumSize(QSize(35, 35))
        self.pb_corf2_open_file.setMaximumSize(QSize(35, 35))
        self.pb_corf2_open_file.setIcon(icon2)
        self.pb_corf2_open_file.setIconSize(QSize(20, 20))

        self.gl_corf2_actions.addWidget(self.pb_corf2_open_file, 3, 3, 1, 1)

        self.line_corf2_1 = QFrame(self.w_corf2_actions)
        self.line_corf2_1.setObjectName(u"line_corf2_1")
        self.line_corf2_1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.line_corf2_1.sizePolicy().hasHeightForWidth())
        self.line_corf2_1.setSizePolicy(sizePolicy)
        self.line_corf2_1.setMinimumSize(QSize(0, 35))
        self.line_corf2_1.setFrameShape(QFrame.VLine)
        self.line_corf2_1.setFrameShadow(QFrame.Sunken)

        self.gl_corf2_actions.addWidget(self.line_corf2_1, 3, 2, 1, 1)

        self.line_corf2_2 = QFrame(self.w_corf2_actions)
        self.line_corf2_2.setObjectName(u"line_corf2_2")
        self.line_corf2_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.line_corf2_2.sizePolicy().hasHeightForWidth())
        self.line_corf2_2.setSizePolicy(sizePolicy)
        self.line_corf2_2.setMinimumSize(QSize(0, 35))
        self.line_corf2_2.setFrameShape(QFrame.VLine)
        self.line_corf2_2.setFrameShadow(QFrame.Sunken)

        self.gl_corf2_actions.addWidget(self.line_corf2_2, 3, 5, 1, 1)

        self.vl_corf2_title = QVBoxLayout()
        self.vl_corf2_title.setSpacing(2)
        self.vl_corf2_title.setObjectName(u"vl_corf2_title")
        self.l_corf2 = QLabel(self.w_corf2_actions)
        self.l_corf2.setObjectName(u"l_corf2")
        self.l_corf2.setEnabled(True)
        self.l_corf2.setFont(font)

        self.vl_corf2_title.addWidget(self.l_corf2)

        self.l_corf2_path = QLabel(self.w_corf2_actions)
        self.l_corf2_path.setObjectName(u"l_corf2_path")
        self.l_corf2_path.setEnabled(True)

        self.vl_corf2_title.addWidget(self.l_corf2_path)


        self.gl_corf2_actions.addLayout(self.vl_corf2_title, 3, 0, 1, 1)


        self.gl_t_corf.addWidget(self.w_corf2_actions, 2, 0, 1, 2)

        self.tw_addictions.addTab(self.t_cash_order_receipt_forms, "")

        self.vl_main.addWidget(self.tw_addictions)

        QWidget.setTabOrder(self.le_af_agent, self.de_af_date)
        QWidget.setTabOrder(self.de_af_date, self.le_af_price)
        QWidget.setTabOrder(self.le_af_price, self.le_af_price_text)
        QWidget.setTabOrder(self.le_af_price_text, self.cmb_af_service)
        QWidget.setTabOrder(self.cmb_af_service, self.pb_af_toggle_service)
        QWidget.setTabOrder(self.pb_af_toggle_service, self.le_af_company)
        QWidget.setTabOrder(self.le_af_company, self.pb_af_save)
        QWidget.setTabOrder(self.pb_af_save, self.pb_af_open_file)
        QWidget.setTabOrder(self.pb_af_open_file, self.pb_af_open_folder)
        QWidget.setTabOrder(self.pb_af_open_folder, self.pb_af_docx)
        QWidget.setTabOrder(self.pb_af_docx, self.le_coef_agent)
        QWidget.setTabOrder(self.le_coef_agent, self.de_coef_date)
        QWidget.setTabOrder(self.de_coef_date, self.le_coef_price)
        QWidget.setTabOrder(self.le_coef_price, self.le_coef_price_text)
        QWidget.setTabOrder(self.le_coef_price_text, self.cmb_coef_service)
        QWidget.setTabOrder(self.cmb_coef_service, self.pb_coef_toggle_service)
        QWidget.setTabOrder(self.pb_coef_toggle_service, self.le_coef_document)
        QWidget.setTabOrder(self.le_coef_document, self.le_coef_document_code)
        QWidget.setTabOrder(self.le_coef_document_code, self.de_coef_document_issue_date)
        QWidget.setTabOrder(self.de_coef_document_issue_date, self.le_coef_document_issue_place)
        QWidget.setTabOrder(self.le_coef_document_issue_place, self.pte_coef_addiction)
        QWidget.setTabOrder(self.pte_coef_addiction, self.pb_coef_save)
        QWidget.setTabOrder(self.pb_coef_save, self.pb_coef_open_file)
        QWidget.setTabOrder(self.pb_coef_open_file, self.pb_coef_open_folder)
        QWidget.setTabOrder(self.pb_coef_open_folder, self.pb_coef_docx)
        QWidget.setTabOrder(self.pb_coef_docx, self.le_corf1_agent)
        QWidget.setTabOrder(self.le_corf1_agent, self.de_corf1_date)
        QWidget.setTabOrder(self.de_corf1_date, self.le_corf1_price)
        QWidget.setTabOrder(self.le_corf1_price, self.le_corf1_price_text)
        QWidget.setTabOrder(self.le_corf1_price_text, self.cmb_corf1_service)
        QWidget.setTabOrder(self.cmb_corf1_service, self.pb_corf1_toggle_service)
        QWidget.setTabOrder(self.pb_corf1_toggle_service, self.pb_corf1_save)
        QWidget.setTabOrder(self.pb_corf1_save, self.pb_corf1_open_file)
        QWidget.setTabOrder(self.pb_corf1_open_file, self.pb_corf1_open_folder)
        QWidget.setTabOrder(self.pb_corf1_open_folder, self.pb_corf1_docx)
        QWidget.setTabOrder(self.pb_corf1_docx, self.le_corf2_agent)
        QWidget.setTabOrder(self.le_corf2_agent, self.de_corf2_date)
        QWidget.setTabOrder(self.de_corf2_date, self.le_corf2_price)
        QWidget.setTabOrder(self.le_corf2_price, self.le_corf2_price_text)
        QWidget.setTabOrder(self.le_corf2_price_text, self.cmb_corf2_service)
        QWidget.setTabOrder(self.cmb_corf2_service, self.pb_corf2_toggle_service)
        QWidget.setTabOrder(self.pb_corf2_toggle_service, self.pb_corf2_save)
        QWidget.setTabOrder(self.pb_corf2_save, self.pb_corf2_open_file)
        QWidget.setTabOrder(self.pb_corf2_open_file, self.pb_corf2_open_folder)
        QWidget.setTabOrder(self.pb_corf2_open_folder, self.pb_corf2_docx)
        QWidget.setTabOrder(self.pb_corf2_docx, self.tw_addictions)

        self.retranslateUi(EditAddictionsWindow)

        self.tw_addictions.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(EditAddictionsWindow)
    # setupUi

    def retranslateUi(self, EditAddictionsWindow):
        EditAddictionsWindow.setWindowTitle(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.l_contract_number.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u043a\u0442:", None))
        self.l_contract_service.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430:", None))
        self.l_contract_price.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u043f\u043b\u0430\u0442\u0430:", None))
        self.l_contract_path.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0443\u0442\u044c:", None))
#if QT_CONFIG(tooltip)
        self.pb_af_save.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_af_open_file.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_af_open_file.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_af_docx.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0432\u044c\u044e \u0444\u0430\u0439\u043b\u0430 Word", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_af_docx.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.l_af.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0410\u043a\u0442", None))
        self.l_af_path.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0443\u0442\u044c:", None))
#if QT_CONFIG(tooltip)
        self.pb_af_open_folder.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_af_open_folder.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.l_af_price.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.le_af_price.setText("")
        self.le_af_price.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.l_af_price_text.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e", None))
        self.l_af_agent.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.le_af_agent.setText("")
        self.le_af_agent.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.le_af_price_text.setText("")
        self.le_af_price_text.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e", None))
        self.l_af_date.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.le_af_company.setText("")
        self.le_af_company.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.l_af_company.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.l_af_service.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430 / \u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.tw_addictions.setTabText(self.tw_addictions.indexOf(self.t_act_form), QCoreApplication.translate("EditAddictionsWindow", u"\u0410\u043a\u0442", None))
        self.le_coef_document_code.setText("")
        self.le_coef_document_code.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.l_coef_document_issue_date.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.l_coef_addiction.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.le_coef_document.setText("")
        self.le_coef_document.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.l_coef_price.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.l_coef_price_text.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e", None))
        self.le_coef_agent.setText("")
        self.le_coef_agent.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.l_coef_document_code.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041d\u043e\u043c\u0435\u0440", None))
        self.le_coef_price.setText("")
        self.le_coef_price.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.l_coef_service.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430 / \u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.le_coef_price_text.setText("")
        self.le_coef_price_text.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e", None))
        self.l_coef_document_issue_place.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041c\u0435\u0441\u0442\u043e \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.l_coef_document.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.le_coef_document_issue_place.setText("")
        self.le_coef_document_issue_place.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u041c\u0435\u0441\u0442\u043e \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.l_coef_date.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.l_coef_agent.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.pb_coef_open_file.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_coef_open_file.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_coef_save.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_coef_open_folder.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_coef_open_folder.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_coef_docx.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0432\u044c\u044e \u0444\u0430\u0439\u043b\u0430 Word", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_coef_docx.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
        self.l_coef.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043e\u0440\u0434\u0435\u0440", None))
        self.l_coef_path.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.tw_addictions.setTabText(self.tw_addictions.indexOf(self.t_cash_order_expense_form), QCoreApplication.translate("EditAddictionsWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043e\u0440\u0434\u0435\u0440", None))
        self.le_corf1_price_text.setText("")
        self.le_corf1_price_text.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e", None))
        self.le_corf1_agent.setText("")
        self.le_corf1_agent.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.l_corf1_price_text.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e", None))
        self.l_corf1_price.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.le_corf1_price.setText("")
        self.le_corf1_price.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.l_corf1_service.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430 / \u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.l_corf1_date.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.l_corf1_agent.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.pb_corf1_save.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_corf1_open_file.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_corf1_open_file.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_corf1_docx.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0432\u044c\u044e \u0444\u0430\u0439\u043b\u0430 Word", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_corf1_docx.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_corf1_open_folder.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_corf1_open_folder.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.l_corf1.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0438\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043e\u0440\u0434\u0435\u0440 1", None))
        self.l_corf1_path.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.l_corf2_agent.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.l_corf2_price.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.l_corf2_date.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f", None))
        self.le_corf2_price_text.setText("")
        self.le_corf2_price_text.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e", None))
        self.le_corf2_price.setText("")
        self.le_corf2_price.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.l_corf2_price_text.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u0443\u043c\u043c\u0430 \u043f\u0440\u043e\u043f\u0438\u0441\u044c\u044e", None))
        self.le_corf2_agent.setText("")
        self.le_corf2_agent.setPlaceholderText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.l_corf2_service.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430 / \u041e\u0441\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
#if QT_CONFIG(tooltip)
        self.pb_corf2_save.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_corf2_docx.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0435\u0432\u044c\u044e \u0444\u0430\u0439\u043b\u0430 Word", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_corf2_docx.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+W", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_corf2_open_folder.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_corf2_open_folder.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_corf2_open_file.setToolTip(QCoreApplication.translate("EditAddictionsWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_corf2_open_file.setShortcut(QCoreApplication.translate("EditAddictionsWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.l_corf2.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0438\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043e\u0440\u0434\u0435\u0440 2", None))
        self.l_corf2_path.setText(QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.tw_addictions.setTabText(self.tw_addictions.indexOf(self.t_cash_order_receipt_forms), QCoreApplication.translate("EditAddictionsWindow", u"\u041f\u0440\u0438\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043e\u0440\u0434\u0435\u0440", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateDocxWindow.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDateEdit, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)
import resources_rc

class Ui_CreateDocxWindow(object):
    def setupUi(self, CreateDocxWindow):
        if not CreateDocxWindow.objectName():
            CreateDocxWindow.setObjectName(u"CreateDocxWindow")
        CreateDocxWindow.resize(650, 449)
        icon = QIcon()
        icon.addFile(u":/images/pngs/main-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        CreateDocxWindow.setWindowIcon(icon)
        self.gl_main = QGridLayout(CreateDocxWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setHorizontalSpacing(9)
        self.w_services = QWidget(CreateDocxWindow)
        self.w_services.setObjectName(u"w_services")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w_services.sizePolicy().hasHeightForWidth())
        self.w_services.setSizePolicy(sizePolicy)
        self.hl_service = QHBoxLayout(self.w_services)
        self.hl_service.setSpacing(3)
        self.hl_service.setObjectName(u"hl_service")
        self.hl_service.setContentsMargins(0, 0, 0, 0)
        self.cmb_service = QComboBox(self.w_services)
        self.cmb_service.setObjectName(u"cmb_service")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cmb_service.sizePolicy().hasHeightForWidth())
        self.cmb_service.setSizePolicy(sizePolicy1)
        self.cmb_service.setMinimumSize(QSize(0, 22))
        self.cmb_service.setMaximumSize(QSize(16777215, 22))
        self.cmb_service.setEditable(True)
        self.cmb_service.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.cmb_service.setDuplicatesEnabled(False)

        self.hl_service.addWidget(self.cmb_service)

        self.pb_toggle_service = QPushButton(self.w_services)
        self.pb_toggle_service.setObjectName(u"pb_toggle_service")
        self.pb_toggle_service.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_toggle_service.sizePolicy().hasHeightForWidth())
        self.pb_toggle_service.setSizePolicy(sizePolicy2)
        self.pb_toggle_service.setMinimumSize(QSize(0, 22))
        self.pb_toggle_service.setMaximumSize(QSize(16777215, 22))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_toggle_service.setIcon(icon1)
        self.pb_toggle_service.setIconSize(QSize(10, 10))

        self.hl_service.addWidget(self.pb_toggle_service)


        self.gl_main.addWidget(self.w_services, 3, 1, 1, 1)

        self.l_price = QLabel(CreateDocxWindow)
        self.l_price.setObjectName(u"l_price")
        sizePolicy1.setHeightForWidth(self.l_price.sizePolicy().hasHeightForWidth())
        self.l_price.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_price, 2, 0, 1, 1)

        self.l_contract_end_date = QLabel(CreateDocxWindow)
        self.l_contract_end_date.setObjectName(u"l_contract_end_date")
        self.l_contract_end_date.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.l_contract_end_date.sizePolicy().hasHeightForWidth())
        self.l_contract_end_date.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_contract_end_date, 6, 0, 1, 2)

        self.l_requisites = QLabel(CreateDocxWindow)
        self.l_requisites.setObjectName(u"l_requisites")
        sizePolicy1.setHeightForWidth(self.l_requisites.sizePolicy().hasHeightForWidth())
        self.l_requisites.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(9)
        self.l_requisites.setFont(font)
        self.l_requisites.setAlignment(Qt.AlignCenter)

        self.gl_main.addWidget(self.l_requisites, 11, 0, 1, 2)

        self.l_passwort_kp = QLabel(CreateDocxWindow)
        self.l_passwort_kp.setObjectName(u"l_passwort_kp")
        sizePolicy1.setHeightForWidth(self.l_passwort_kp.sizePolicy().hasHeightForWidth())
        self.l_passwort_kp.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_passwort_kp, 16, 0, 1, 1)

        self.pb_create = QPushButton(CreateDocxWindow)
        self.pb_create.setObjectName(u"pb_create")
        sizePolicy1.setHeightForWidth(self.pb_create.sizePolicy().hasHeightForWidth())
        self.pb_create.setSizePolicy(sizePolicy1)
        self.pb_create.setMinimumSize(QSize(0, 24))
        self.pb_create.setMaximumSize(QSize(16777215, 24))

        self.gl_main.addWidget(self.pb_create, 20, 1, 1, 1)

        self.l_passport_issue_date = QLabel(CreateDocxWindow)
        self.l_passport_issue_date.setObjectName(u"l_passport_issue_date")
        sizePolicy1.setHeightForWidth(self.l_passport_issue_date.sizePolicy().hasHeightForWidth())
        self.l_passport_issue_date.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_passport_issue_date, 14, 1, 1, 1)

        self.le_passport_kp = QLineEdit(CreateDocxWindow)
        self.le_passport_kp.setObjectName(u"le_passport_kp")
        sizePolicy1.setHeightForWidth(self.le_passport_kp.sizePolicy().hasHeightForWidth())
        self.le_passport_kp.setSizePolicy(sizePolicy1)
        self.le_passport_kp.setMinimumSize(QSize(0, 22))
        self.le_passport_kp.setMaximumSize(QSize(16777215, 22))

        self.gl_main.addWidget(self.le_passport_kp, 17, 0, 1, 1)

        self.l_service = QLabel(CreateDocxWindow)
        self.l_service.setObjectName(u"l_service")
        sizePolicy1.setHeightForWidth(self.l_service.sizePolicy().hasHeightForWidth())
        self.l_service.setSizePolicy(sizePolicy1)
        self.l_service.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gl_main.addWidget(self.l_service, 2, 1, 1, 1)

        self.pb_clear = QPushButton(CreateDocxWindow)
        self.pb_clear.setObjectName(u"pb_clear")
        sizePolicy1.setHeightForWidth(self.pb_clear.sizePolicy().hasHeightForWidth())
        self.pb_clear.setSizePolicy(sizePolicy1)
        self.pb_clear.setMinimumSize(QSize(0, 26))
        self.pb_clear.setMaximumSize(QSize(16777215, 26))

        self.gl_main.addWidget(self.pb_clear, 20, 0, 1, 1)

        self.pte_passport_issue_place = QPlainTextEdit(CreateDocxWindow)
        self.pte_passport_issue_place.setObjectName(u"pte_passport_issue_place")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pte_passport_issue_place.sizePolicy().hasHeightForWidth())
        self.pte_passport_issue_place.setSizePolicy(sizePolicy3)
        self.pte_passport_issue_place.setMinimumSize(QSize(0, 50))
        self.pte_passport_issue_place.setMaximumSize(QSize(16777215, 50))
        self.pte_passport_issue_place.setTabChangesFocus(True)

        self.gl_main.addWidget(self.pte_passport_issue_place, 19, 0, 1, 2)

        self.l_passport_issue_place = QLabel(CreateDocxWindow)
        self.l_passport_issue_place.setObjectName(u"l_passport_issue_place")
        sizePolicy1.setHeightForWidth(self.l_passport_issue_place.sizePolicy().hasHeightForWidth())
        self.l_passport_issue_place.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_passport_issue_place, 18, 0, 1, 1)

        self.cb_part_price = QCheckBox(CreateDocxWindow)
        self.cb_part_price.setObjectName(u"cb_part_price")
        sizePolicy1.setHeightForWidth(self.cb_part_price.sizePolicy().hasHeightForWidth())
        self.cb_part_price.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.cb_part_price, 4, 0, 1, 1)

        self.le_second_price = QLineEdit(CreateDocxWindow)
        self.le_second_price.setObjectName(u"le_second_price")
        self.le_second_price.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_second_price.sizePolicy().hasHeightForWidth())
        self.le_second_price.setSizePolicy(sizePolicy1)
        self.le_second_price.setMinimumSize(QSize(0, 22))
        self.le_second_price.setMaximumSize(QSize(16777215, 22))
        self.le_second_price.setReadOnly(True)
        self.le_second_price.setClearButtonEnabled(False)

        self.gl_main.addWidget(self.le_second_price, 5, 1, 1, 1)

        self.le_first_price = QLineEdit(CreateDocxWindow)
        self.le_first_price.setObjectName(u"le_first_price")
        self.le_first_price.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_first_price.sizePolicy().hasHeightForWidth())
        self.le_first_price.setSizePolicy(sizePolicy1)
        self.le_first_price.setMinimumSize(QSize(0, 22))
        self.le_first_price.setMaximumSize(QSize(16777215, 22))
        self.le_first_price.setClearButtonEnabled(True)

        self.gl_main.addWidget(self.le_first_price, 5, 0, 1, 1)

        self.l_company = QLabel(CreateDocxWindow)
        self.l_company.setObjectName(u"l_company")
        sizePolicy1.setHeightForWidth(self.l_company.sizePolicy().hasHeightForWidth())
        self.l_company.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_company, 0, 0, 1, 1)

        self.l_phone = QLabel(CreateDocxWindow)
        self.l_phone.setObjectName(u"l_phone")
        sizePolicy1.setHeightForWidth(self.l_phone.sizePolicy().hasHeightForWidth())
        self.l_phone.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_phone, 12, 1, 1, 1)

        self.cb_agent = QCheckBox(CreateDocxWindow)
        self.cb_agent.setObjectName(u"cb_agent")
        sizePolicy1.setHeightForWidth(self.cb_agent.sizePolicy().hasHeightForWidth())
        self.cb_agent.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.cb_agent, 9, 0, 1, 1)

        self.le_agent = QLineEdit(CreateDocxWindow)
        self.le_agent.setObjectName(u"le_agent")
        self.le_agent.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.le_agent.sizePolicy().hasHeightForWidth())
        self.le_agent.setSizePolicy(sizePolicy1)
        self.le_agent.setMinimumSize(QSize(0, 22))
        self.le_agent.setMaximumSize(QSize(16777215, 22))
        self.le_agent.setClearButtonEnabled(True)

        self.gl_main.addWidget(self.le_agent, 10, 0, 1, 1)

        self.le_price = QLineEdit(CreateDocxWindow)
        self.le_price.setObjectName(u"le_price")
        sizePolicy1.setHeightForWidth(self.le_price.sizePolicy().hasHeightForWidth())
        self.le_price.setSizePolicy(sizePolicy1)
        self.le_price.setMinimumSize(QSize(0, 22))
        self.le_price.setMaximumSize(QSize(16777215, 22))
        self.le_price.setClearButtonEnabled(True)

        self.gl_main.addWidget(self.le_price, 3, 0, 1, 1)

        self.l_contract_date = QLabel(CreateDocxWindow)
        self.l_contract_date.setObjectName(u"l_contract_date")
        sizePolicy1.setHeightForWidth(self.l_contract_date.sizePolicy().hasHeightForWidth())
        self.l_contract_date.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_contract_date, 0, 1, 1, 1)

        self.le_passport_code = QLineEdit(CreateDocxWindow)
        self.le_passport_code.setObjectName(u"le_passport_code")
        sizePolicy1.setHeightForWidth(self.le_passport_code.sizePolicy().hasHeightForWidth())
        self.le_passport_code.setSizePolicy(sizePolicy1)
        self.le_passport_code.setMinimumSize(QSize(0, 22))
        self.le_passport_code.setMaximumSize(QSize(16777215, 22))

        self.gl_main.addWidget(self.le_passport_code, 15, 0, 1, 1)

        self.le_company = QLineEdit(CreateDocxWindow)
        self.le_company.setObjectName(u"le_company")
        sizePolicy1.setHeightForWidth(self.le_company.sizePolicy().hasHeightForWidth())
        self.le_company.setSizePolicy(sizePolicy1)
        self.le_company.setMinimumSize(QSize(0, 22))
        self.le_company.setMaximumSize(QSize(16777215, 22))
        self.le_company.setClearButtonEnabled(True)

        self.gl_main.addWidget(self.le_company, 1, 0, 1, 1)

        self.le_phone = QLineEdit(CreateDocxWindow)
        self.le_phone.setObjectName(u"le_phone")
        sizePolicy1.setHeightForWidth(self.le_phone.sizePolicy().hasHeightForWidth())
        self.le_phone.setSizePolicy(sizePolicy1)
        self.le_phone.setMinimumSize(QSize(0, 22))
        self.le_phone.setMaximumSize(QSize(16777215, 22))

        self.gl_main.addWidget(self.le_phone, 13, 1, 1, 1)

        self.l_birthday = QLabel(CreateDocxWindow)
        self.l_birthday.setObjectName(u"l_birthday")
        sizePolicy1.setHeightForWidth(self.l_birthday.sizePolicy().hasHeightForWidth())
        self.l_birthday.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_birthday, 12, 0, 1, 1)

        self.l_passport_code = QLabel(CreateDocxWindow)
        self.l_passport_code.setObjectName(u"l_passport_code")
        sizePolicy1.setHeightForWidth(self.l_passport_code.sizePolicy().hasHeightForWidth())
        self.l_passport_code.setSizePolicy(sizePolicy1)

        self.gl_main.addWidget(self.l_passport_code, 14, 0, 1, 1)

        self.de_birthday = QDateEdit(CreateDocxWindow)
        self.de_birthday.setObjectName(u"de_birthday")
        sizePolicy1.setHeightForWidth(self.de_birthday.sizePolicy().hasHeightForWidth())
        self.de_birthday.setSizePolicy(sizePolicy1)
        self.de_birthday.setMinimumSize(QSize(0, 22))
        self.de_birthday.setMaximumSize(QSize(16777215, 22))
        self.de_birthday.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_birthday.setCalendarPopup(True)
        self.de_birthday.setDate(QDate(1970, 1, 1))

        self.gl_main.addWidget(self.de_birthday, 13, 0, 1, 1)

        self.de_contract_end_date = QDateEdit(CreateDocxWindow)
        self.de_contract_end_date.setObjectName(u"de_contract_end_date")
        self.de_contract_end_date.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.de_contract_end_date.sizePolicy().hasHeightForWidth())
        self.de_contract_end_date.setSizePolicy(sizePolicy1)
        self.de_contract_end_date.setMinimumSize(QSize(0, 22))
        self.de_contract_end_date.setMaximumSize(QSize(16777215, 22))
        self.de_contract_end_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_contract_end_date.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.de_contract_end_date.setCalendarPopup(True)
        self.de_contract_end_date.setDate(QDate(2020, 1, 1))

        self.gl_main.addWidget(self.de_contract_end_date, 8, 0, 1, 1)

        self.de_passport_issue_date = QDateEdit(CreateDocxWindow)
        self.de_passport_issue_date.setObjectName(u"de_passport_issue_date")
        sizePolicy1.setHeightForWidth(self.de_passport_issue_date.sizePolicy().hasHeightForWidth())
        self.de_passport_issue_date.setSizePolicy(sizePolicy1)
        self.de_passport_issue_date.setMinimumSize(QSize(0, 22))
        self.de_passport_issue_date.setMaximumSize(QSize(16777215, 22))
        self.de_passport_issue_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_passport_issue_date.setCalendarPopup(True)
        self.de_passport_issue_date.setDate(QDate(2020, 1, 1))

        self.gl_main.addWidget(self.de_passport_issue_date, 15, 1, 1, 1)

        self.de_contract_date = QDateEdit(CreateDocxWindow)
        self.de_contract_date.setObjectName(u"de_contract_date")
        sizePolicy1.setHeightForWidth(self.de_contract_date.sizePolicy().hasHeightForWidth())
        self.de_contract_date.setSizePolicy(sizePolicy1)
        self.de_contract_date.setMinimumSize(QSize(0, 22))
        self.de_contract_date.setMaximumSize(QSize(16777215, 22))
        self.de_contract_date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.de_contract_date.setDateTime(QDateTime(QDate(1970, 1, 1), QTime(0, 0, 0)))
        self.de_contract_date.setCalendarPopup(True)

        self.gl_main.addWidget(self.de_contract_date, 1, 1, 1, 1)

        QWidget.setTabOrder(self.le_company, self.de_contract_date)
        QWidget.setTabOrder(self.de_contract_date, self.le_price)
        QWidget.setTabOrder(self.le_price, self.cmb_service)
        QWidget.setTabOrder(self.cmb_service, self.pb_toggle_service)
        QWidget.setTabOrder(self.pb_toggle_service, self.cb_part_price)
        QWidget.setTabOrder(self.cb_part_price, self.le_first_price)
        QWidget.setTabOrder(self.le_first_price, self.le_second_price)
        QWidget.setTabOrder(self.le_second_price, self.de_contract_end_date)
        QWidget.setTabOrder(self.de_contract_end_date, self.cb_agent)
        QWidget.setTabOrder(self.cb_agent, self.le_agent)
        QWidget.setTabOrder(self.le_agent, self.de_birthday)
        QWidget.setTabOrder(self.de_birthday, self.le_phone)
        QWidget.setTabOrder(self.le_phone, self.le_passport_code)
        QWidget.setTabOrder(self.le_passport_code, self.de_passport_issue_date)
        QWidget.setTabOrder(self.de_passport_issue_date, self.le_passport_kp)
        QWidget.setTabOrder(self.le_passport_kp, self.pte_passport_issue_place)
        QWidget.setTabOrder(self.pte_passport_issue_place, self.pb_create)
        QWidget.setTabOrder(self.pb_create, self.pb_clear)

        self.retranslateUi(CreateDocxWindow)

        QMetaObject.connectSlotsByName(CreateDocxWindow)
    # setupUi

    def retranslateUi(self, CreateDocxWindow):
        CreateDocxWindow.setWindowTitle(QCoreApplication.translate("CreateDocxWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043a\u043e\u043d\u0442\u0440\u0430\u043a\u0442", None))
        self.l_price.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.l_contract_end_date.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0434\u0435\u043b\u0430", None))
        self.l_requisites.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0420\u0435\u043a\u0432\u0438\u0437\u0438\u0442\u044b \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
        self.l_passwort_kp.setText(QCoreApplication.translate("CreateDocxWindow", u"\u041a\u043e\u0434 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f (\u043a/\u043f)", None))
        self.pb_create.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.l_passport_issue_date.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.le_passport_kp.setInputMask(QCoreApplication.translate("CreateDocxWindow", u"999-999", None))
        self.le_passport_kp.setPlaceholderText(QCoreApplication.translate("CreateDocxWindow", u"\u041a\u043e\u0434 \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.l_service.setText(QCoreApplication.translate("CreateDocxWindow", u"\u041e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u043c\u0430\u044f \u0443\u0441\u043b\u0443\u0433\u0430", None))
        self.pb_clear.setText(QCoreApplication.translate("CreateDocxWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.l_passport_issue_place.setText(QCoreApplication.translate("CreateDocxWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442 \u0432\u044b\u0434\u0430\u043d", None))
        self.cb_part_price.setText(QCoreApplication.translate("CreateDocxWindow", u"\u041e\u043f\u043b\u0430\u0442\u0430 \u0447\u0430\u0441\u0442\u044f\u043c\u0438", None))
        self.le_second_price.setPlaceholderText(QCoreApplication.translate("CreateDocxWindow", u"\u0414\u043e\u043f\u043b\u0430\u0442\u0430", None))
        self.le_first_price.setPlaceholderText(QCoreApplication.translate("CreateDocxWindow", u"\u041f\u0440\u0435\u0434\u043e\u043f\u043b\u0430\u0442\u0430", None))
        self.l_company.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.l_phone.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.cb_agent.setText(QCoreApplication.translate("CreateDocxWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.le_agent.setPlaceholderText(QCoreApplication.translate("CreateDocxWindow", u"\u0424\u0418\u041e \u043f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044f", None))
        self.le_price.setText("")
        self.le_price.setPlaceholderText(QCoreApplication.translate("CreateDocxWindow", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.l_contract_date.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0414\u0430\u0442\u0430 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f", None))
        self.le_passport_code.setInputMask(QCoreApplication.translate("CreateDocxWindow", u"99 99 999999", None))
        self.le_passport_code.setPlaceholderText(QCoreApplication.translate("CreateDocxWindow", u"\u0421\u0435\u0440\u0438\u044f \u0438 \u043d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
        self.le_company.setPlaceholderText(QCoreApplication.translate("CreateDocxWindow", u"\u0424\u0418\u041e \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
        self.le_phone.setInputMask(QCoreApplication.translate("CreateDocxWindow", u"8 (999) 999 9999", None))
        self.le_phone.setText(QCoreApplication.translate("CreateDocxWindow", u"8 ()  ", None))
        self.le_phone.setPlaceholderText(QCoreApplication.translate("CreateDocxWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.l_birthday.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.l_passport_code.setText(QCoreApplication.translate("CreateDocxWindow", u"\u0421\u0435\u0440\u0438\u044f \u0438 \u043d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430", None))
    # retranslateUi


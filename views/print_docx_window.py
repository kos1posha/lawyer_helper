# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrintDocxWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
import resources_rc

class Ui_PrintDocxWindow(object):
    def setupUi(self, PrintDocxWindow):
        if not PrintDocxWindow.objectName():
            PrintDocxWindow.setObjectName(u"PrintDocxWindow")
        PrintDocxWindow.resize(219, 223)
        icon = QIcon()
        icon.addFile(u":/images/pngs/main-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        PrintDocxWindow.setWindowIcon(icon)
        self.gl_main = QGridLayout(PrintDocxWindow)
        self.gl_main.setObjectName(u"gl_main")
        self.w_contract = QWidget(PrintDocxWindow)
        self.w_contract.setObjectName(u"w_contract")
        self.gl_contract = QGridLayout(self.w_contract)
        self.gl_contract.setObjectName(u"gl_contract")
        self.gl_contract.setVerticalSpacing(0)
        self.gl_contract.setContentsMargins(0, 0, 0, 0)
        self.cb_contract = QCheckBox(self.w_contract)
        self.cb_contract.setObjectName(u"cb_contract")

        self.gl_contract.addWidget(self.cb_contract, 0, 0, 1, 1)

        self.l_contract_path = QLabel(self.w_contract)
        self.l_contract_path.setObjectName(u"l_contract_path")
        font = QFont()
        font.setPointSize(7)
        self.l_contract_path.setFont(font)

        self.gl_contract.addWidget(self.l_contract_path, 1, 0, 1, 1)


        self.gl_main.addWidget(self.w_contract, 1, 0, 1, 1)

        self.w_coef = QWidget(PrintDocxWindow)
        self.w_coef.setObjectName(u"w_coef")
        self.gl_coef = QGridLayout(self.w_coef)
        self.gl_coef.setObjectName(u"gl_coef")
        self.gl_coef.setVerticalSpacing(0)
        self.gl_coef.setContentsMargins(0, 0, 0, 0)
        self.l_coef_path = QLabel(self.w_coef)
        self.l_coef_path.setObjectName(u"l_coef_path")
        self.l_coef_path.setFont(font)

        self.gl_coef.addWidget(self.l_coef_path, 1, 0, 1, 1)

        self.cb_coef = QCheckBox(self.w_coef)
        self.cb_coef.setObjectName(u"cb_coef")

        self.gl_coef.addWidget(self.cb_coef, 0, 0, 1, 1)


        self.gl_main.addWidget(self.w_coef, 3, 0, 1, 1)

        self.w_act = QWidget(PrintDocxWindow)
        self.w_act.setObjectName(u"w_act")
        self.gl_act = QGridLayout(self.w_act)
        self.gl_act.setObjectName(u"gl_act")
        self.gl_act.setVerticalSpacing(0)
        self.gl_act.setContentsMargins(0, 0, 0, 0)
        self.l_act_path = QLabel(self.w_act)
        self.l_act_path.setObjectName(u"l_act_path")
        self.l_act_path.setFont(font)

        self.gl_act.addWidget(self.l_act_path, 1, 0, 1, 1)

        self.cb_act = QCheckBox(self.w_act)
        self.cb_act.setObjectName(u"cb_act")

        self.gl_act.addWidget(self.cb_act, 0, 0, 1, 1)


        self.gl_main.addWidget(self.w_act, 2, 0, 1, 1)

        self.w_corf1 = QWidget(PrintDocxWindow)
        self.w_corf1.setObjectName(u"w_corf1")
        self.gl_corf1 = QGridLayout(self.w_corf1)
        self.gl_corf1.setObjectName(u"gl_corf1")
        self.gl_corf1.setVerticalSpacing(0)
        self.gl_corf1.setContentsMargins(0, 0, 0, 0)
        self.l_corf1_path = QLabel(self.w_corf1)
        self.l_corf1_path.setObjectName(u"l_corf1_path")
        self.l_corf1_path.setFont(font)

        self.gl_corf1.addWidget(self.l_corf1_path, 1, 0, 1, 1)

        self.cb_corf1 = QCheckBox(self.w_corf1)
        self.cb_corf1.setObjectName(u"cb_corf1")

        self.gl_corf1.addWidget(self.cb_corf1, 0, 0, 1, 1)


        self.gl_main.addWidget(self.w_corf1, 4, 0, 1, 1)

        self.w_printers = QWidget(PrintDocxWindow)
        self.w_printers.setObjectName(u"w_printers")
        self.hl_printers = QHBoxLayout(self.w_printers)
        self.hl_printers.setSpacing(3)
        self.hl_printers.setObjectName(u"hl_printers")
        self.hl_printers.setContentsMargins(0, 0, 0, 0)
        self.cmb_printers = QComboBox(self.w_printers)
        self.cmb_printers.setObjectName(u"cmb_printers")
        self.cmb_printers.setEnabled(True)
        self.cmb_printers.setMinimumSize(QSize(0, 22))

        self.hl_printers.addWidget(self.cmb_printers)

        self.pb_refresh_printers = QPushButton(self.w_printers)
        self.pb_refresh_printers.setObjectName(u"pb_refresh_printers")
        self.pb_refresh_printers.setEnabled(True)
        self.pb_refresh_printers.setMinimumSize(QSize(22, 22))
        self.pb_refresh_printers.setMaximumSize(QSize(22, 22))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/refresh.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_refresh_printers.setIcon(icon1)
        self.pb_refresh_printers.setIconSize(QSize(16, 16))

        self.hl_printers.addWidget(self.pb_refresh_printers)


        self.gl_main.addWidget(self.w_printers, 15, 0, 1, 2)

        self.w_corf2 = QWidget(PrintDocxWindow)
        self.w_corf2.setObjectName(u"w_corf2")
        self.gl_corf2 = QGridLayout(self.w_corf2)
        self.gl_corf2.setObjectName(u"gl_corf2")
        self.gl_corf2.setVerticalSpacing(0)
        self.gl_corf2.setContentsMargins(0, 0, 0, 0)
        self.l_corf2_path = QLabel(self.w_corf2)
        self.l_corf2_path.setObjectName(u"l_corf2_path")
        self.l_corf2_path.setFont(font)

        self.gl_corf2.addWidget(self.l_corf2_path, 1, 0, 1, 1)

        self.cb_corf2 = QCheckBox(self.w_corf2)
        self.cb_corf2.setObjectName(u"cb_corf2")

        self.gl_corf2.addWidget(self.cb_corf2, 0, 0, 1, 1)


        self.gl_main.addWidget(self.w_corf2, 5, 0, 1, 1)

        self.l_choose_docs = QLabel(PrintDocxWindow)
        self.l_choose_docs.setObjectName(u"l_choose_docs")

        self.gl_main.addWidget(self.l_choose_docs, 0, 0, 1, 2)

        self.pb_print = QPushButton(PrintDocxWindow)
        self.pb_print.setObjectName(u"pb_print")
        self.pb_print.setMinimumSize(QSize(0, 22))
        self.pb_print.setMaximumSize(QSize(16777215, 22))

        self.gl_main.addWidget(self.pb_print, 16, 0, 1, 2)

        self.l_choose_printer = QLabel(PrintDocxWindow)
        self.l_choose_printer.setObjectName(u"l_choose_printer")

        self.gl_main.addWidget(self.l_choose_printer, 14, 0, 1, 1)

        self.sb_contract_count = QSpinBox(PrintDocxWindow)
        self.sb_contract_count.setObjectName(u"sb_contract_count")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sb_contract_count.sizePolicy().hasHeightForWidth())
        self.sb_contract_count.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.sb_contract_count, 1, 1, 1, 1)

        self.sb_coef_count = QSpinBox(PrintDocxWindow)
        self.sb_coef_count.setObjectName(u"sb_coef_count")
        sizePolicy.setHeightForWidth(self.sb_coef_count.sizePolicy().hasHeightForWidth())
        self.sb_coef_count.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.sb_coef_count, 3, 1, 1, 1)

        self.sb_corf1_count = QSpinBox(PrintDocxWindow)
        self.sb_corf1_count.setObjectName(u"sb_corf1_count")
        sizePolicy.setHeightForWidth(self.sb_corf1_count.sizePolicy().hasHeightForWidth())
        self.sb_corf1_count.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.sb_corf1_count, 4, 1, 1, 1)

        self.sb_act_count = QSpinBox(PrintDocxWindow)
        self.sb_act_count.setObjectName(u"sb_act_count")
        sizePolicy.setHeightForWidth(self.sb_act_count.sizePolicy().hasHeightForWidth())
        self.sb_act_count.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.sb_act_count, 2, 1, 1, 1)

        self.sb_corf2_count = QSpinBox(PrintDocxWindow)
        self.sb_corf2_count.setObjectName(u"sb_corf2_count")
        sizePolicy.setHeightForWidth(self.sb_corf2_count.sizePolicy().hasHeightForWidth())
        self.sb_corf2_count.setSizePolicy(sizePolicy)

        self.gl_main.addWidget(self.sb_corf2_count, 5, 1, 1, 1)


        self.retranslateUi(PrintDocxWindow)

        QMetaObject.connectSlotsByName(PrintDocxWindow)
    # setupUi

    def retranslateUi(self, PrintDocxWindow):
        PrintDocxWindow.setWindowTitle(QCoreApplication.translate("PrintDocxWindow", u"\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c", None))
        self.cb_contract.setText(QCoreApplication.translate("PrintDocxWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440 \u043e\u0431 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0438 \u044e\u0440\u0438\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0443\u0441\u043b\u0443\u0433", None))
        self.l_contract_path.setText(QCoreApplication.translate("PrintDocxWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.l_coef_path.setText(QCoreApplication.translate("PrintDocxWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.cb_coef.setText(QCoreApplication.translate("PrintDocxWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043e\u0440\u0434\u0435\u0440", None))
        self.l_act_path.setText(QCoreApplication.translate("PrintDocxWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.cb_act.setText(QCoreApplication.translate("PrintDocxWindow", u"\u0410\u043a\u0442 \u043d\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u0435 \u0440\u0430\u0431\u043e\u0442-\u0443\u0441\u043b\u0443\u0433", None))
        self.l_corf1_path.setText(QCoreApplication.translate("PrintDocxWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.cb_corf1.setText(QCoreApplication.translate("PrintDocxWindow", u"\u041f\u0440\u0438\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043e\u0440\u0434\u0435\u0440 1", None))
#if QT_CONFIG(tooltip)
        self.pb_refresh_printers.setToolTip(QCoreApplication.translate("PrintDocxWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.l_corf2_path.setText(QCoreApplication.translate("PrintDocxWindow", u"\u041f\u0443\u0442\u044c:", None))
        self.cb_corf2.setText(QCoreApplication.translate("PrintDocxWindow", u"\u041f\u0440\u0438\u0445\u043e\u0434\u043d\u044b\u0439 \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043e\u0440\u0434\u0435\u0440 2", None))
        self.l_choose_docs.setText(QCoreApplication.translate("PrintDocxWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u0434\u043b\u044f \u043f\u0435\u0447\u0430\u0442\u0438", None))
        self.pb_print.setText(QCoreApplication.translate("PrintDocxWindow", u"\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c", None))
        self.l_choose_printer.setText(QCoreApplication.translate("PrintDocxWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0440\u0438\u043d\u0442\u0435\u0440", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WordPreviewWindow.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QLabel, QScrollArea,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_WordPreviewWindow(object):
    def setupUi(self, WordPreviewWindow):
        if not WordPreviewWindow.objectName():
            WordPreviewWindow.setObjectName(u"WordPreviewWindow")
        WordPreviewWindow.resize(800, 640)
        icon = QIcon()
        icon.addFile(u":/images/pngs/main-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        WordPreviewWindow.setWindowIcon(icon)
        self.vl_main = QVBoxLayout(WordPreviewWindow)
        self.vl_main.setSpacing(0)
        self.vl_main.setObjectName(u"vl_main")
        self.vl_main.setContentsMargins(0, 0, 0, 0)
        self.sa_docx_html_preview = QScrollArea(WordPreviewWindow)
        self.sa_docx_html_preview.setObjectName(u"sa_docx_html_preview")
        self.sa_docx_html_preview.setFocusPolicy(Qt.WheelFocus)
        self.sa_docx_html_preview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.sa_docx_html_preview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.sa_docx_html_preview.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.sa_docx_html_preview.setWidgetResizable(True)
        self.w1_docx_html_preview = QWidget()
        self.w1_docx_html_preview.setObjectName(u"w1_docx_html_preview")
        self.w1_docx_html_preview.setGeometry(QRect(0, 0, 785, 7850))
        self.w1_docx_html_preview.setStyleSheet(u"margin: 36px 56px;")
        self.v1_docx_html_preview = QVBoxLayout(self.w1_docx_html_preview)
        self.v1_docx_html_preview.setSpacing(0)
        self.v1_docx_html_preview.setObjectName(u"v1_docx_html_preview")
        self.v1_docx_html_preview.setContentsMargins(0, 0, 0, 0)
        self.w2_docx_html_preview = QWidget(self.w1_docx_html_preview)
        self.w2_docx_html_preview.setObjectName(u"w2_docx_html_preview")
        self.w2_docx_html_preview.setStyleSheet(u"background-color: white;")
        self.vl2_docx_html_preview = QVBoxLayout(self.w2_docx_html_preview)
        self.vl2_docx_html_preview.setSpacing(0)
        self.vl2_docx_html_preview.setObjectName(u"vl2_docx_html_preview")
        self.vl2_docx_html_preview.setContentsMargins(0, 0, 0, 0)
        self.te_docx_html_preview = QTextEdit(self.w2_docx_html_preview)
        self.te_docx_html_preview.setObjectName(u"te_docx_html_preview")
        self.te_docx_html_preview.setEnabled(True)
        self.te_docx_html_preview.setMinimumSize(QSize(0, 7850))
        self.te_docx_html_preview.setFocusPolicy(Qt.NoFocus)
        self.te_docx_html_preview.setStyleSheet(u"background-color: white; color: black; padding: 12px 48px; border: 0;")
        self.te_docx_html_preview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.te_docx_html_preview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.te_docx_html_preview.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.te_docx_html_preview.setReadOnly(True)

        self.vl2_docx_html_preview.addWidget(self.te_docx_html_preview)


        self.v1_docx_html_preview.addWidget(self.w2_docx_html_preview)

        self.sa_docx_html_preview.setWidget(self.w1_docx_html_preview)

        self.vl_main.addWidget(self.sa_docx_html_preview)

        self.l_description = QLabel(WordPreviewWindow)
        self.l_description.setObjectName(u"l_description")
        self.l_description.setStyleSheet(u"color: gray; font-size: 11px;")
        self.l_description.setAlignment(Qt.AlignCenter)
        self.l_description.setWordWrap(True)
        self.l_description.setMargin(6)

        self.vl_main.addWidget(self.l_description)


        self.retranslateUi(WordPreviewWindow)

        QMetaObject.connectSlotsByName(WordPreviewWindow)
    # setupUi

    def retranslateUi(self, WordPreviewWindow):
        WordPreviewWindow.setWindowTitle(QCoreApplication.translate("WordPreviewWindow", u"\u041f\u0440\u0435\u0432\u044c\u044e", None))
        self.l_description.setText(QCoreApplication.translate("WordPreviewWindow", u"\u0414\u0430\u043d\u043d\u043e\u0435 \u043f\u0440\u0435\u0432\u044c\u044e \u043d\u0435 \u043e\u0442\u0440\u0430\u0436\u0430\u0435\u0442 \u0442\u043e\u0447\u043d\u044b\u0439 \u0432\u0438\u0434 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430. \u042d\u0442\u043e \u043a\u043e\u043d\u0432\u0435\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0432 html \u0432\u0430\u0440\u0438\u0430\u043d\u0442.", None))
    # retranslateUi


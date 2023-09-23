# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(682, 547)
        MainWindow.setMinimumSize(QSize(682, 300))
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/images/pngs/main-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.a_ask_for_delete = QAction(MainWindow)
        self.a_ask_for_delete.setObjectName(u"a_ask_for_delete")
        self.a_ask_for_delete.setCheckable(True)
        self.a_ask_for_delete.setChecked(True)
        self.a_filter_with_hidden_columns = QAction(MainWindow)
        self.a_filter_with_hidden_columns.setObjectName(u"a_filter_with_hidden_columns")
        self.a_filter_with_hidden_columns.setCheckable(True)
        self.a_filter_with_hidden_columns.setChecked(True)
        self.a_show_contract_info = QAction(MainWindow)
        self.a_show_contract_info.setObjectName(u"a_show_contract_info")
        self.a_show_contract_info.setCheckable(True)
        self.a_show_contract_info.setChecked(True)
        self.a_column_0 = QAction(MainWindow)
        self.a_column_0.setObjectName(u"a_column_0")
        self.a_column_0.setCheckable(True)
        self.a_column_1 = QAction(MainWindow)
        self.a_column_1.setObjectName(u"a_column_1")
        self.a_column_1.setCheckable(True)
        self.a_column_2 = QAction(MainWindow)
        self.a_column_2.setObjectName(u"a_column_2")
        self.a_column_2.setCheckable(True)
        self.a_column_3 = QAction(MainWindow)
        self.a_column_3.setObjectName(u"a_column_3")
        self.a_column_3.setCheckable(True)
        self.a_column_4 = QAction(MainWindow)
        self.a_column_4.setObjectName(u"a_column_4")
        self.a_column_4.setCheckable(True)
        self.a_column_6 = QAction(MainWindow)
        self.a_column_6.setObjectName(u"a_column_6")
        self.a_column_6.setCheckable(True)
        self.a_column_7 = QAction(MainWindow)
        self.a_column_7.setObjectName(u"a_column_7")
        self.a_column_7.setCheckable(True)
        self.a_column_8 = QAction(MainWindow)
        self.a_column_8.setObjectName(u"a_column_8")
        self.a_column_8.setCheckable(True)
        self.a_column_9 = QAction(MainWindow)
        self.a_column_9.setObjectName(u"a_column_9")
        self.a_column_9.setCheckable(True)
        self.a_column_10 = QAction(MainWindow)
        self.a_column_10.setObjectName(u"a_column_10")
        self.a_column_10.setCheckable(True)
        self.a_column_12 = QAction(MainWindow)
        self.a_column_12.setObjectName(u"a_column_12")
        self.a_column_12.setCheckable(True)
        self.a_column_13 = QAction(MainWindow)
        self.a_column_13.setObjectName(u"a_column_13")
        self.a_column_13.setCheckable(True)
        self.a_column_5 = QAction(MainWindow)
        self.a_column_5.setObjectName(u"a_column_5")
        self.a_column_5.setCheckable(True)
        self.a_column_11 = QAction(MainWindow)
        self.a_column_11.setObjectName(u"a_column_11")
        self.a_column_11.setCheckable(True)
        self.w_main = QWidget(MainWindow)
        self.w_main.setObjectName(u"w_main")
        self.gl_main = QGridLayout(self.w_main)
        self.gl_main.setObjectName(u"gl_main")
        self.gl_main.setHorizontalSpacing(6)
        self.gl_main.setVerticalSpacing(0)
        self.w_toolbar = QWidget(self.w_main)
        self.w_toolbar.setObjectName(u"w_toolbar")
        self.w_toolbar.setMinimumSize(QSize(0, 35))
        self.w_toolbar.setMaximumSize(QSize(16777215, 35))
        self.hl_toolbar = QHBoxLayout(self.w_toolbar)
        self.hl_toolbar.setSpacing(3)
        self.hl_toolbar.setObjectName(u"hl_toolbar")
        self.hl_toolbar.setContentsMargins(0, 0, 0, 0)
        self.pb_create = QPushButton(self.w_toolbar)
        self.pb_create.setObjectName(u"pb_create")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(36)
        sizePolicy.setVerticalStretch(36)
        sizePolicy.setHeightForWidth(self.pb_create.sizePolicy().hasHeightForWidth())
        self.pb_create.setSizePolicy(sizePolicy)
        self.pb_create.setMinimumSize(QSize(35, 35))
        self.pb_create.setMaximumSize(QSize(35, 35))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/plus.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_create.setIcon(icon1)
        self.pb_create.setIconSize(QSize(18, 18))

        self.hl_toolbar.addWidget(self.pb_create)

        self.pb_delete = QPushButton(self.w_toolbar)
        self.pb_delete.setObjectName(u"pb_delete")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(32)
        sizePolicy1.setVerticalStretch(32)
        sizePolicy1.setHeightForWidth(self.pb_delete.sizePolicy().hasHeightForWidth())
        self.pb_delete.setSizePolicy(sizePolicy1)
        self.pb_delete.setMinimumSize(QSize(35, 35))
        self.pb_delete.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/minus.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_delete.setIcon(icon2)
        self.pb_delete.setIconSize(QSize(18, 18))

        self.hl_toolbar.addWidget(self.pb_delete)

        self.pb_edit = QPushButton(self.w_toolbar)
        self.pb_edit.setObjectName(u"pb_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(33)
        sizePolicy2.setVerticalStretch(32)
        sizePolicy2.setHeightForWidth(self.pb_edit.sizePolicy().hasHeightForWidth())
        self.pb_edit.setSizePolicy(sizePolicy2)
        self.pb_edit.setMinimumSize(QSize(35, 35))
        self.pb_edit.setMaximumSize(QSize(35, 35))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/pencil.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_edit.setIcon(icon3)
        self.pb_edit.setIconSize(QSize(20, 20))

        self.hl_toolbar.addWidget(self.pb_edit)

        self.pb_duplicate = QPushButton(self.w_toolbar)
        self.pb_duplicate.setObjectName(u"pb_duplicate")
        sizePolicy2.setHeightForWidth(self.pb_duplicate.sizePolicy().hasHeightForWidth())
        self.pb_duplicate.setSizePolicy(sizePolicy2)
        self.pb_duplicate.setMinimumSize(QSize(35, 35))
        self.pb_duplicate.setMaximumSize(QSize(35, 35))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/duplicate.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_duplicate.setIcon(icon4)
        self.pb_duplicate.setIconSize(QSize(22, 22))

        self.hl_toolbar.addWidget(self.pb_duplicate)

        self.line_1 = QFrame(self.w_toolbar)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setEnabled(True)
        self.line_1.setFrameShape(QFrame.VLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_1)

        self.pb_open_file = QPushButton(self.w_toolbar)
        self.pb_open_file.setObjectName(u"pb_open_file")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_open_file.sizePolicy().hasHeightForWidth())
        self.pb_open_file.setSizePolicy(sizePolicy3)
        self.pb_open_file.setMinimumSize(QSize(35, 35))
        self.pb_open_file.setMaximumSize(QSize(35, 35))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/open-file.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_open_file.setIcon(icon5)
        self.pb_open_file.setIconSize(QSize(20, 20))

        self.hl_toolbar.addWidget(self.pb_open_file)

        self.pb_open_folder = QPushButton(self.w_toolbar)
        self.pb_open_folder.setObjectName(u"pb_open_folder")
        sizePolicy3.setHeightForWidth(self.pb_open_folder.sizePolicy().hasHeightForWidth())
        self.pb_open_folder.setSizePolicy(sizePolicy3)
        self.pb_open_folder.setMinimumSize(QSize(35, 35))
        self.pb_open_folder.setMaximumSize(QSize(35, 35))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/open-folder.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_open_folder.setIcon(icon6)
        self.pb_open_folder.setIconSize(QSize(24, 24))

        self.hl_toolbar.addWidget(self.pb_open_folder)

        self.pb_edit_contract_addictions = QPushButton(self.w_toolbar)
        self.pb_edit_contract_addictions.setObjectName(u"pb_edit_contract_addictions")
        sizePolicy3.setHeightForWidth(self.pb_edit_contract_addictions.sizePolicy().hasHeightForWidth())
        self.pb_edit_contract_addictions.setSizePolicy(sizePolicy3)
        self.pb_edit_contract_addictions.setMinimumSize(QSize(35, 35))
        self.pb_edit_contract_addictions.setMaximumSize(QSize(35, 35))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/paperclip.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_edit_contract_addictions.setIcon(icon7)
        self.pb_edit_contract_addictions.setIconSize(QSize(22, 22))

        self.hl_toolbar.addWidget(self.pb_edit_contract_addictions)

        self.line_2 = QFrame(self.w_toolbar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_2)

        self.l_filter = QLabel(self.w_toolbar)
        self.l_filter.setObjectName(u"l_filter")
        self.l_filter.setMaximumSize(QSize(24, 24))
        self.l_filter.setStyleSheet(u"background-size: 50%;")
        self.l_filter.setPixmap(QPixmap(u":/icons/icons/filter.ico"))
        self.l_filter.setScaledContents(True)
        self.l_filter.setAlignment(Qt.AlignCenter)

        self.hl_toolbar.addWidget(self.l_filter)

        self.le_filter = QLineEdit(self.w_toolbar)
        self.le_filter.setObjectName(u"le_filter")
        self.le_filter.setMinimumSize(QSize(190, 30))
        self.le_filter.setMaximumSize(QSize(16777215, 30))
        self.le_filter.setStyleSheet(u"padding: 2px; font-size: 11px;")

        self.hl_toolbar.addWidget(self.le_filter)

        self.hs_toolbar = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hl_toolbar.addItem(self.hs_toolbar)

        self.line_3 = QFrame(self.w_toolbar)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setEnabled(True)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_3)

        self.pb_preview_docx = QPushButton(self.w_toolbar)
        self.pb_preview_docx.setObjectName(u"pb_preview_docx")
        sizePolicy3.setHeightForWidth(self.pb_preview_docx.sizePolicy().hasHeightForWidth())
        self.pb_preview_docx.setSizePolicy(sizePolicy3)
        self.pb_preview_docx.setMinimumSize(QSize(35, 35))
        self.pb_preview_docx.setMaximumSize(QSize(35, 35))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/eye.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_preview_docx.setIcon(icon8)
        self.pb_preview_docx.setIconSize(QSize(20, 20))

        self.hl_toolbar.addWidget(self.pb_preview_docx)

        self.pb_export_to_xlsx = QPushButton(self.w_toolbar)
        self.pb_export_to_xlsx.setObjectName(u"pb_export_to_xlsx")
        sizePolicy3.setHeightForWidth(self.pb_export_to_xlsx.sizePolicy().hasHeightForWidth())
        self.pb_export_to_xlsx.setSizePolicy(sizePolicy3)
        self.pb_export_to_xlsx.setMinimumSize(QSize(35, 35))
        self.pb_export_to_xlsx.setMaximumSize(QSize(35, 35))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/excel.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_export_to_xlsx.setIcon(icon9)
        self.pb_export_to_xlsx.setIconSize(QSize(20, 20))

        self.hl_toolbar.addWidget(self.pb_export_to_xlsx)

        self.pb_print = QPushButton(self.w_toolbar)
        self.pb_print.setObjectName(u"pb_print")
        sizePolicy3.setHeightForWidth(self.pb_print.sizePolicy().hasHeightForWidth())
        self.pb_print.setSizePolicy(sizePolicy3)
        self.pb_print.setMinimumSize(QSize(35, 35))
        self.pb_print.setMaximumSize(QSize(35, 35))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/printer.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_print.setIcon(icon10)
        self.pb_print.setIconSize(QSize(22, 22))

        self.hl_toolbar.addWidget(self.pb_print)

        self.line_4 = QFrame(self.w_toolbar)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setEnabled(True)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.hl_toolbar.addWidget(self.line_4)

        self.pb_adjust = QPushButton(self.w_toolbar)
        self.pb_adjust.setObjectName(u"pb_adjust")
        sizePolicy3.setHeightForWidth(self.pb_adjust.sizePolicy().hasHeightForWidth())
        self.pb_adjust.setSizePolicy(sizePolicy3)
        self.pb_adjust.setMinimumSize(QSize(35, 35))
        self.pb_adjust.setMaximumSize(QSize(35, 35))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/zoom.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_adjust.setIcon(icon11)
        self.pb_adjust.setIconSize(QSize(32, 32))

        self.hl_toolbar.addWidget(self.pb_adjust)


        self.gl_main.addWidget(self.w_toolbar, 0, 0, 1, 2)

        self.l_contract_info = QLabel(self.w_main)
        self.l_contract_info.setObjectName(u"l_contract_info")
        font = QFont()
        font.setPointSize(9)
        self.l_contract_info.setFont(font)
        self.l_contract_info.setStyleSheet(u"margin-bottom: 3px;")

        self.gl_main.addWidget(self.l_contract_info, 1, 1, 1, 1)

        self.l_contracts = QLabel(self.w_main)
        self.l_contracts.setObjectName(u"l_contracts")
        self.l_contracts.setFont(font)
        self.l_contracts.setStyleSheet(u"margin-bottom: 3px;")

        self.gl_main.addWidget(self.l_contracts, 1, 0, 1, 1)

        self.tw_contracts = QTableWidget(self.w_main)
        if (self.tw_contracts.columnCount() < 14):
            self.tw_contracts.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tw_contracts.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        self.tw_contracts.setObjectName(u"tw_contracts")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tw_contracts.sizePolicy().hasHeightForWidth())
        self.tw_contracts.setSizePolicy(sizePolicy4)
        self.tw_contracts.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tw_contracts.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_contracts.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tw_contracts.setSortingEnabled(True)
        self.tw_contracts.setWordWrap(False)
        self.tw_contracts.horizontalHeader().setMinimumSectionSize(22)
        self.tw_contracts.horizontalHeader().setDefaultSectionSize(150)
        self.tw_contracts.horizontalHeader().setProperty("showSortIndicator", True)
        self.tw_contracts.horizontalHeader().setStretchLastSection(True)
        self.tw_contracts.verticalHeader().setVisible(False)

        self.gl_main.addWidget(self.tw_contracts, 2, 0, 1, 1)

        self.te_contract_info = QTextEdit(self.w_main)
        self.te_contract_info.setObjectName(u"te_contract_info")
        self.te_contract_info.setMaximumSize(QSize(200, 16777215))
        self.te_contract_info.setLineWrapMode(QTextEdit.WidgetWidth)
        self.te_contract_info.setReadOnly(True)

        self.gl_main.addWidget(self.te_contract_info, 2, 1, 1, 1)

        MainWindow.setCentralWidget(self.w_main)
        self.menu = QMenuBar(MainWindow)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 682, 18))
        self.m_settings = QMenu(self.menu)
        self.m_settings.setObjectName(u"m_settings")
        MainWindow.setMenuBar(self.menu)
        QWidget.setTabOrder(self.pb_create, self.pb_delete)
        QWidget.setTabOrder(self.pb_delete, self.pb_duplicate)
        QWidget.setTabOrder(self.pb_duplicate, self.pb_open_file)
        QWidget.setTabOrder(self.pb_open_file, self.pb_open_folder)
        QWidget.setTabOrder(self.pb_open_folder, self.pb_edit_contract_addictions)
        QWidget.setTabOrder(self.pb_edit_contract_addictions, self.pb_preview_docx)
        QWidget.setTabOrder(self.pb_preview_docx, self.pb_export_to_xlsx)
        QWidget.setTabOrder(self.pb_export_to_xlsx, self.pb_adjust)
        QWidget.setTabOrder(self.pb_adjust, self.le_filter)
        QWidget.setTabOrder(self.le_filter, self.tw_contracts)
        QWidget.setTabOrder(self.tw_contracts, self.te_contract_info)

        self.menu.addAction(self.m_settings.menuAction())
        self.m_settings.addAction(self.a_ask_for_delete)
        self.m_settings.addAction(self.a_filter_with_hidden_columns)
        self.m_settings.addAction(self.a_show_contract_info)
        self.m_settings.addSeparator()
        self.m_settings.addAction(self.a_column_0)
        self.m_settings.addAction(self.a_column_1)
        self.m_settings.addAction(self.a_column_2)
        self.m_settings.addAction(self.a_column_3)
        self.m_settings.addAction(self.a_column_4)
        self.m_settings.addAction(self.a_column_5)
        self.m_settings.addAction(self.a_column_6)
        self.m_settings.addAction(self.a_column_7)
        self.m_settings.addAction(self.a_column_8)
        self.m_settings.addAction(self.a_column_9)
        self.m_settings.addAction(self.a_column_10)
        self.m_settings.addAction(self.a_column_11)
        self.m_settings.addAction(self.a_column_12)
        self.m_settings.addAction(self.a_column_13)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a \u044e\u0440\u0438\u0441\u0442\u0430", None))
        self.a_ask_for_delete.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0448\u0438\u0432\u0430\u0442\u044c \u043f\u0440\u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0438", None))
        self.a_filter_with_hidden_columns.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u044b\u0435 \u0441\u0442\u043e\u043b\u0431\u0446\u044b \u043f\u0440\u0438 \u0444\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u0438", None))
        self.a_show_contract_info.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e", None))
        self.a_column_0.setText(QCoreApplication.translate("MainWindow", u"\u2116", None))
        self.a_column_1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430", None))
        self.a_column_2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None))
        self.a_column_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f", None))
        self.a_column_4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.a_column_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.a_column_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.a_column_8.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.a_column_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043e\u043f\u043b\u0430\u0442\u0430", None))
        self.a_column_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043b\u0430\u0442\u0430", None))
        self.a_column_12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.a_column_13.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.a_column_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.a_column_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0434\u0435\u043b\u0430", None))
#if QT_CONFIG(tooltip)
        self.pb_create.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_create.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_delete.setToolTip(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_delete.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_edit.setToolTip(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_edit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_duplicate.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u043e \u043e\u0431\u0440\u0430\u0437\u0446\u0443", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_duplicate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_open_file.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_open_file.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_open_folder.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0432 \u043f\u0440\u043e\u0432\u043e\u0434\u043d\u0438\u043a\u0435", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_open_folder.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pb_edit_contract_addictions.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.pb_edit_contract_addictions.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.l_filter.setText("")
        self.le_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
#if QT_CONFIG(tooltip)
        self.pb_preview_docx.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0432\u044c\u044e \u0444\u0430\u0439\u043b\u0430 Word", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_export_to_xlsx.setToolTip(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u0440\u0442 \u0432 Excel", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_print.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u0442\u0435\u0440", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_adjust.setToolTip(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0430\u0432\u043d\u044f\u0442\u044c \u0442\u0430\u0431\u043b\u0438\u0446\u0443 \u043f\u043e \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u043c\u0443", None))
#endif // QT_CONFIG(tooltip)
        self.l_contract_info.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.l_contracts.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0442\u0440\u0430\u043a\u0442\u044b", None))
        ___qtablewidgetitem = self.tw_contracts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u2116", None));
        ___qtablewidgetitem1 = self.tw_contracts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u0443\u0433\u0430", None));
        ___qtablewidgetitem2 = self.tw_contracts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a", None));
        ___qtablewidgetitem3 = self.tw_contracts.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem4 = self.tw_contracts.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u0441\u0442\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None));
        ___qtablewidgetitem5 = self.tw_contracts.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None));
        ___qtablewidgetitem6 = self.tw_contracts.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None));
        ___qtablewidgetitem7 = self.tw_contracts.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem8 = self.tw_contracts.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0438", None));
        ___qtablewidgetitem9 = self.tw_contracts.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043e\u043f\u043b\u0430\u0442\u0430", None));
        ___qtablewidgetitem10 = self.tw_contracts.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043b\u0430\u0442\u0430", None));
        ___qtablewidgetitem11 = self.tw_contracts.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u0434\u0435\u043b\u0430", None));
        ___qtablewidgetitem12 = self.tw_contracts.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430", None));
        ___qtablewidgetitem13 = self.tw_contracts.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None));
        self.te_contract_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>", None))
        self.te_contract_info.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0427\u0442\u043e\u0431\u044b \u043e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c \u043f\u043e\u0434\u0440\u043e\u0431\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e, \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u043e\u043d\u0442\u0440\u0430\u043a\u0442.", None))
        self.m_settings.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi


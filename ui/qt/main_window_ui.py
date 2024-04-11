# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1022, 643)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.horizontalLayoutWidget = QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon = QIcon()
        icon.addFile(u"resources/Nova_logo2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(25, 25))
        self.pushButton_3.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_setting = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_setting.setObjectName(u"pushButton_setting")
        icon1 = QIcon()
        icon1.addFile(u"resources/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_setting.setIcon(icon1)
        self.pushButton_setting.setIconSize(QSize(25, 25))
        self.pushButton_setting.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton_setting)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.listWidget = QListWidget(self.horizontalLayoutWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_3.addWidget(self.listWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_chat_content = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_chat_content.setObjectName(u"lineEdit_chat_content")

        self.horizontalLayout_2.addWidget(self.lineEdit_chat_content)

        self.pushButton_chat_send = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_chat_send.setObjectName(u"pushButton_chat_send")

        self.horizontalLayout_2.addWidget(self.pushButton_chat_send)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.splitter.addWidget(self.horizontalLayoutWidget)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_plan = QPushButton(self.verticalLayoutWidget)
        self.pushButton_plan.setObjectName(u"pushButton_plan")
        icon2 = QIcon()
        icon2.addFile(u"resources/planner.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_plan.setIcon(icon2)
        self.pushButton_plan.setIconSize(QSize(25, 25))
        self.pushButton_plan.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_plan)

        self.pushButton_code = QPushButton(self.verticalLayoutWidget)
        self.pushButton_code.setObjectName(u"pushButton_code")
        icon3 = QIcon()
        icon3.addFile(u"resources/code.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_code.setIcon(icon3)
        self.pushButton_code.setIconSize(QSize(25, 25))
        self.pushButton_code.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_code)

        self.pushButton_browse = QPushButton(self.verticalLayoutWidget)
        self.pushButton_browse.setObjectName(u"pushButton_browse")
        icon4 = QIcon()
        icon4.addFile(u"resources/browser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_browse.setIcon(icon4)
        self.pushButton_browse.setIconSize(QSize(25, 25))
        self.pushButton_browse.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_browse)

        self.pushButton_cmd = QPushButton(self.verticalLayoutWidget)
        self.pushButton_cmd.setObjectName(u"pushButton_cmd")
        icon5 = QIcon()
        icon5.addFile(u"resources/cmd.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_cmd.setIcon(icon5)
        self.pushButton_cmd.setIconSize(QSize(25, 25))
        self.pushButton_cmd.setFlat(True)

        self.horizontalLayout_3.addWidget(self.pushButton_cmd)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.stackedWidget = QStackedWidget(self.verticalLayoutWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_code = QWidget()
        self.page_code.setObjectName(u"page_code")
        self.stackedWidget.addWidget(self.page_code)
        self.page_plan = QWidget()
        self.page_plan.setObjectName(u"page_plan")
        self.stackedWidget.addWidget(self.page_plan)
        self.page_browser = QWidget()
        self.page_browser.setObjectName(u"page_browser")
        self.stackedWidget.addWidget(self.page_browser)
        self.page_cmd = QWidget()
        self.page_cmd.setObjectName(u"page_cmd")
        self.stackedWidget.addWidget(self.page_cmd)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.splitter.addWidget(self.verticalLayoutWidget)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1022, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nova", None))
        self.pushButton_3.setText("")
        self.pushButton_setting.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Chat", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem5 = self.listWidget.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_chat_send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.pushButton_plan.setText(QCoreApplication.translate("MainWindow", u" Plan", None))
        self.pushButton_code.setText(QCoreApplication.translate("MainWindow", u" Code", None))
#if QT_CONFIG(shortcut)
        self.pushButton_code.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButton_browse.setText(QCoreApplication.translate("MainWindow", u" Browser", None))
        self.pushButton_cmd.setText(QCoreApplication.translate("MainWindow", u" CMD", None))
#if QT_CONFIG(tooltip)
        self.stackedWidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.stackedWidget.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Setting</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi


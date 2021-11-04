from PySide6 import QtGui
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from icon import Icon
import base64
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"热度图生成器")
        MainWindow.resize(918, 538)
        with open('tmp.ico', 'wb') as tmp:
            tmp.write(base64.b64decode(Icon().img))
        MainWindow.setWindowIcon(QtGui.QIcon('tmp.ico'))
        os.remove('tmp.ico')
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.excelButton = QPushButton(self.centralwidget)
        self.excelButton.setObjectName(u"excelButton")

        self.horizontalLayout.addWidget(self.excelButton)

        self.horizontalSpacer = QSpacerItem(808, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(828, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)
        self.saveButton.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.saveButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.saveButton)


        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"热度图生成器", None))
        self.excelButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00Excel", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u4fdd \u5b58", None))
    # retranslateUi
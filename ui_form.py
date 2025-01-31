# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test1.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QGroupBox, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(670, 502)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(670, 490))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)

        self.gridLayout_2.addWidget(self.checkBox_2, 0, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font)

        self.gridLayout_2.addWidget(self.checkBox_4, 1, 0, 1, 1)

        self.checkBox_5 = QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font)

        self.gridLayout_2.addWidget(self.checkBox_5, 1, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font)

        self.gridLayout_2.addWidget(self.checkBox_3, 0, 2, 1, 1)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 2, 2, 2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(3)
        sizePolicy2.setVerticalStretch(4)
        sizePolicy2.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 0, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_2.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.lineEdit_2.setFont(font1)

        self.gridLayout_4.addWidget(self.lineEdit_2, 1, 0, 1, 2)

        self.tcp_status_label = QLabel(self.centralwidget)
        self.tcp_status_label.setObjectName(u"tcp_status_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.tcp_status_label.sizePolicy().hasHeightForWidth())
        self.tcp_status_label.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        self.tcp_status_label.setFont(font2)
        self.tcp_status_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tcp_status_label, 2, 0, 1, 2)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_9, 2, 2, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font)

        self.gridLayout_4.addWidget(self.label_2, 3, 2, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.lineEdit, 3, 3, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 4, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(3)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(True)
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.checkBox1 = QCheckBox(self.groupBox_2)
        self.checkBox1.setObjectName(u"checkBox1")

        self.gridLayout.addWidget(self.checkBox1, 0, 0, 1, 1)

        self.checkBox2 = QCheckBox(self.groupBox_2)
        self.checkBox2.setObjectName(u"checkBox2")

        self.gridLayout.addWidget(self.checkBox2, 0, 1, 1, 1)

        self.checkBox3 = QCheckBox(self.groupBox_2)
        self.checkBox3.setObjectName(u"checkBox3")

        self.gridLayout.addWidget(self.checkBox3, 1, 0, 1, 1)

        self.checkBox4 = QCheckBox(self.groupBox_2)
        self.checkBox4.setObjectName(u"checkBox4")

        self.gridLayout.addWidget(self.checkBox4, 1, 1, 1, 1)

        self.checkBox5 = QCheckBox(self.groupBox_2)
        self.checkBox5.setObjectName(u"checkBox5")

        self.gridLayout.addWidget(self.checkBox5, 2, 0, 1, 1)

        self.checkBox6 = QCheckBox(self.groupBox_2)
        self.checkBox6.setObjectName(u"checkBox6")

        self.gridLayout.addWidget(self.checkBox6, 2, 1, 1, 1)

        self.checkBox7 = QCheckBox(self.groupBox_2)
        self.checkBox7.setObjectName(u"checkBox7")

        self.gridLayout.addWidget(self.checkBox7, 3, 0, 1, 1)

        self.checkBox8 = QCheckBox(self.groupBox_2)
        self.checkBox8.setObjectName(u"checkBox8")

        self.gridLayout.addWidget(self.checkBox8, 3, 1, 1, 1)

        self.checkBox9 = QCheckBox(self.groupBox_2)
        self.checkBox9.setObjectName(u"checkBox9")

        self.gridLayout.addWidget(self.checkBox9, 4, 0, 1, 1)

        self.checkBox10 = QCheckBox(self.groupBox_2)
        self.checkBox10.setObjectName(u"checkBox10")

        self.gridLayout.addWidget(self.checkBox10, 4, 1, 1, 1)

        self.checkBox11 = QCheckBox(self.groupBox_2)
        self.checkBox11.setObjectName(u"checkBox11")

        self.gridLayout.addWidget(self.checkBox11, 5, 0, 1, 1)

        self.checkBox12 = QCheckBox(self.groupBox_2)
        self.checkBox12.setObjectName(u"checkBox12")

        self.gridLayout.addWidget(self.checkBox12, 5, 1, 1, 1)

        self.all_load = QPushButton(self.groupBox_2)
        self.all_load.setObjectName(u"all_load")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.all_load.sizePolicy().hasHeightForWidth())
        self.all_load.setSizePolicy(sizePolicy5)
        self.all_load.setFont(font)

        self.gridLayout.addWidget(self.all_load, 6, 0, 1, 1)

        self.all_write = QPushButton(self.groupBox_2)
        self.all_write.setObjectName(u"all_write")
        sizePolicy5.setHeightForWidth(self.all_write.sizePolicy().hasHeightForWidth())
        self.all_write.setSizePolicy(sizePolicy5)
        self.all_write.setFont(font)

        self.gridLayout.addWidget(self.all_write, 6, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 4, 2, 4, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font)

        self.gridLayout_4.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font)

        self.gridLayout_4.addWidget(self.label_6, 7, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.label_11, 8, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setFont(font)

        self.gridLayout_4.addWidget(self.label_7, 9, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy2)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.lineEdit_3.setPalette(palette1)
        self.lineEdit_3.setFont(font1)

        self.gridLayout_4.addWidget(self.lineEdit_3, 5, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 670, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Restore revisioned", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"T-CON Board Restore", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"EEPROM", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Encoding", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckPID", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"NAND", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.tcp_status_label.setText(QCoreApplication.translate("MainWindow", u"0ms - Please Connect T-Con Zig", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Please Connect I2C Board", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Panel ID", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Model Info", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"FHD", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"FHD_RO", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"QHD_RO", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"UHD", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"UHD_RO", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"WUHD_RO", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Data Restore", None))
        self.checkBox1.setText(QCoreApplication.translate("MainWindow", u"Parameter", None))
        self.checkBox2.setText(QCoreApplication.translate("MainWindow", u"OLSB", None))
        self.checkBox3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox8.setText(QCoreApplication.translate("MainWindow", u"YB", None))
        self.checkBox9.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox10.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox11.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox12.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.all_load.setText(QCoreApplication.translate("MainWindow", u"Sel. Load", None))
        self.all_write.setText(QCoreApplication.translate("MainWindow", u"Sel. Write", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"NAND", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"EEPROM", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Elspsed Time - 00 :00", None))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
    # retranslateUi


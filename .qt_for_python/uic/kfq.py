# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kfq.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 398)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pbtn_start_server = QPushButton(self.centralwidget)
        self.pbtn_start_server.setObjectName(u"pbtn_start_server")
        self.pbtn_start_server.setGeometry(QRect(130, 20, 661, 29))
        self.pbtn_start_server.setCursor(QCursor(Qt.PointingHandCursor))
        self.n_8 = QLabel(self.centralwidget)
        self.n_8.setObjectName(u"n_8")
        self.n_8.setGeometry(QRect(130, 60, 69, 20))
        self.cbox_using_java = QComboBox(self.centralwidget)
        self.cbox_using_java.addItem("")
        self.cbox_using_java.addItem("")
        self.cbox_using_java.addItem("")
        self.cbox_using_java.setObjectName(u"cbox_using_java")
        self.cbox_using_java.setGeometry(QRect(210, 60, 87, 26))
        self.cbox_using_java.setCursor(QCursor(Qt.PointingHandCursor))
        self.n_2 = QLabel(self.centralwidget)
        self.n_2.setObjectName(u"n_2")
        self.n_2.setGeometry(QRect(130, 360, 151, 20))
        self.cbox_want_to_download = QComboBox(self.centralwidget)
        self.cbox_want_to_download.addItem("")
        self.cbox_want_to_download.addItem("")
        self.cbox_want_to_download.addItem("")
        self.cbox_want_to_download.addItem("")
        self.cbox_want_to_download.setObjectName(u"cbox_want_to_download")
        self.cbox_want_to_download.setGeometry(QRect(290, 360, 87, 26))
        self.pbtn_how_to_choice = QPushButton(self.centralwidget)
        self.pbtn_how_to_choice.setObjectName(u"pbtn_how_to_choice")
        self.pbtn_how_to_choice.setGeometry(QRect(380, 360, 93, 29))
        self.n_1 = QLabel(self.centralwidget)
        self.n_1.setObjectName(u"n_1")
        self.n_1.setGeometry(QRect(130, 90, 91, 20))
        self.label_path = QLabel(self.centralwidget)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setGeometry(QRect(220, 90, 461, 20))
        self.pbtn_download_server = QPushButton(self.centralwidget)
        self.pbtn_download_server.setObjectName(u"pbtn_download_server")
        self.pbtn_download_server.setGeometry(QRect(690, 80, 51, 31))
        self.pbtn_download_server.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_select_path = QPushButton(self.centralwidget)
        self.pbtn_select_path.setObjectName(u"pbtn_select_path")
        self.pbtn_select_path.setGeometry(QRect(740, 90, 21, 21))
        self.pbtn_select_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.n_3 = QLabel(self.centralwidget)
        self.n_3.setObjectName(u"n_3")
        self.n_3.setGeometry(QRect(130, 140, 69, 20))
        self.n_4 = QLabel(self.centralwidget)
        self.n_4.setObjectName(u"n_4")
        self.n_4.setGeometry(QRect(248, 140, 111, 20))
        self.n_5 = QLabel(self.centralwidget)
        self.n_5.setObjectName(u"n_5")
        self.n_5.setGeometry(QRect(400, 140, 69, 20))
        self.pbtn_dis_log4j2 = QPushButton(self.centralwidget)
        self.pbtn_dis_log4j2.setObjectName(u"pbtn_dis_log4j2")
        self.pbtn_dis_log4j2.setGeometry(QRect(440, 140, 341, 29))
        self.pbtn_dis_log4j2.setCursor(QCursor(Qt.PointingHandCursor))
        self.n_7 = QLabel(self.centralwidget)
        self.n_7.setObjectName(u"n_7")
        self.n_7.setGeometry(QRect(130, 190, 69, 20))
        self.cbox_mojang = QComboBox(self.centralwidget)
        self.cbox_mojang.addItem("")
        self.cbox_mojang.addItem("")
        self.cbox_mojang.setObjectName(u"cbox_mojang")
        self.cbox_mojang.setGeometry(QRect(200, 190, 71, 26))
        self.cbox_mojang.setCursor(QCursor(Qt.PointingHandCursor))
        self.n_6 = QLabel(self.centralwidget)
        self.n_6.setObjectName(u"n_6")
        self.n_6.setGeometry(QRect(290, 190, 101, 20))
        self.max_player = QLineEdit(self.centralwidget)
        self.max_player.setObjectName(u"max_player")
        self.max_player.setGeometry(QRect(390, 190, 113, 25))
        self.n_9 = QLabel(self.centralwidget)
        self.n_9.setObjectName(u"n_9")
        self.n_9.setGeometry(QRect(510, 190, 91, 20))
        self.server_port = QLineEdit(self.centralwidget)
        self.server_port.setObjectName(u"server_port")
        self.server_port.setGeometry(QRect(610, 190, 113, 25))
        self.n_10 = QLabel(self.centralwidget)
        self.n_10.setObjectName(u"n_10")
        self.n_10.setGeometry(QRect(130, 220, 69, 20))
        self.cbox_pvp = QComboBox(self.centralwidget)
        self.cbox_pvp.addItem("")
        self.cbox_pvp.addItem("")
        self.cbox_pvp.setObjectName(u"cbox_pvp")
        self.cbox_pvp.setGeometry(QRect(200, 220, 71, 26))
        self.cbox_pvp.setCursor(QCursor(Qt.PointingHandCursor))
        self.n_11 = QLabel(self.centralwidget)
        self.n_11.setObjectName(u"n_11")
        self.n_11.setGeometry(QRect(290, 220, 69, 20))
        self.cbox_command_block = QComboBox(self.centralwidget)
        self.cbox_command_block.addItem("")
        self.cbox_command_block.addItem("")
        self.cbox_command_block.setObjectName(u"cbox_command_block")
        self.cbox_command_block.setGeometry(QRect(360, 220, 71, 26))
        self.cbox_command_block.setCursor(QCursor(Qt.PointingHandCursor))
        self.n_12 = QLabel(self.centralwidget)
        self.n_12.setObjectName(u"n_12")
        self.n_12.setGeometry(QRect(440, 220, 151, 20))
        self.motd = QLineEdit(self.centralwidget)
        self.motd.setObjectName(u"motd")
        self.motd.setGeometry(QRect(590, 220, 211, 25))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 110, 701, 20))
        self.pbtn_ok_adv_set = QPushButton(self.centralwidget)
        self.pbtn_ok_adv_set.setObjectName(u"pbtn_ok_adv_set")
        self.pbtn_ok_adv_set.setGeometry(QRect(420, 260, 93, 29))
        self.pbtn_ok_adv_set.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 260, 301, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(520, 260, 311, 20))
        self.pbtn_download = QPushButton(self.centralwidget)
        self.pbtn_download.setObjectName(u"pbtn_download")
        self.pbtn_download.setGeometry(QRect(480, 360, 93, 29))
        self.pbtn_output = QPushButton(self.centralwidget)
        self.pbtn_output.setObjectName(u"pbtn_output")
        self.pbtn_output.setGeometry(QRect(10, 30, 93, 91))
        self.pbtn_output.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_frp = QPushButton(self.centralwidget)
        self.pbtn_frp.setObjectName(u"pbtn_frp")
        self.pbtn_frp.setGeometry(QRect(10, 130, 93, 91))
        self.pbtn_frp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_about = QPushButton(self.centralwidget)
        self.pbtn_about.setObjectName(u"pbtn_about")
        self.pbtn_about.setGeometry(QRect(10, 230, 93, 91))
        self.pbtn_about.setCursor(QCursor(Qt.PointingHandCursor))
        self.min_ram = QSpinBox(self.centralwidget)
        self.min_ram.setObjectName(u"min_ram")
        self.min_ram.setGeometry(QRect(200, 140, 44, 25))
        self.min_ram.setMinimum(1)
        self.min_ram.setMaximum(256)
        self.max_ram = QSpinBox(self.centralwidget)
        self.max_ram.setObjectName(u"max_ram")
        self.max_ram.setGeometry(QRect(350, 140, 44, 25))
        self.max_ram.setMinimum(1)
        self.max_ram.setMaximum(256)
        self.pbtn_show_java_path = QPushButton(self.centralwidget)
        self.pbtn_show_java_path.setObjectName(u"pbtn_show_java_path")
        self.pbtn_show_java_path.setGeometry(QRect(300, 60, 151, 29))
        self.pbtn_show_java_path.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pbtn_start_server.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u670d\u52a1\u5668", None))
        self.n_8.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528Java:", None))
        self.cbox_using_java.setItemText(0, QCoreApplication.translate("MainWindow", u"Java17", None))
        self.cbox_using_java.setItemText(1, QCoreApplication.translate("MainWindow", u"Java16", None))
        self.cbox_using_java.setItemText(2, QCoreApplication.translate("MainWindow", u"Java8", None))

        self.n_2.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u4ee5\u4e0b\u7248\u672c\u7684Java:", None))
        self.cbox_want_to_download.setItemText(0, QCoreApplication.translate("MainWindow", u"Java17", None))
        self.cbox_want_to_download.setItemText(1, QCoreApplication.translate("MainWindow", u"Java16", None))
        self.cbox_want_to_download.setItemText(2, QCoreApplication.translate("MainWindow", u"Java8", None))
        self.cbox_want_to_download.setItemText(3, QCoreApplication.translate("MainWindow", u"Java7", None))

        self.pbtn_how_to_choice.setText(QCoreApplication.translate("MainWindow", u"\u5982\u4f55\u9009\u62e9", None))
        self.n_1.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u7aef\u8def\u5f84\uff1a", None))
        self.label_path.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.pbtn_download_server.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.pbtn_select_path.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.n_3.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5185\u5b58\uff1a", None))
        self.n_4.setText(QCoreApplication.translate("MainWindow", u"GB   \u6700\u5927\u5185\u5b58\uff1a", None))
        self.n_5.setText(QCoreApplication.translate("MainWindow", u"GB", None))
        self.pbtn_dis_log4j2.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8fc7\u542f\u52a8\u53c2\u6570\u7981\u7528Log4j2", None))
        self.n_7.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u7248\u9a8c\u8bc1\uff1a", None))
        self.cbox_mojang.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.cbox_mojang.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.n_6.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u73a9\u5bb6\u6570\u91cf\uff1a", None))
        self.max_player.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.n_9.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u7aef\u53e3\uff1a", None))
        self.server_port.setText(QCoreApplication.translate("MainWindow", u"19132", None))
        self.n_10.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f PVP:", None))
        self.cbox_pvp.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.cbox_pvp.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.n_11.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u65b9\u5757\uff1a", None))
        self.cbox_command_block.setItemText(0, QCoreApplication.translate("MainWindow", u"True", None))
        self.cbox_command_block.setItemText(1, QCoreApplication.translate("MainWindow", u"False", None))

        self.n_12.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668\u5217\u8868\u754c\u9762\u63d0\u793a\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u9ad8\u7ea7\u8bbe\u7f6e\uff1a\u5c06\u5728\u670d\u52a1\u5668\u91cd\u542f\u540e\u751f\u6548\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", None))
        self.pbtn_ok_adv_set.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014\u2014", None))
        self.pbtn_download.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.pbtn_output.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.pbtn_frp.setText(QCoreApplication.translate("MainWindow", u"\u6620\u5c04", None))
        self.pbtn_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.pbtn_show_java_path.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u663e\u793a\u5f53\u524d\u8def\u5f84", None))
    # retranslateUi


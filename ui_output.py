# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Output(object):
    def setupUi(self, Output):
        if not Output.objectName():
            Output.setObjectName(u"Output")
        Output.resize(640, 480)
        self.logs = QTextBrowser(Output)
        self.logs.setObjectName(u"logs")
        self.logs.setGeometry(QRect(10, 10, 621, 461))

        self.retranslateUi(Output)

        QMetaObject.connectSlotsByName(Output)
    # setupUi

    def retranslateUi(self, Output):
        Output.setWindowTitle(QCoreApplication.translate("Output", u"Dialog", None))
    # retranslateUi


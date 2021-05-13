# -*- coding: utf-8 -*-

from PySide2.QtCore import (
    QCoreApplication,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QUrl,
    Qt,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QLinearGradient,
    QPalette,
    QPainter,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *

from pyqtgraph import GraphicsLayoutWidget


class Ui_SingleWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(760, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../src/ui/icons/wood.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(62, 101, 190, 255), stop:1 rgba(81, 47, 154, 255));\n"
            "border-radius: 10px;"
        )
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 16pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_2.addWidget(self.title_label)

        self.message_label = QLabel(self.frame)
        self.message_label.setObjectName(u"message_label")
        sizePolicy1.setHeightForWidth(
            self.message_label.sizePolicy().hasHeightForWidth()
        )
        self.message_label.setSizePolicy(sizePolicy1)
        self.message_label.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 14pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_2.addWidget(self.message_label)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(
            u"background-color: rgb(255, 255, 255);\n"
            "border-radius: 17.0px;\n"
            "margin-top: 15px;\n"
            "margin-bottom: 15px;"
        )
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.plot_view = GraphicsLayoutWidget(self.frame_3)
        self.plot_view.setObjectName(u"plot_view")
        self.plot_view.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.plot_view)

        self.results_label = QLabel(self.frame_3)
        self.results_label.setObjectName(u"results_label")
        sizePolicy1.setHeightForWidth(
            self.results_label.sizePolicy().hasHeightForWidth()
        )
        self.results_label.setSizePolicy(sizePolicy1)
        self.results_label.setStyleSheet(
            u"color: rgb(0, 0, 0);\n"
            "font-size: 14pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_3.addWidget(self.results_label, 0, Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.close_button = QPushButton(self.frame_2)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color: rgb(255, 0, 127);\n"
            "height: 30px;\n"
            "padding-left: 10px;\n"
            "padding-bottom: 5px;\n"
            "border-radius: 17.0px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border: 2px solid rgb(255, 255, 255)\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "color: rgba(255, 255, 255, 0.5);\n"
            "background-color: rgba(255, 0, 127, 0.5);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.close_button)

        self.browse_button = QPushButton(self.frame_2)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color: rgb(0, 221, 51);\n"
            "height: 30px;\n"
            "padding-left: 10px;\n"
            "padding-bottom: 5px;\n"
            "border-radius: 17.0px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "border: 2px solid rgb(255, 255, 255)\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "color: rgba(255, 255, 255, 0.5);\n"
            "background-color: rgba(0, 221, 51, 0.5);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.browse_button)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout.addWidget(self.frame)

        self.footer = QLabel(self.centralwidget)
        self.footer.setObjectName(u"footer")
        sizePolicy.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy)
        self.footer.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);\n" "color: rgb(255, 255, 255);"
        )

        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"HARDIS | Single analysis", None)
        )
        self.title_label.setText(
            QCoreApplication.translate("MainWindow", u"Single analysis", None)
        )
        self.message_label.setText(
            QCoreApplication.translate(
                "MainWindow", u"Upload a file and select a cutting range", None
            )
        )
        self.results_label.setText("")
        self.close_button.setText(
            QCoreApplication.translate("MainWindow", u"Close", None)
        )
        self.browse_button.setText(
            QCoreApplication.translate("MainWindow", u"Browse", None)
        )
        self.footer.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"All Rights Reserved \u00a9 2021 Kompetenzzentrum Holz GmbH",
                None,
            )
        )

    # retranslateUi

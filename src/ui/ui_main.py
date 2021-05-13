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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 470)
        MainWindow.setMinimumSize(QSize(800, 470))
        MainWindow.setMaximumSize(QSize(800, 470))
        icon = QIcon()
        icon.addFile(u"../src/ui/icons/wood.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(18, 18, 18, 18)
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(
            self.message_label.sizePolicy().hasHeightForWidth()
        )
        self.message_label.setSizePolicy(sizePolicy)
        self.message_label.setStyleSheet(
            u"background-color: rgba(0, 0, 0, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 14pt;\n"
            'font-family: "Segoe UI Light";'
        )

        self.verticalLayout_2.addWidget(self.message_label)

        self.channel_field = QLineEdit(self.frame)
        self.channel_field.setObjectName(u"channel_field")
        self.channel_field.setStyleSheet(
            u"QLineEdit {\n"
            "height: 30px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "padding-left: 10px;\n"
            "padding-bottom: 5px;\n"
            "border-bottom: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 0px;\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 17.5px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "border-radius: 17.5px;\n"
            "}\n"
            ""
        )

        self.verticalLayout_2.addWidget(self.channel_field)

        self.cs_field = QLineEdit(self.frame)
        self.cs_field.setObjectName(u"cs_field")
        self.cs_field.setStyleSheet(
            u"QLineEdit {\n"
            "height: 30px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "padding-left: 10px;\n"
            "padding-bottom: 5px;\n"
            "border-bottom: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 0px;\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 17.5px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "border-radius: 17.5px;\n"
            "}\n"
            ""
        )

        self.verticalLayout_2.addWidget(self.cs_field)

        self.fs_field = QLineEdit(self.frame)
        self.fs_field.setObjectName(u"fs_field")
        self.fs_field.setStyleSheet(
            u"QLineEdit {\n"
            "height: 30px;\n"
            "font-size: 12pt;\n"
            'font-family: "Segoe UI Light";\n'
            "padding-left: 10px;\n"
            "padding-bottom: 5px;\n"
            "border-bottom: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 0px;\n"
            "color: rgb(255, 255, 255);\n"
            "}\n"
            "\n"
            "QLineEdit:hover {\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 17.5px;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "border: 2px solid rgb(0, 255, 213);\n"
            "border-radius: 17.5px;\n"
            "}\n"
            ""
        )

        self.verticalLayout_2.addWidget(self.fs_field)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
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

        self.single_button = QPushButton(self.frame_2)
        self.single_button.setObjectName(u"single_button")
        self.single_button.setStyleSheet(
            u"QPushButton {\n"
            "color: #ffffff;\n"
            "background-color: rgb(255, 170, 0);\n"
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
            "background-color: rgba(255, 170, 0, 0.5);\n"
            "}"
        )

        self.horizontalLayout.addWidget(self.single_button)

        self.batch_button = QPushButton(self.frame_2)
        self.batch_button.setObjectName(u"batch_button")
        self.batch_button.setStyleSheet(
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

        self.horizontalLayout.addWidget(self.batch_button)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalLayout.addWidget(self.frame)

        self.footer = QLabel(self.centralwidget)
        self.footer.setObjectName(u"footer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.footer.sizePolicy().hasHeightForWidth())
        self.footer.setSizePolicy(sizePolicy1)
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
            QCoreApplication.translate(
                "MainWindow", u"HARDIS | Cutting force analysis", None
            )
        )
        self.title_label.setText(
            QCoreApplication.translate(
                "MainWindow", u"Automatic cutting force analysis", None
            )
        )
        self.message_label.setText(
            QCoreApplication.translate("MainWindow", u"Fill in required fields", None)
        )
        self.channel_field.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"Channel corresponding to normal force", None
            )
        )
        self.cs_field.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"Cutting speed index used in file naming", None
            )
        )
        self.fs_field.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"Sampling rate in [Hz]", None)
        )
        self.close_button.setText(
            QCoreApplication.translate("MainWindow", u"Close", None)
        )
        self.single_button.setText(
            QCoreApplication.translate("MainWindow", u"Single analysis", None)
        )
        self.batch_button.setText(
            QCoreApplication.translate("MainWindow", u"Batch analysis", None)
        )
        self.footer.setText(
            QCoreApplication.translate(
                "MainWindow",
                u"All Rights Reserved \u00a9 2021 Kompetenzzentrum Holz GmbH",
                None,
            )
        )

    # retranslateUi

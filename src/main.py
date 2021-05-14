# -*- coding: utf-8 -*-

# Imports for ParametersWindow class
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import *
from ui.ui_main import Ui_MainWindow
from ui.ui_single import Ui_SingleWindow

# Imports for Single and Batch classes
from settings import *
import analyser
import database
import filter
import numpy as np
import os
import plotter
import pyqtgraph as pg
import sys


class Single(QMainWindow):
    def __init__(self, channel, cs_index, fs):
        # Constructor
        self.channel = channel
        self.cs_index = cs_index
        self.fs = fs

        # User interface
        QMainWindow.__init__(self)
        self.ui = Ui_SingleWindow()
        self.ui.setupUi(self)
        self.setup_initial_view()
        self.setup_graph()
        self.define_callbacks()
        self.oldPos = self.pos()
        self.show()

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setup_graph(self):
        self.ui.plot_view.setBackground("w")

    def get_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Import file path...", str(dir)
        )
        return file_path

    def get_data(self, path):
        data_raw = np.loadtxt(path, delimiter=",", usecols=self.channel)
        data_raw = data_raw * (-1)
        data_corrected = filter.Filter(self.fs).butter_lowpass_filter(
            data=data_raw, cut_off=CUTOFF_FREQUENCY, order=ORDER
        )

        return data_raw, data_corrected

    def browse(self):
        self.ui.plot_view.clear()
        file_path = self.get_file()
        data_raw, data_corrected = self.get_data(file_path)
        self.plot(data_raw, data_corrected)

    def define_callbacks(self):
        self.ui.close_button.clicked.connect(lambda: self.close())
        self.ui.browse_button.clicked.connect(lambda: self.browse())

    def plot(self, data_raw, data_corrected):
        x = np.linspace(0, len(data_raw) / self.fs, len(data_raw))

        lr_cutting = pg.LinearRegionItem(
            [int(x[-1] * 0.4), int(x[-1] * 0.6)],
            brush=(82, 255, 152, 100),
            pen=(17, 255, 0),
        )
        lr_cutting.setZValue(-10)

        # Adjust graphs
        p1 = self.ui.plot_view.addPlot(row=0, col=0)
        p1.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Force [N]</span>'.format(
                FONTSIZE
            ),
        )
        p1.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">Time [s]</span>'.format(
                FONTSIZE
            ),
        )

        p2 = self.ui.plot_view.addPlot(row=1, col=0)
        p2.setLabel(
            "left",
            '<span style="color: black; font-size: {}px">Force [N]</span>'.format(
                FONTSIZE
            ),
        )
        p2.setLabel(
            "bottom",
            '<span style="color: black; font-size: {}px">Time [s]</span>'.format(
                FONTSIZE
            ),
        )

        # Add items to the graphics view
        p1.addItem(lr_cutting)

        # Plot data
        p1.plot(x, data_raw, pen=(0, 0, 0, 100))
        p1.plot(x, data_corrected, pen=(0, 255, 0))
        p2.plot(x, data_raw, pen=(0, 0, 0, 100))
        p2.plot(x, data_corrected, pen=(0, 255, 0))

        # Define callbacks
        def update_plot():
            p2.setXRange(*lr_cutting.getRegion(), padding=0)

            # Since the default unit were seconds, multiply the variable by the applied sampling rate
            cutting_region = [
                int(lr_cutting.getRegion()[0] * self.fs),
                int(lr_cutting.getRegion()[1] * self.fs),
            ]

            # Update results
            mean_raw = np.mean(data_raw[cutting_region[0] : cutting_region[1]])
            std_raw = np.std(data_raw[cutting_region[0] : cutting_region[1]])
            mean_corrected = np.mean(
                data_corrected[cutting_region[0] : cutting_region[1]]
            )
            std_corrected = np.std(
                data_corrected[cutting_region[0] : cutting_region[1]]
            )
            self.ui.results_label.setText(
                "Raw: %.1f ± %.2f N | Filtered: %.1f ± %.2f N"
                % (mean_raw, std_raw, mean_corrected, std_corrected)
            )

        def update_cutting_region():
            lr_cutting.setRegion(p2.getViewBox().viewRange()[0])

        # Connect linear regions' callbacks with above functions
        lr_cutting.sigRegionChanged.connect(update_plot)
        p2.sigXRangeChanged.connect(update_cutting_region)
        update_plot()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


class Batch:
    def get_cutting_speed(self, filename, cs_index):
        return int(filename[cs_index : cs_index + 2])

    def get_text_files(self, files):
        files_ = []
        for file in files:
            if file.endswith(".txt"):
                files_.append(file)
            else:
                continue

        return files_

    def get_data(self, path):
        data_raw = np.loadtxt(path, delimiter=",", usecols=self.channel)
        data_raw = data_raw * (-1)
        data_corrected = self.filter_.butter_lowpass_filter(
            data=data_raw, cut_off=CUTOFF_FREQUENCY, order=ORDER
        )

        return data_raw, data_corrected

    def batch_analysis(self):
        self.filter_ = filter.Filter(self.fs)
        self.plotter_ = plotter.Plotter()

        # Get all the files within the directory
        files_ = os.listdir(self.folder_path)
        files = self.get_text_files(files_)

        for i, filename in enumerate(files):
            path = os.path.join(self.folder_path, filename)
            data_raw, data_corrected = self.get_data(path)
            cs = self.get_cutting_speed(filename, self.cs_index)

            # Find cutting's start and stop indices
            analyser_ = analyser.Analyser(fs=self.fs, cutting_speed=cs)
            start, stop = analyser_.process_scanner(data_corrected)

            # Plot (zoom into cutting range)
            self.plotter_.plot(
                filename=filename,
                data_original=data_raw,
                data_corrected=data_corrected,
                start=start,
                stop=stop,
            )

            # Save
            database.Database(DB_NAME).insert_into_table(
                filename,
                round(np.mean(data_corrected[start:stop]), DECIMALS_MEAN),
                round(np.median(data_corrected[start:stop]), DECIMALS_MEDIAN),
                round(np.std(data_corrected[start:stop]), DECIMALS_STD),
            )

        database.Database(DB_NAME).save_as_CSV()
        database.Database(DB_NAME).delete()


class MainWindow(QMainWindow, Batch):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_initial_view()
        self.setup_default_variables()
        self.define_callbacks()
        self.oldPos = self.pos()
        self.show()

    def setup_initial_view(self):
        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def setup_default_variables(self):
        self.channel = 0
        self.fs = 0
        self.cs_index = 0

    def show_single_window(self):
        # Show main window
        self.get_parameters()
        if self.channel and self.cs_index and self.fs:
            self.single = Single(self.channel, self.cs_index, self.fs)
            self.single.show()
        else:
            self.ui.message_label.setText("To start the analysis, complete the fields!")

    def define_callbacks(self):
        self.ui.close_button.clicked.connect(lambda: self.close())
        self.ui.single_button.clicked.connect(lambda: self.show_single_window())
        self.ui.batch_button.clicked.connect(lambda: self.start_batch_analysis())

    def get_parameters(self):
        try:
            self.channel = int(self.ui.channel_field.text())
        except:
            pass

        try:
            self.cs_index = int(self.ui.cs_field.text())
        except:
            pass

        try:
            self.fs = int(self.ui.fs_field.text())
        except:
            pass

    def get_directory(self):
        folder_path = str(
            QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory")
        )
        return folder_path

    def start_batch_analysis(self):
        self.get_parameters()
        if self.channel and self.cs_index and self.fs:
            self.folder_path = self.get_directory()
            if self.folder_path:
                self.ui.message_label.setText("Please wait...")
                self.batch_analysis()
                self.ui.message_label.setText("Success! You can view the results")
            else:
                self.ui.message_label.setText("No path was given! Try again")
        else:
            self.ui.message_label.setText("To start the analysis, complete the fields!")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    from PySide2.QtWidgets import *
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

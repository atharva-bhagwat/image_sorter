# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from secondpage import UiSecondWindow


class UiFirstWindow(object):
    def __init__(self):
        self.folder_to_process = None
        self.copy_operation = None
        self.subfolder_list = []

    def setupUi(self, firstpage):
        firstpage.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(firstpage)
        self.centralwidget.setObjectName("centralwidget")
        self.open_folder = QtWidgets.QPushButton(self.centralwidget)
        self.open_folder.setGeometry(QtCore.QRect(270, 50, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.open_folder.setFont(font)
        self.open_folder.setObjectName("open_folder")
        self.copy_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.copy_radio.setGeometry(QtCore.QRect(250, 200, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.copy_radio.setFont(font)
        self.copy_radio.setObjectName("copy_radio")
        self.cut_radio = QtWidgets.QRadioButton(self.centralwidget)
        self.cut_radio.setGeometry(QtCore.QRect(400, 200, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.cut_radio.setFont(font)
        self.cut_radio.setObjectName("cut_radio")
        self.choose_opr_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_opr_label.setGeometry(QtCore.QRect(110, 160, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.choose_opr_label.setFont(font)
        self.choose_opr_label.setObjectName("choose_opr_label")
        self.folder_list = QtWidgets.QListWidget(self.centralwidget)
        self.folder_list.setGeometry(QtCore.QRect(110, 340, 571, 151))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.folder_list.setFont(font)
        self.folder_list.setObjectName("folder_list")
        self.add_folder = QtWidgets.QPushButton(self.centralwidget)
        self.add_folder.setGeometry(QtCore.QRect(550, 290, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.add_folder.setFont(font)
        self.add_folder.setObjectName("add_folder")
        self.subfolder_name = QtWidgets.QTextEdit(self.centralwidget)
        self.subfolder_name.setGeometry(QtCore.QRect(110, 290, 431, 31))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.subfolder_name.setFont(font)
        self.subfolder_name.setObjectName("folder_name")
        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setGeometry(QtCore.QRect(310, 510, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Serif")
        self.proceed.setFont(font)
        self.proceed.setObjectName("proceed")
        firstpage.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(firstpage)
        self.statusbar.setObjectName("statusbar")
        firstpage.setStatusBar(self.statusbar)

        self.retranslateUi(firstpage)
        QtCore.QMetaObject.connectSlotsByName(firstpage)

        self.open_folder.clicked.connect(self.set_folder)
        self.copy_radio.toggled.connect(
            lambda: self.set_operation(self.copy_radio))
        self.cut_radio.toggled.connect(
            lambda: self.set_operation(self.cut_radio))
        self.add_folder.clicked.connect(
            lambda: self.add_folder_to_list(self.subfolder_name.toPlainText()))
        self.proceed.clicked.connect(lambda: self.next_window(firstpage))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Sorter"))
        self.open_folder.setText(_translate("MainWindow", "Open Folder"))
        self.open_folder.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.subfolder_name.setPlaceholderText(_translate("FirstWindow", "Enter Subfolder Name"))
        self.copy_radio.setText(_translate("MainWindow", "Cop&y"))
        self.cut_radio.setText(_translate("MainWindow", "C&ut"))
        self.choose_opr_label.setText(
            _translate("MainWindow", "Choose Operation:"))
        self.add_folder.setText(_translate("MainWindow", "Add Folder"))
        self.proceed.setText(_translate("MainWindow", "Proceed"))
        
    def reset(self):
        self.copy_radio.setAutoExclusive(False)
        self.cut_radio.setAutoExclusive(False)
        self.copy_radio.setChecked(False)
        self.cut_radio.setChecked(False)
        self.copy_radio.setAutoExclusive(True)
        self.cut_radio.setAutoExclusive(True)
        self.folder_list.clear()
        self.folder_to_process = None
        self.copy_operation = None
        self.subfolder_list = []        

    def display_error_message(self, title_message, info_message):
        error_message = QtWidgets.QMessageBox()
        error_message.setIcon(QtWidgets.QMessageBox.Critical)
        error_message.setText(title_message)
        error_message.setInformativeText(info_message)
        error_message.setWindowTitle("Error!")
        _ = error_message.exec_()

    def set_folder(self):
        self.folder_to_process = QtWidgets.QFileDialog.getExistingDirectory()

    def set_operation(self, button):
        if button.objectName() == 'copy_radio' and button.isChecked():
            self.copy_operation = True
        if button.objectName() == 'cut_radio' and button.isChecked():
            self.copy_operation = False

    def does_not_exist(self, folder_name):
        for itr in range(self.folder_list.count()):
            if folder_name == self.folder_list.item(itr).text():
                return False
        return True

    def add_folder_to_list(self, folder_name):
        if self.does_not_exist(folder_name):
            if not self.subfolder_name.document().isEmpty():
                folder_entry = QtWidgets.QListWidgetItem(folder_name)
                self.folder_list.addItem(folder_entry)
                self.subfolder_list.append(folder_name)
            else:
                self.display_error_message('Error:',
                                           "Folder name cannot be empty!")
        else:
            self.display_error_message('Error:',
                                       "Duplicate entry: Folder already in the list!")

        self.subfolder_name.setPlainText("")

    def next_window(self, firstpage):
        if self.folder_to_process is not None and self.copy_operation is not None and len(self.subfolder_list) >= 2:
            self.second_window = QtWidgets.QMainWindow()
            self.ui = UiSecondWindow(self.folder_to_process, self.copy_operation, self.subfolder_list)
            self.ui.setupUi(self.second_window, firstpage)
            self.second_window.showMaximized()
            firstpage.hide()
            self.reset()
        else:
            self.display_error_message('Missing Condition:',
                                       "Make sure:\n- Folder to process is selected.\n- Copy/Cut operation is selected.\n- There are atleast 2 subfolders added.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    first_window = QtWidgets.QMainWindow()
    first_ui = UiFirstWindow()
    first_ui.setupUi(first_window)
    first_window.showMaximized()
    sys.exit(app.exec_())

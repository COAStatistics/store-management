# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product_card_in_list.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 839)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_btn.setEnabled(True)
        self.search_btn.setGeometry(QtCore.QRect(480, 30, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.search_btn.setFont(font)
        self.search_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_btn.setObjectName("search_btn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 90, 1080, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 165, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.search_code = QtWidgets.QLineEdit(self.centralwidget)
        self.search_code.setEnabled(True)
        self.search_code.setGeometry(QtCore.QRect(200, 30, 270, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.search_code.setFont(font)
        self.search_code.setText("")
        self.search_code.setAlignment(QtCore.Qt.AlignCenter)
        self.search_code.setObjectName("search_code")
        self.card_table = QtWidgets.QTableWidget(self.centralwidget)
        self.card_table.setGeometry(QtCore.QRect(10, 110, 910, 671))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.card_table.setFont(font)
        self.card_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.card_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.card_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.card_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.card_table.setObjectName("card_table")
        self.card_table.setColumnCount(5)
        self.card_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.card_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.card_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.card_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.card_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.card_table.setHorizontalHeaderItem(4, item)
        self.card_table.horizontalHeader().setVisible(True)
        self.card_table.horizontalHeader().setCascadingSectionResizes(False)
        self.card_table.verticalHeader().setVisible(True)
        self.card_table.verticalHeader().setCascadingSectionResizes(False)
        self.print_btn = QtWidgets.QPushButton(self.centralwidget)
        self.print_btn.setGeometry(QtCore.QRect(810, 30, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.print_btn.setFont(font)
        self.print_btn.setObjectName("print_btn")
        self.clean_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clean_btn.setEnabled(True)
        self.clean_btn.setGeometry(QtCore.QRect(590, 30, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.clean_btn.setFont(font)
        self.clean_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clean_btn.setObjectName("clean_btn")
        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setEnabled(True)
        self.refresh_btn.setGeometry(QtCore.QRect(700, 30, 100, 40))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(20)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refresh_btn.setObjectName("refresh_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu_manager = QtWidgets.QMenu(self.menubar)
        self.menu_manager.setObjectName("menu_manager")
        self.menu_card = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.menu_card.setFont(font)
        self.menu_card.setObjectName("menu_card")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiontest = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.actiontest.setFont(font)
        self.actiontest.setObjectName("actiontest")
        self.product_all_card = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.product_all_card.setFont(font)
        self.product_all_card.setObjectName("product_all_card")
        self.product_manager = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.product_manager.setFont(font)
        self.product_manager.setObjectName("product_manager")
        self.product_card = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.product_card.setFont(font)
        self.product_card.setObjectName("product_card")
        self.product_card_in_list = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.product_card_in_list.setFont(font)
        self.product_card_in_list.setObjectName("product_card_in_list")
        self.menu_manager.addAction(self.product_manager)
        self.menu_card.addAction(self.product_card)
        self.menu_card.addAction(self.product_card_in_list)
        self.menu_card.addAction(self.product_all_card)
        self.menubar.addAction(self.menu_manager.menuAction())
        self.menubar.addAction(self.menu_card.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_btn.setText(_translate("MainWindow", "查詢"))
        self.label.setText(_translate("MainWindow", "商品條碼："))
        item = self.card_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "商品編碼"))
        item = self.card_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "商品名稱"))
        item = self.card_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "商品價格"))
        item = self.card_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "是否特價"))
        item = self.card_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "特價價格"))
        self.print_btn.setText(_translate("MainWindow", "列印"))
        self.clean_btn.setText(_translate("MainWindow", "清空"))
        self.refresh_btn.setText(_translate("MainWindow", "重整"))
        self.menu_manager.setTitle(_translate("MainWindow", "商品管理"))
        self.menu_card.setTitle(_translate("MainWindow", "價格牌管理"))
        self.actiontest.setText(_translate("MainWindow", "test"))
        self.product_all_card.setText(_translate("MainWindow", "3 列印所有價格牌"))
        self.product_manager.setText(_translate("MainWindow", "商品管理"))
        self.product_card.setText(_translate("MainWindow", "1 列印指定價格牌"))
        self.product_card_in_list.setText(_translate("MainWindow", "2 從清單中選取商品"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

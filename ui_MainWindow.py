# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1078, 609)
        MainWindow.setStyleSheet("* {\n"
"    color: #ffffff;\n"
"    background-color: #212121;\n"
"    border: none;\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QMenuBar {\n"
"    padding: 5px 2px;\n"
"    border-bottom: 3px solid #121212;\n"
"    spacing: 0px;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    border-color: none;\n"
"    padding: 2px 5px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    border-color: none;\n"
"    background: #121212;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    border-color: none;\n"
"    background: #121212;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background: #121212;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    border-top: 3px solid #121212;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    margin: 0;\n"
"}\n"
"\n"
"QMainWindow::separator {\n"
"    /*\n"
"    border: none;\n"
"    border-left: 1px solid #121212;\n"
"    */\n"
"    background-color: #aa121212;\n"
"    width:4px;\n"
"}\n"
"\n"
"QListWidget::item:hover\n"
"{\n"
"    background: #22000000;\n"
"}\n"
"\n"
"QListWidget::item:selected\n"
"{\n"
"    background: #00000000;\n"
"}\n"
"\n"
"QListWidget::item:selected:active { background: transparent;}\n"
"QListWidget::item:selected:!active { background: transparent;}\n"
"QListWidget::item:alternate { background: transparent;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setMouseTracking(True)
        self.listWidget_2.setAutoFillBackground(True)
        self.listWidget_2.setStyleSheet("\n"
"QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"     background: #00000000;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"     border: none;\n"
"     background: none;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"     border: none;\n"
"     border-radius: 2px;\n"
"     background: #aaffffff;\n"
"     width: 10px;\n"
"}\n"
"QScrollBar {\n"
"     width: 8px;\n"
"     margin-top: 4px;\n"
"     border-radius: 90;\n"
"     margin-right: 4px;\n"
"     margin-bottom: 4px;\n"
"}")
        self.listWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.listWidget_2.setProperty("showDropIndicator", False)
        self.listWidget_2.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.listWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.listWidget_2.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_2.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("border-top:3px solid #121212; border-bottom:3px solid #121212; padding: 3px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1078, 33))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.dockWidgetContents)
        self.line.setStyleSheet("border-radius: 90;\n"
"border-top: 2px solid #BB121212;\n"
"margin: 0 5px;\n"
"")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.listView_2 = QtWidgets.QListWidget(self.dockWidgetContents)
        self.listView_2.setStyleSheet("QListWidget::item{\n"
"    color: #ffffff;\n"
"    margin-right: 8px;\n"
"    margin-top: 0px;\n"
"    margin-bottom: 0px;\n"
"    border: none;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    color: #ffffff;\n"
"    background: #22000000;\n"
"    padding-left:8px;\n"
"    border: none;\n"
"}\n"
"\n"
"QListWidget::item:selected,\n"
"QListWidget::item:selected:active,\n"
"QListWidget::item:selected:!active {\n"
"    color: #ffffff;\n"
"    background: #66000000;\n"
"    padding-left:8px;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"     background: #00000000;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"     border: none;\n"
"     background: none;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"     border: none;\n"
"     border-radius: 2px;\n"
"     background: #aaffffff;\n"
"     width: 10px;\n"
"}\n"
"QScrollBar {\n"
"     width: 8px;\n"
"     margin-top: 4px;\n"
"     border-radius: 90;\n"
"     margin-right: 4px;\n"
"     margin-bottom: 4px;\n"
"}")
        self.listView_2.setObjectName("listView_2")
        self.verticalLayout.addWidget(self.listView_2)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "4QT"))
        self.pushButton.setText(_translate("MainWindow", "New post"))
        self.label.setText(_translate("MainWindow", "Page"))
        self.label_2.setText(_translate("MainWindow", "of 1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "  Boards"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+R"))

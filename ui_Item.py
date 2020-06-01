# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/Item.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets   
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import *
import urllib
from functools import partial
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, Qt, QThread, QTimer

class Downloader(QObject):
    resultsChanged = pyqtSignal(bytes)

    @pyqtSlot(str)
    def download(self, url):
        try:
            img = urllib.request.urlopen(url).read()
        except:
            img = b""
        self.resultsChanged.emit(img)

class Ui_Item(QtWidgets.QWidget):            
    def __init__(self, parent=None):
        super(Ui_Item, self).__init__(parent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(16777215, 260))
        self.setStyleSheet("QWidget {\n"
"    background: transparent;\n"
"}\n"
"\n"
"* {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"#widget,#widget_2 {\n"
"    border: 1px solid #121212;\n"
"    border-radius: 10px;\n"
"    background-color: #12000000;\n"
"}\n"
"\n"
"#title,#title2 {\n"
"    color: #E65100;\n"
"    font-weight: bold;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 240))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label.hide()
        self.label.setCursor(QCursor(Qt.PointingHandCursor))

        self.label.mousePressEvent = partial(self._downloadImage)

        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(8, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.title2 = QtWidgets.QLabel(self.widget_2)
        self.title2.setObjectName("title2")
        self.horizontalLayout_5.addWidget(self.title2)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet("color: #0277BD;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setStyleSheet("color: #757575;")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        
        self.pin = QtWidgets.QLabel(self.widget_2)
        self.pin.setMaximumSize(QtCore.QSize(12, 12))
        self.pin.setText("")
        self.pin.setTextFormat(QtCore.Qt.RichText)
        self.pin.setPixmap(QtGui.QPixmap("images/pin.png"))
        self.pin.setScaledContents(True)
        self.pin.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout_5.addWidget(self.pin)

        self.pin.hide()
        
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.scrollArea = QtWidgets.QScrollArea(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("""
        QScrollArea {
            background-color: #21000000; 
                border-radius: 10;
                }

        QScrollBar::add-line:vertical {
                      border: none;
                            background: #00000000;
                            }

        QScrollBar::sub-line:vertical {
                      border: none;
                            background: none;
                            }

        QScrollBar::handle:vertical {
                      border: none;
                            border-radius: 2px;
                                  background: #aaffffff;
                                        width: 10px;
                                        }

        QScrollBar {
                      width: 8px;
                            margin-top: 4px;
                                  border-radius: 90;
                                        margin-right: 4px;
                                              margin-bottom: 4px;
                                              }
""")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 627, 427))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: none; color: #ddd;")
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_3.setObjectName("label_3")
        self.label_3.setWordWrap(True)
        self.verticalLayout_4.addWidget(self.label_3)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setStyleSheet("background: #121212;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setStyleSheet("background-color: transparent;")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.verticalLayout_4.addWidget(self.label_4)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)
        self.label_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_5.setStyleSheet(u"color: lightblue;")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.label_5.hide()
        
        self.thread = QThread(self)
        self.thread.start()

        self.downloader = Downloader()
        self.downloader.moveToThread(self.thread)
        self.downloader.resultsChanged.connect(self.on_resultsChanged)

        self.retranslateUi(self)

    def retranslateUi(self, Item):
        _translate = QtCore.QCoreApplication.translate
        self.title2.setText(_translate("Item", "TextLabel"))
        self.label_2.setText(_translate("Item", "TextLabel"))
        self.label_6.setText(_translate("Item", "TextLabel"))
        self.label_3.setText(_translate("Item", "TextLabel"))
        self.label_4.setText(_translate("Item", "Sample Text\n"*20))
        self.label_5.setText(_translate("Item", u"View Thread >", None))

    def setPin(self):
        self.pin.show()

    def _downloadImage(self, sauce):
        import webbrowser
        webbrowser.open(self.postData.file.file_url)

    def setPostData(self, data):
        self.postData = data
    def setTitle(self, title: str):
        if title:
            self.label_3.setText(title)
        else:
            self.label_3.hide()
            self.line.hide()
    def setAuthor(self, author: str):
        self.title2.setText(author)
    def setReplyIds(self, ids):
        # TODO: Add href
        self.label_2.setText(' '.join(['>>' + str(i) for i in ids]))
    def setId(self, _id):
        self.label_6.setText(str(_id))
    def setContent(self, content):
        self.label_4.setText(content)
    def setThumbnail(self, url):
        wrapper = partial(self.downloader.download, url)
        QTimer.singleShot(0, wrapper)
    def setPost(self):
        self.horizontalLayout.setContentsMargins(64, -1, -1, -1)
    def setThread(self):
        self.label_5.show()

    @pyqtSlot(bytes)
    def on_resultsChanged(self, img):
        pixmap = QPixmap()
        pixmap.loadFromData(img)
        self.label.setToolTip(self.postData.file.filename)
        self.label.setPixmap(pixmap)
        self.label.show()


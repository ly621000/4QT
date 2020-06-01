#!/usr/bin/env python3

import sys
import threading

import basc_py4chan

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import *

from ui_MainWindow import *
from ui_Item import *

boards = basc_py4chan.get_all_boards()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        x = threading.Thread(target=self._loadBoards)
        x.start()

        self.listView_2.itemClicked.connect(self.listwidgetclicked)
        self.spinBox.valueChanged.connect(self._updateView)

        self.listView_2.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel);

        self.rows = []

        #item = QListWidgetItem(self.listWidget_2)
        #self.listWidget_2.addItem(item)

        #row = Ui_Item()
        #item.setSizeHint(row.sizeHint())
        
        #self.listWidget_2.setItemWidget(item, row)

    def _updateView(self):
        self.spinBox.setMaximum(self.board.page_count)
        self.label_2.setText(str(self.board.page_count))

        self.listWidget_2.clear()

        for i in self.rows:
            i.thread.quit()
        self.rows = []

        page = self.spinBox.value()

        for i in self.board.get_threads(page):
            item = QListWidgetItem(self.listWidget_2)
            self.listWidget_2.addItem(item)

            row = Ui_Item()
            item.setSizeHint(row.sizeHint())
            row.setPostData(i.topic)
            row.setTitle(i.topic.subject)
            row.setThumbnail(list(i.thumbs())[0])
            row.setReplyIds([])
            row.setAuthor(i.topic.name + (" ({})" if i.topic.poster_id else '').format(i.topic.poster_id))
            row.setContent(i.topic.text_comment)
            row.setId(i.topic.post_id)
            if i.sticky: row.setPin()

            self.rows.append(row)

            self.listWidget_2.setItemWidget(item, row)
        self.listView_2.verticalScrollBar().setSingleStep(3)

    def _loadBoards(self):
        lst = self.listView_2

        data = ['/{}/ - {} - {}'.format(i.name, i.title, 'SFW' if i.is_worksafe else 'NSFW' ) for i in boards]

        lst.clear()
        lst.addItems(data)

    def listwidgetclicked(self, item):
        self.spinBox.setValue(1)
        if item.text().startswith('/'):
            board_name=item.text().split(' - ')[0].replace('/', '')
            self.board = basc_py4chan.get_boards([board_name])[0]

            self._updateView()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


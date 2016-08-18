# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDesktopWidget, QFileDialog,
                             QGroupBox, QHBoxLayout, QLabel, QMainWindow, QMenuBar, QStatusBar,
                             QToolBar)

{% if cookiecutter.insert_menubar == 'yes' %}
class MenuBar(QMenuBar):

    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent)

        self.open_items = OpenDialogs()
        self.dialogs = Dialogs()

        self.file_menu()
        self.help_menu()

    def file_menu(self):
        self.file_sub_menu = self.addMenu('File')

        self.open_action = QAction('Open File', self)
        self.open_action.setStatusTip('Open a file into {{ cookiecutter.application_title }}.')
        self.open_action.setShortcut('CTRL+O')
        self.open_action.triggered.connect(self.open_items.open_file)

        self.file_sub_menu.addAction(self.open_action)

    def help_menu(self):
        self.help_sub_menu = self.addMenu('Help')

        self.about_action = QAction('About', self)
        self.about_action.setStatusTip('About {{ cookiecutter.application_title }}')
        self.about_action.setShortcut('CTRL+H')
        self.about_action.triggered.connect(self.dialogs.about_dialog)

        self.help_sub_menu.addAction(self.about_action)


class OpenDialogs(QFileDialog):

    def __init__(self, parent=None):
        super(OpenDialogs, self).__init__(parent)

    def open_file(self):

        filename, accepted = QFileDialog.getOpenFileName(self, 'Open File')

        if accepted:
            with open(filename) as file:
                file.read()


class Dialogs(QDialog):

    def __init__(self, parent=None):
        super(Dialogs, self).__init__(parent)

    def about_dialog(self):

        group_box = QGroupBox()
        layout = QHBoxLayout()

        author = QLabel('Created by {{ cookiecutter.full_name }}', self)

        layout.addWidget(author)
        group_box.setLayout(layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(group_box)
        main_layout.addStretch(1)
        self.setLayout(main_layout)

        self.setWindowTitle('About {{ cookiecutter.application_title }}')
        self.resize(400, 400)
        self.exec_()
{% endif %}


{% if cookiecutter.insert_statusbar == 'yes' %}
class StatusBar(QToolBar):

    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)

        self.status_bar = QStatusBar()

        self.addWidget(self.status_bar)

{% endif %}

class {{ cookiecutter.application_title }}(QMainWindow):

    def __init__(self, parent=None):
        super({{ cookiecutter.application_title }}, self).__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle('{{ cookiecutter.application_title }}')

        {% if cookiecutter.insert_menubar == 'yes' %}
        self.setMenuBar(MenuBar())
        {% endif %}

        {% if cookiecutter.insert_statusbar == 'yes' %}
        self.addToolBar(StatusBar())
        {% endif %}


def main():
    application = QApplication(sys.argv)
    window = {{ cookiecutter.application_title }}()
    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) / 2
    height = (desktop.height() - window.height()) / 2
    window.show()
    window.move(width, height)
    sys.exit(application.exec_())

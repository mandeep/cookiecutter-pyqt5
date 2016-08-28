# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDesktopWidget, QFileDialog,
                             QGroupBox, QHBoxLayout, QLabel, QMainWindow, QMenuBar, QStatusBar,
                             QToolBar)

{% if cookiecutter.insert_statusbar == 'yes' %}
class StatusBar(QToolBar):
    """Creates a status bar to be added to the main window. Inherits QToolBar so that the user
    may move the status bar wherever they please."""

    def __init__(self, parent=None):
        super(StatusBar, self).__init__(parent)

        self.status_bar = QStatusBar()

        self.addWidget(self.status_bar)
{% endif %}
class {{ cookiecutter.application_title }}(QMainWindow):
    """Creates the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initializes the window size and title and instantiates the menu bar and status bar
        if selected by the user."""

        super({{ cookiecutter.application_title }}, self).__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle('{{ cookiecutter.application_title }}')

        self.menu_bar = self.menuBar()

        {% if cookiecutter.insert_statusbar == 'yes' %}
        self.status_bar = self.statusBar()
        {% endif %}

        self.file_menu()
        self.help_menu()

    def file_menu(self):
        """Creates a file menu for the menu bar with an Open File item that opens a
        file dialog."""

        self.file_sub_menu = self.menu_bar.addMenu('File')

        self.open_action = QAction('Open File', self)
        self.open_action.setStatusTip('Open a file into {{ cookiecutter.application_title }}.')
        self.open_action.setShortcut('CTRL+O')
        self.open_action.triggered.connect(self.open_items.open_file)

        self.file_sub_menu.addAction(self.open_action)

    def help_menu(self):
        """Creates a help menu for the menu bar with a dialog box used to show users helpful
        information about the application."""
        self.help_sub_menu = self.menu_bar.addMenu('Help')

    def open_file(self):
        """Opens a QFileDialog to allow the user to open a file into the application. The template
        creates the dialog and simply reads it with the context manager."""

        filename, accepted = QFileDialog.getOpenFileName(self, 'Open File')

        if accepted:
            with open(filename) as file:
                file.read()

def main():
    application = QApplication(sys.argv)
    window = {{ cookiecutter.application_title }}()
    desktop = QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) / 2
    height = (desktop.height() - window.height()) / 2
    window.show()
    window.move(width, height)
    sys.exit(application.exec_())

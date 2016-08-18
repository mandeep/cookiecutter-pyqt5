# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDesktopWidget, QFileDialog,
                             QGroupBox, QHBoxLayout, QLabel, QMainWindow, QMenuBar, QStatusBar,
                             QToolBar)

{% if cookiecutter.insert_menubar == 'yes' %}
class MenuBar(QMenuBar):
    """MenuBar class creates a menu bar with necessary items to be used inside of a QMainWindow."""

    def __init__(self, parent=None):
        """Instantiates the file dialogs and dialog boxes that are used to open files and show
        messages. Also creates the file menu and help menu."""
        
        super(MenuBar, self).__init__(parent)

        self.open_items = OpenDialogs()
        self.dialogs = Dialogs()

        self.file_menu()
        self.help_menu()

    def file_menu(self):
        """Creates a file menu for the menu bar with an Open File item that opens a
        file dialog."""

        self.file_sub_menu = self.addMenu('File')

        self.open_action = QAction('Open File', self)
        self.open_action.setStatusTip('Open a file into {{ cookiecutter.application_title }}.')
        self.open_action.setShortcut('CTRL+O')
        self.open_action.triggered.connect(self.open_items.open_file)

        self.file_sub_menu.addAction(self.open_action)

    def help_menu(self):
        """Creates a help menu for the menu bar with a dialog box used to show users helpful
        information about the application."""
        self.help_sub_menu = self.addMenu('Help')

        self.about_action = QAction('About', self)
        self.about_action.setStatusTip('About {{ cookiecutter.application_title }}')
        self.about_action.setShortcut('CTRL+H')
        self.about_action.triggered.connect(self.dialogs.about_dialog)

        self.help_sub_menu.addAction(self.about_action)


class OpenDialogs(QFileDialog):
    """The OpenDialogs class stores all activities related to opening files with file dialogs."""

    def __init__(self, parent=None):
        super(OpenDialogs, self).__init__(parent)

    def open_file(self):
        """Opens a QFileDialog to allow the user to open a file into the application. The template
        creates the dialog and simply reads it with the context manager."""

        filename, accepted = QFileDialog.getOpenFileName(self, 'Open File')

        if accepted:
            with open(filename) as file:
                file.read()


class Dialogs(QDialog):
    """Because of the wide array of uses of QDialogs, Dialogs is created to store any kind of
    QDialog item that the user can create."""

    def __init__(self, parent=None):
        super(Dialogs, self).__init__(parent)

    def about_dialog(self):
        """Creates a QDialog that shows the user information regarding the application. Uses layouts
        to arrange the widgets on the dialog."""

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

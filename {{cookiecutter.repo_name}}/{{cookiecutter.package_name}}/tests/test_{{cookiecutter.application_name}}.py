#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.package_name }}
----------------------------------

Tests for `{{ cookiecutter.package_name }}` module.
"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDesktopWidget, QFileDialog,
                             QGroupBox, QHBoxLayout, QLabel, QMainWindow, QMenuBar, QStatusBar,
                             QToolBar)
from {{ cookiecutter.package_name }} import {{ cookiecutter.application_name }}

app = QApplication(sys.argv)


class Test{{ cookiecutter.application_title }}:

    def setup(self):
        self.window = {{cookiecutter.application_name }}.{{cookiecutter.application_title }}()
        {% if cookiecutter.insert_menubar == 'yes' %}
        self.menu_bar = {{cookiecutter.application_name}}.MenuBar()
        {% endif %}
        self.window.show()

    def test_window_title(self):
        assert self.window.windowTitle() == '{{ cookiecutter.application_title }}'

    def test_window_geometry(self):
        assert self.window.width() == 1024
        assert self.window.height() == 768

    {% if cookiecutter.insert_menubar == 'yes' %}
    def test_open_file(self, qtbot, mock):
        qtbot.mouseClick(self.menu_bar.file_sub_menu, Qt.LeftButton)
        qtbot.keyClick(self.menu_bar.file_sub_menu, Qt.Key_Down)
        mock.patch.object(QFileDialog, 'getOpenFileName', return_value=('README.rst', '*.rst'))
        qtbot.keyClick(self.menu_bar.file_sub_menu, Qt.Key_Enter)

    def test_about_dialog(self, qtbot, mock):
        qtbot.mouseClick(self.menu_bar.help_sub_menu, Qt.LeftButton)
        qtbot.keyClick(self.menu_bar.help_sub_menu, Qt.Key_Down)
        mock.patch.object(QDialog, 'exec_', return_value='finished')
        qtbot.keyClick(self.menu_bar.help_sub_menu, Qt.Key_Enter)
    {% endif %}


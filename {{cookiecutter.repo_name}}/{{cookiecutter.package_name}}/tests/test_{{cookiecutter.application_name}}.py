#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.package_name }}
----------------------------------

Tests for `{{ cookiecutter.package_name }}` module.
"""
import pytest
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDesktopWidget, QFileDialog,
                             QGroupBox, QHBoxLayout, QLabel, QMainWindow, QMenuBar, QStatusBar,
                             QToolBar)
from {{ cookiecutter.package_name }} import {{ cookiecutter.application_name }}


@pytest.fixture
def window(qtbot):
    new_window = {{cookiecutter.application_name }}.{{cookiecutter.application_title }}()
    qtbot.add_widget(new_window)
    new_window.show()
    return new_window

{% if cookiecutter.insert_menubar == 'yes' %}
@pytest.fixture
def menu(qtbot):
    new_menu_bar = {{cookiecutter.application_name}}.MenuBar()
    qtbot.add_widget(new_menu_bar)
    return new_menu_bar
{% endif %}

def test_window_title(window):
    assert window.windowTitle() == '{{ cookiecutter.application_title }}'


def test_window_geometry(window):
    assert window.width() == 1024
    assert window.height() == 768

{% if cookiecutter.insert_menubar == 'yes' %}
def test_open_file(window, menu, qtbot, mock):
    qtbot.mouseClick(menu.file_sub_menu, Qt.LeftButton)
    qtbot.keyClick(menu.file_sub_menu, Qt.Key_Down)
    mock.patch.object(QFileDialog, 'getOpenFileName', return_value=('README.rst', '*.rst'))
    qtbot.keyClick(menu.file_sub_menu, Qt.Key_Enter)


def test_about_dialog(window, menu, qtbot, mock):
    qtbot.mouseClick(menu.help_sub_menu, Qt.LeftButton)
    qtbot.keyClick(menu.help_sub_menu, Qt.Key_Down)
    mock.patch.object(QDialog, 'exec_', return_value='finished')
    qtbot.keyClick(menu.help_sub_menu, Qt.Key_Enter)
{% endif %}
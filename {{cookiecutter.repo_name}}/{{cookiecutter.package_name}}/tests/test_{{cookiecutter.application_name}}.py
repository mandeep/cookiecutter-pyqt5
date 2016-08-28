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
    """Window is used as a pytest fixture that allows passing it to test functions. Qtbot
    uses qApp to open a new main window."""

    new_window = {{cookiecutter.application_name }}.{{cookiecutter.application_title }}()
    qtbot.add_widget(new_window)
    new_window.show()
    return new_window


def test_window_title(window):
    assert window.windowTitle() == '{{ cookiecutter.application_title }}'


def test_window_geometry(window):
    assert window.width() == 1024
    assert window.height() == 768


def test_open_file(window, menu, qtbot, mock):
    """Qtbot clicks on the file sub menu and then navigates to the Open File item. Mock creates
    an object to be passed to the QFileDialog."""

    qtbot.mouseClick(menu.file_sub_menu, Qt.LeftButton)
    qtbot.keyClick(menu.file_sub_menu, Qt.Key_Down)
    mock.patch.object(QFileDialog, 'getOpenFileName', return_value=('', ''))
    qtbot.keyClick(menu.file_sub_menu, Qt.Key_Enter)

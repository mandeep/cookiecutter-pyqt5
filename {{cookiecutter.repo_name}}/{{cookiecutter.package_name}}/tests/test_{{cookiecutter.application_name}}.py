#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.package_name }}
----------------------------------

Tests for `{{ cookiecutter.package_name }}` module.
"""
import sys
from PyQt5.QtWidgets import (QAction, QApplication, QDialog, QDesktopWidget, QFileDialog,
                             QGroupBox, QHBoxLayout, QLabel, QMainWindow, QMenuBar, QStatusBar,
                             QToolBar)
from {{ cookiecutter.package_name }} import {{ cookiecutter.application_name }}


class Test{{ cookiecutter.application_title }}:

    def setup(self):
        self.window = {{cookiecutter.application_name }}.{{cookiecutter.application_title }}()
        self.window.show()

    def window_title():
        assert self.windowTitle() == '{{ cookiecutter.application_title }}'
"""This module defines the main application window"""

from PyQt5.QtWidgets import QMainWindow, QStatusBar, QVBoxLayout, QWidget

from ..app_info import __appdescription__, __appname__
from .labeling.label_wrapper import LabelingWrapper


class MainWindow(QMainWindow):
    """Main application window"""

    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setContentsMargins(0, 0, 0, 0)
        self.setWindowTitle(__appname__)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        self.labeling_widget = LabelingWrapper(self)
        main_layout.addWidget(self.labeling_widget)
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        status_bar = QStatusBar()
        status_bar.showMessage(f"{__appname__} - {__appdescription__}")
        self.setStatusBar(status_bar)

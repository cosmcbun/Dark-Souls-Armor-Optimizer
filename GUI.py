import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QToolBar
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QAction

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Armor Optimizer")
        #self.setWindowIcon(QtGui.QIcon("mask.png"))

        saveAction = QAction("&Save", self)
        saveAction.setShortcut("Cmd+S")
        saveAction.setStatusTip("Saves the current character")
        saveAction.triggered.connect(sys.exit)

        self.statusBar()

        mainMenu = QToolBar("My main toolbar")
        self.addToolBar(mainMenu)
        mainMenu.addAction(saveAction)

reverse()
        #fileMenu = mainMenu.addMenu("&File")
        #fileMenu.addAction(saveAction)

        """layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)"""

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(btn.sizeHint())
        btn.move(200, 100)
        self.show()

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec())

run()

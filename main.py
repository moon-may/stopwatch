import sys
from PySide6.QtWidgets import *

class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 300, 100)
        self.setWindowTitle('Таймер')

        central = QWidget()
        self.setCentralWidget(central)

        view = QVBoxLayout(central)

        timer_label = QLabel('00:00:00')
        view.addWidget(timer_label)

        btn_layout = QHBoxLayout()

        self.start_btn = QPushButton()
        self.pause_btn = QPushButton()
        self.stop_btn = QPushButton()

        style = self.style()
        self.start_btn.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.pause_btn.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        self.stop_btn.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_MediaStop))
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.pause_btn)
        btn_layout.addWidget(self.stop_btn)

        view.addLayout(btn_layout)




app = QApplication(sys.argv)
main_window = TimerWindow()
main_window.show()
app.exec()
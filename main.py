import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QTimer

class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 300, 100)
        self.setWindowTitle('Таймер')

        central = QWidget()
        self.setCentralWidget(central)

        view = QVBoxLayout(central)

        self.timer_label = QLabel('00:00:00')
        view.addWidget(self.timer_label)

        btn_layout = QHBoxLayout()

        self.start_btn = QPushButton()
        self.pause_btn = QPushButton()
        self.stop_btn = QPushButton()

        style = self.style()
        self.start_btn.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_MediaPlay))
        self.pause_btn.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_MediaPause))
        self.stop_btn.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_MediaStop))

        self.start_btn.clicked.connect(self.start_clicked)
        self.pause_btn.clicked.connect(self.pause_clicked)
        self.stop_btn.clicked.connect(self.stop_clicked)

        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.pause_btn)
        btn_layout.addWidget(self.stop_btn)

        view.addLayout(btn_layout)

        self.seconds = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.on_tick)


    def time_format(self, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


    def on_tick(self):
        self.seconds += 1
        self.timer_label.setText(self.time_format(self.seconds))


    def start_clicked(self):
        self.timer.start(1000)


    def pause_clicked(self):
        self.timer.stop()


    def stop_clicked(self):
        self.timer.stop()
        self.seconds = 0
        self.timer_label.setText(self.time_format(0))


app = QApplication(sys.argv)
main_window = TimerWindow()
main_window.show()
app.exec()
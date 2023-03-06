import sys
import os
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class Slideshow(QMainWindow):
    def __init__(self, images):
        super().__init__()
        self.images = images
        self.current_image = 0
        self.label = QLabel()
        self.setCentralWidget(self.label)
        self.showFullScreen()
        self.timer = QTimer()
        self.timer.timeout.connect(self.next_image)
        self.timer.start(3000)  # Change this value to adjust the slideshow speed
    
    def next_image(self):
        pixmap = QPixmap(self.images[self.current_image])
        self.label.setPixmap(pixmap)
        self.current_image = (self.current_image + 1) % len(self.images)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    files = os.listdir('Images')
    files_path = ['Images/' + file for file in files]
    slideshow = Slideshow(files_path)
    slideshow.show()
    sys.exit(app.exec())

from PyQt5.QtCore import QSize
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

fileName = "/home/drapaiton/Documents/GitHub/videoplayer-master/risa.mp4"


class InstantlyPlay(QWidget):
    def __init__(self, parent=None):
        super(InstantlyPlay, self).__init__(parent)
        self.resize(1280, 400)
        self.baseSize = QSize(1280, 400)
        self.mediaPlayer = QMediaPlayer(flags=QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.play()


if __name__ == "__main__":
    app = QApplication([])
    player = InstantlyPlay()

    player.show()
    app.exec_()

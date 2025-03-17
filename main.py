import sys
import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp
import zipfile
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QListWidget, QFileDialog, QRadioButton, QGroupBox

# Client Key
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="6db2ef04b8fd4c37890143f9d0adc34b",
                                               client_secret="c006c498f4f54e7ab80d073e3ab53c36",
                                               redirect_uri="http://localhost:49154",
                                               scope="user-library-read"))

class SpotifyToYoutubeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spotify to YouTube MP3")
        self.setGeometry(100, 100, 400, 500)

        layout = QVBoxLayout()

        self.typeGroup = QGroupBox("Pick an option: ")
        self.radioButton1 = QRadioButton("Single Track")
        self.radioButton1.setChecked(True)
        layout.addWidget(self.radioButton1)
        self.radioButton2 = QRadioButton("Playlist")
        layout.addWidget(self.radioButton2)
        self.typeGroup.setLayout(layout)


        self.label = QLabel("Enter Spotify Playlist URL:")
        layout.addWidget(self.label)

        self.urlInput = QLineEdit()
        layout.addWidget(self.urlInput)

        self.fetchBtn = QPushButton("Fetch Song(s)")
        self.fetchBtn.clicked.connect(self.fetch_songs)
        layout.addWidget(self.fetchBtn)

        self.songList = QListWidget()
        layout.addWidget(self.songList)

        self.individualBtn = QPushButton("Download song")
        self.individualBtn.clicked.connect(self.download_songs)
        layout.addWidget(self.individualBtn)

        self.zipBtn = QPushButton("Download as ZIP")
        self.zipBtn.clicked.connect(self.download_songs)
        layout.addWidget(self.zipBtn)

        self.statusLabel = QLabel("")
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)

    def fetch_songs(self):
        return 0
    
    def download_songs(self):
        return 0

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpotifyToYoutubeApp()
    window.show()
    sys.exit(app.exec_())
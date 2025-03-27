#import sqlite3
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QMovie, QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ferg Timer")
        self.setGeometry(500,500,500,500)

        #Affichage du GIF
        self.gif_label = QLabel(self)
        movie = QMovie("assets/ferg.gif")
        self.gif_label.setMovie(movie)
        movie.start()

        # Centrer le GIF avec un layout horizontal
        gif_layout = QHBoxLayout()
        gif_layout.addStretch()  # Espace avant
        gif_layout.addWidget(self.gif_label)  # Ajout du GIF
        gif_layout.addStretch()  # Espace après

        # === Bouton avec image ===
        self.button = QPushButton(self)
        self.button.setFixedSize(100, 100)  # Taille du bouton
        self.button.setStyleSheet("border: none;")  # Supprime la bordure
        self.set_button_image("assets/start_button_idle.png")  # Mettre l'image de base

        # Images des états
        self.idle_image = "assets/start_button_pressed.png"
        self.pressed_image = "assets/start_button_idle.png"

        self.set_button_image(self.idle_image)  # Image initiale

        # Connexion des événements
        self.button.pressed.connect(self.on_button_press)
        self.button.released.connect(self.on_button_release)

        # Mise en page principale
        layout = QVBoxLayout()
        layout.addLayout(gif_layout)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)  # ✅ Correct
        self.setLayout(layout)

    def set_button_image(self, image_path):
        """Met à jour l'image du bouton."""
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        self.button.setIcon(icon)
        self.button.setIconSize(self.button.size())  # Adapter à la taille du bouton

    def on_button_press(self):
        """Change l'image du bouton quand il est pressé."""
        self.set_button_image(self.pressed_image)

    def on_button_release(self):
        """Remet l'image du bouton à l'état normal quand on relâche."""
        self.set_button_image(self.idle_image)
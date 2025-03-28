from PyQt6.QtWidgets import QHBoxLayout, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QMovie, QPixmap, QIcon, QRegion
from PyQt6.QtCore import Qt, QRect
import sys

from gui.TimerDigit import TimerDigit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ferg Timer")
        self.setGeometry(400, 400, 600, 600)

        # Supprimer la barre de titre et rendre la fenêtre transparente
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # === Feuille de fond ===
        self.container = QWidget(self)  # Créer une feuille de fond
        self.container.setStyleSheet("""
            background-color: #2E3440;  /* Fond opaque */
            border-radius: 20px;
        """)
        self.container.setGeometry(0, 0, 600, 600)  # Taille de la feuille

        # Affichage du GIF
        self.gif_label = QLabel(self.container)  # ⬅️ Placer sur la feuille
        movie = QMovie("assets/ferg.gif")
        self.gif_label.setMovie(movie)
        movie.start()

        # Centrer le GIF
        gif_layout = QHBoxLayout()
        gif_layout.addStretch()
        gif_layout.addWidget(self.gif_label)
        gif_layout.addStretch()

        # === Bouton avec image ===
        self.button = QPushButton(self.container)  # ⬅️ Placer sur la feuille
        self.button.setFixedSize(200, 200)
        self.button.setStyleSheet("border: none;")

        self.idle_image = "assets/start_button_idle.png"
        self.pressed_image = "assets/start_button_pressed.png"

        self.set_button_image(self.idle_image)

        self.button.pressed.connect(self.on_button_press)
        self.button.released.connect(self.on_button_release)

        # === Bouton de fermeture avec une image ===
        self.close_button = QPushButton(self.container)  # Placer sur la feuille
        self.close_button.setFixedSize(40, 40)  # Adapter la taille
        self.set_close_button_image("assets/close_button.png")  # Appliquer l’image

        self.close_button.setStyleSheet("border: none;")  # Supprimer la bordure
        self.close_button.clicked.connect(self.close)  # Fermer l'appli au clic

        # === Bouton de réduction avec une image ===
        self.reduce_button = QPushButton(self.container)
        self.reduce_button.setFixedSize(40, 40)  # Taille du bouton
        self.set_reduce_button_image("assets/reduce_button.png")  # Appliquer l’image

        self.reduce_button.setStyleSheet("border: none;")  # Supprimer la bordure
        self.reduce_button.clicked.connect(self.showMinimized)  # Réduire la fenêtre au clic

        # Layout pour les boutons en haut à droite
        close_layout = QHBoxLayout()
        close_layout.addStretch()  # Espace à gauche
        close_layout.addWidget(self.reduce_button)  # Bouton de réduction
        close_layout.addWidget(self.close_button)   # Bouton de fermeture

        # === Layout horizontal pour les chiffres ===
        digits_layout = QHBoxLayout()
        self.h1 = TimerDigit("assets/digits/0.png")  # Heure 1
        self.h2 = TimerDigit("assets/digits/0.png")  # Heure 2
        self.m1 = TimerDigit("assets/digits/0.png")  # Minute 1
        self.m2 = TimerDigit("assets/digits/0.png")  # Minute 2

        # colon_label = QLabel(self)  # Image pour les deux points ":"
        # colon_label.setPixmap(QPixmap("assets/colon.png"))
        # colon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Ajout des éléments dans le layout
        digits_layout.addWidget(self.h1)
        digits_layout.addWidget(self.h2)
        #digits_layout.addWidget(colon_label)
        digits_layout.addWidget(self.m1)
        digits_layout.addWidget(self.m2)

        # Mise en page principale
        layout = QVBoxLayout()
        layout.addLayout(close_layout)  # Boutons de fermeture et réduction
        layout.addLayout(gif_layout)    # GIF
        layout.addLayout(digits_layout) # Digits (H1 H2 : M1 M2)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)  # Bouton Start centré en dessous

        self.container.setLayout(layout)  # ⬅️ Fixer la mise en page au conteneur


    def set_button_image(self, image_path):
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        self.button.setIcon(icon)
        self.button.setIconSize(self.button.size())

    def on_button_press(self):
        self.set_button_image(self.pressed_image)

    def on_button_release(self):
        self.set_button_image(self.idle_image)

    # === Déplacement de la fenêtre ===
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

    def set_close_button_image(self, image_path):
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(self.close_button.size())  # Adapter à la taille

    def set_reduce_button_image(self, image_path):
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        self.reduce_button.setIcon(icon)
        self.reduce_button.setIconSize(self.reduce_button.size())  # Adapter l’icône à la taille
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QMovie, QPixmap, QIcon
from PyQt6.QtCore import Qt, QPoint
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ferg Timer")
        self.setGeometry(500, 500, 500, 500)

        # Supprimer la barre de titre
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Affichage du GIF
        self.gif_label = QLabel(self)
        movie = QMovie("assets/ferg.gif")
        if not movie.isValid():
            print("Erreur : Le GIF n'a pas pu être chargé.")
        self.gif_label.setMovie(movie)
        movie.start()

        # Centrer le GIF
        gif_layout = QHBoxLayout()
        gif_layout.addStretch()
        gif_layout.addWidget(self.gif_label)
        gif_layout.addStretch()

        # === Bouton avec image ===
        self.button = QPushButton(self)
        self.button.setFixedSize(100, 100)
        self.button.setStyleSheet("border: none;")

        self.idle_image = "assets/start_button_idle.png"
        self.pressed_image = "assets/start_button_pressed.png"

        self.set_button_image(self.idle_image)

        self.button.pressed.connect(self.on_button_press)
        self.button.released.connect(self.on_button_release)

        # Bouton de fermeture
        self.close_button = QPushButton("X", self)
        self.close_button.setFixedSize(40, 40)
        self.close_button.setStyleSheet("background-color: red; color: white; font-size: 16px; border-radius: 20px;")
        self.close_button.clicked.connect(self.close)

        # Layout pour le bouton de fermeture
        close_layout = QHBoxLayout()
        close_layout.addStretch()
        close_layout.addWidget(self.close_button)

        # Mise en page principale
        layout = QVBoxLayout()
        layout.addLayout(close_layout)  # Ajoute le bouton de fermeture en haut
        layout.addLayout(gif_layout)
        layout.addWidget(self.button, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout)

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
        """ Capture la position de la souris """
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """ Déplace la fenêtre quand la souris bouge """
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()

    def keyPressEvent(self, event):
        """ Fermer la fenêtre avec Échap """
        if event.key() == Qt.Key.Key_Escape:
            self.close()

# Lancer l'application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

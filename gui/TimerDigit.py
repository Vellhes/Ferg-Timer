from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QWidget
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class TimerDigit(QWidget):
    def __init__(self, image_digit):
        super().__init__()

        self.value = 0

        # === Bouton flèche du haut ===
        self.up_button = QPushButton()
        self.up_button.setFixedSize(50,50)
        self.set_button_image(self.up_button, "assets/arrow_up.png")
        self.up_button.clicked.connect(self.increment_value)

        # === Bouton flèche du bas ===
        self.down_button = QPushButton()
        self.down_button.setFixedSize(50,50)
        self.set_button_image(self.down_button, "assets/arrow_down.png")
        self.down_button.clicked.connect(self.decrement_value)

        # === Image affichant le chiffre ===
        self.digit_label = QLabel(self)
        self.digit_label.setPixmap(QPixmap(image_digit).scaled(50, 80, Qt.AspectRatioMode.KeepAspectRatio))  # Ajuste la taille du chiffre
        self.digit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # === Layout vertical ===
        layout = QVBoxLayout()
        layout.addWidget(self.up_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.digit_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.down_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(layout)

    def set_button_image(self, button, image_path):
        """Definit une image sur un bouton"""
        pixmap = QPixmap(image_path)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(button.size())

    def set_digit_image(self, image_path):
        """Definit une image pour le chiffre"""
        pixmap = QPixmap(image_path)
        self.digit_label.setPixmap(pixmap)

    def update_digit_image(self):
        """Met à jour l'image du chiffre en fonction de la valeur actuelle"""
        image_path = f"assests/digits/{self.value}.png"
        self.set_digit_image(image_path)

    def increment_value(self):
        """Incrémente le chiffre affiché"""
        self.value = (self.value + 1) % 10
        self.update_digit_image()

    def decrement_value(self):
        """Décrémente le chiffre affiché"""
        self.value = (self.value - 1) % 10
        self.update_digit_image()
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from quantum_ui import Ui_MainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QTimer

class QuantumGame(QMainWindow):

    def __init__(self):
        super().__init__()

        self.current_state = "0"
        self.current_player = 1

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.H_Player1.clicked.connect(self.apply_h) # connect signals to slots
        self.ui.X_Player1.clicked.connect(self.apply_x)
        self.ui.Y_Player1.clicked.connect(self.apply_y)
        self.ui.Z_Player1.clicked.connect(self.apply_z)

        self.ui.H_Player2.clicked.connect(self.apply_h)
        self.ui.X_Player2.clicked.connect(self.apply_x)
        self.ui.Y_Player2.clicked.connect(self.apply_y)
        self.ui.Z_Player2.clicked.connect(self.apply_z)

        self.update_turn()

    def apply_h(self):
        if self.current_state == "0":
            self.current_state = "+"
        elif self.current_state == "1":
            self.current_state = "-"
        elif self.current_state == "+":
            self.current_state = "0"
        elif self.current_state == "-":
            self.current_state = "1"
        elif self.current_state == "+i":
            self.current_state = "-i"
        elif self.current_state == "-i":
            self.current_state = "+i"
        self.update_images()
        self.switch_turn()


    def apply_x(self):
        transitions = {
            "0": "1",
            "1": "0",
            "+": "+",
            "-": "-",
            "+i": "-i",
            "-i": "+i"
        }
        self.current_state = transitions[self.current_state]
        self.update_images()
        self.switch_turn()


    def apply_y(self):
        transitions = {
            "0": "1",
            "1": "0",
            "+": "-",
            "-": "+",
            "+i": "+i",
            "-i": "-i"
        }
        self.current_state = transitions[self.current_state]
        self.update_images()
        self.switch_turn()

    def apply_z(self):
        transitions = {
            "0": "0",
            "1": "1",
            "+": "-",
            "-": "+",
            "+i": "-i",
            "-i": "+i"
        }
        self.current_state = transitions[self.current_state]
        self.update_images()
        self.switch_turn()


    def update_turn(self):

        player1_buttons = [
            self.ui.H_Player1,
            self.ui.X_Player1,
            self.ui.Y_Player1,
            self.ui.Z_Player1
        ]

        player2_buttons = [
            self.ui.H_Player2,
            self.ui.X_Player2,
            self.ui.Y_Player2,
            self.ui.Z_Player2
        ]

        for button in player1_buttons:
            button.setEnabled(self.current_player == 1)

        for button in player2_buttons:
            button.setEnabled(self.current_player == 2)


    def switch_turn(self):
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1
        self.update_turn()

    def update_images(self):

        bloch_path = f"images/bloch_{self.current_state}.jpg"
        equation_path = f"images/equation_{self.current_state}.jpg"

        bloch_pixmap = QPixmap(bloch_path)
        equation_pixmap = QPixmap(equation_path)

        self.ui.blochSphereLabel.setPixmap(
            bloch_pixmap.scaled(
                self.ui.blochSphereLabel.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        self.ui.State_Equation_Label.setPixmap(
            equation_pixmap.scaled(
                self.ui.State_Equation_Label.size(),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QuantumGame()
    window.show()

    sys.exit(app.exec())
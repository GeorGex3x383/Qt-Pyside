from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola Mundo")
        boton = QPushButton("botón")
        self.setCentralWidget(boton)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec_())
import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QFileDialog
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from imgiterator import SimpleIterator


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        """
        Сoздаем простое окно с меткой для отображения изображений, кнопкой для переключения между изображениями и кнопкой для выбора папки с данными
        """
        super().__init__()
        self.setWindowTitle("Dataset Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.imgiterator = None
        self.image_label = QLabel("No Image Loaded")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("border: 1px solid black;")
        self.next_button = QPushButton("Next Image")
        self.next_button.clicked.connect(self.show_next_image)
        self.select_folder_button = QPushButton("Select Dataset Folder")
        self.select_folder_button.clicked.connect(self.select_folder)
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.next_button)
        layout.addWidget(self.select_folder_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def select_folder(self):
        """
        Открываем диалоговое окно выбора папки и обработку выбора пользователя.
        """
        file_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if file_path:
            self.imgiterator = SimpleIterator(file_path)
            self.show_next_image()


    def show_next_image(self):
        """
        Отображаем следующее изображения из выбранного набора данных.
        """
        if self.imgiterator is None:
            self.image_label.setText("No Dataset Selected")
            return
        try:
            image_path = next(self.imgiterator)
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(
                pixmap.scaled(
                    self.image_label.size(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )
            )
        except StopIteration:
            self.image_label.setText("No More Images in Dataset")


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        print(e)

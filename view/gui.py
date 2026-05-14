import sys

from PySide6 import QtCore, QtGui, QtWidgets

from controller.controller import Controller


class FloatingWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.drag_pos = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Hasher Core")
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
            | QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(480, 520)

        self.main_container = QtWidgets.QWidget(self)
        self.main_container.setGeometry(0, 0, 480, 520)
        self.main_container.setStyleSheet("""
            QWidget#mainContainer {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a2e,
                    stop:1 #16213e
                );
                border: 2px solid #0f3460;
                border-radius: 16px;
            }
            QLabel#titleLabel {
                color: #e94560;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Consolas', 'Courier New', monospace;
            }
            QLabel#subtitleLabel {
                color: #a0a0b0;
                font-size: 11px;
                font-family: 'Consolas', 'Courier New', monospace;
            }
            QLabel#captionLabel {
                color: #c0c0d0;
                font-size: 13px;
                font-family: 'Segoe UI', sans-serif;
            }
            QLineEdit {
                background: #0f3460;
                color: #ffffff;
                border: 1px solid #1a5276;
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 14px;
                font-family: 'Consolas', 'Courier New', monospace;
                selection-background-color: #e94560;
            }
            QLineEdit:focus {
                border: 1px solid #e94560;
            }
            QComboBox {
                background: #0f3460;
                color: #ffffff;
                border: 1px solid #1a5276;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 13px;
                font-family: 'Segoe UI', sans-serif;
                min-height: 20px;
            }
            QComboBox:focus {
                border: 1px solid #e94560;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 8px solid #e94560;
                margin-right: 8px;
            }
            QComboBox QAbstractItemView {
                background: #16213e;
                color: #ffffff;
                border: 1px solid #0f3460;
                border-radius: 6px;
                selection-background-color: #e94560;
                outline: none;
            }
            QPushButton#hashButton {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #e94560,
                    stop:1 #c23152
                );
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                font-family: 'Segoe UI', sans-serif;
            }
            QPushButton#hashButton:hover {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #ff5a78,
                    stop:1 #e94560
                );
            }
            QPushButton#hashButton:pressed {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #c23152,
                    stop:1 #a01e3e
                );
            }
            QPushButton#copyButton {
                background: transparent;
                color: #e94560;
                border: 1px solid #e94560;
                border-radius: 8px;
                padding: 8px;
                font-size: 12px;
                font-family: 'Segoe UI', sans-serif;
            }
            QPushButton#copyButton:hover {
                background: #e94560;
                color: #ffffff;
            }
            QPushButton#closeButton {
                background: transparent;
                color: #666680;
                border: none;
                font-size: 18px;
                font-weight: bold;
                padding: 4px 10px;
            }
            QPushButton#closeButton:hover {
                color: #e94560;
            }
            QTextEdit {
                background: #0a0a1a;
                color: #00ff88;
                border: 1px solid #1a5276;
                border-radius: 8px;
                padding: 10px;
                font-size: 13px;
                font-family: 'Consolas', 'Courier New', monospace;
                selection-background-color: #e94560;
            }
            QTextEdit:focus {
                border: 1px solid #e94560;
            }
        """)

        self.main_container.setObjectName("mainContainer")

        layout = QtWidgets.QVBoxLayout(self.main_container)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(10)

        title_bar = QtWidgets.QHBoxLayout()
        title_bar.setContentsMargins(0, 0, 0, 0)

        title_label = QtWidgets.QLabel("☰ Hasher Core")
        title_label.setObjectName("titleLabel")
        title_bar.addWidget(title_label)

        title_bar.addStretch()

        self.close_btn = QtWidgets.QPushButton("✕")
        self.close_btn.setObjectName("closeButton")
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.clicked.connect(self.close)
        title_bar.addWidget(self.close_btn)

        layout.addLayout(title_bar)

        subtitle = QtWidgets.QLabel("by k1rpit  •  Cryptographic Hash Tool")
        subtitle.setObjectName("subtitleLabel")
        layout.addWidget(subtitle)

        layout.addSpacing(6)

        caption = QtWidgets.QLabel("Введите текст для хеширования:")
        caption.setObjectName("captionLabel")
        layout.addWidget(caption)

        self.input_field = QtWidgets.QLineEdit()
        self.input_field.setPlaceholderText("Введите строку...")
        self.input_field.returnPressed.connect(self.compute_hash)
        layout.addWidget(self.input_field)

        method_row = QtWidgets.QHBoxLayout()
        method_row.setContentsMargins(0, 0, 0, 0)
        method_row.setSpacing(10)

        self.method_combo = QtWidgets.QComboBox()
        for m in self.controller.get_available_methods():
            self.method_combo.addItem(m["label"], m["name"])
        method_row.addWidget(self.method_combo, 1)

        self.hash_btn = QtWidgets.QPushButton("Вычислить хеш")
        self.hash_btn.setObjectName("hashButton")
        self.hash_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hash_btn.clicked.connect(self.compute_hash)
        method_row.addWidget(self.hash_btn, 0)

        layout.addLayout(method_row)

        result_label = QtWidgets.QLabel("Результат:")
        result_label.setObjectName("captionLabel")
        layout.addWidget(result_label)

        self.result_output = QtWidgets.QTextEdit()
        self.result_output.setReadOnly(True)
        self.result_output.setPlaceholderText("Здесь будет результат...")
        layout.addWidget(self.result_output, 1)

        bottom_row = QtWidgets.QHBoxLayout()
        bottom_row.setContentsMargins(0, 0, 0, 0)

        self.copy_btn = QtWidgets.QPushButton("📋 Копировать")
        self.copy_btn.setObjectName("copyButton")
        self.copy_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_btn.clicked.connect(self.copy_result)
        bottom_row.addWidget(self.copy_btn)

        bottom_row.addStretch()

        status = QtWidgets.QLabel("Готов")
        status.setObjectName("subtitleLabel")
        self.status_label = status
        bottom_row.addWidget(status)

        layout.addLayout(bottom_row)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_pos = (
                event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton and self.drag_pos is not None:
            self.move(event.globalPosition().toPoint() - self.drag_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_pos = None

    def compute_hash(self):
        text = self.input_field.text().strip()
        if not text:
            self.status_label.setText("⚠ Введите текст")
            return

        method_name = self.method_combo.currentData()
        result = self.controller.compute_hash(method_name, text)
        self.result_output.setText(result)
        self.status_label.setText(f"✓ {self.method_combo.currentText()} ✓")

    def copy_result(self):
        text = self.result_output.toPlainText()
        if not text:
            self.status_label.setText("⚠ Нет результата для копирования")
            return

        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(text)
        self.status_label.setText("✓ Скопировано в буфер обмена")


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = FloatingWindow()
    window.show()
    sys.exit(app.exec())

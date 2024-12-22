from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFrame
from PyQt6.QtCore import Qt

class CollapsibleSection(QWidget):
    def __init__(self, title="Solution", parent=None):
        super().__init__(parent)
        self.toggle_button = QPushButton(f"▶ Show {title}")
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: #2d2d2d;
                color: #ffffff;
                border: none;
                padding: 5px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #3d3d3d;
            }
        """)
        self.content_area = QFrame()
        self.content_area.setVisible(False)
        
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.toggle_button)
        self.mainLayout.addWidget(self.content_area)
        
        self.toggle_button.clicked.connect(self.toggle_content)
        
    def toggle_content(self):
        is_visible = self.content_area.isVisible()
        self.content_area.setVisible(not is_visible)
        self.toggle_button.setText(f"{'▼' if not is_visible else '▶'} Show Solution")
        
    def setContentLayout(self, layout):
        if self.content_area.layout():
            QWidget().setLayout(self.content_area.layout())
        self.content_area.setLayout(layout)
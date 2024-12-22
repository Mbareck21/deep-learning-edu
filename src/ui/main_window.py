from PyQt6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
                               QPushButton, QLabel, QStatusBar, QSplitter, QStackedWidget)
from PyQt6.QtCore import Qt
from ..utils.environment import Environment
from ..lessons.deep_learning_basics import DeepLearningBasics
from ..lessons.pytorch_fundamentals import PyTorchFundamentals
from ..lessons.neural_networks import NeuralNetworks
from ..lessons.training_optimization import TrainingOptimization
from ..lessons.projects import Projects
from .styles import DARK_THEME

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Deep Learning Fundamentals")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet(DARK_THEME['main_window'])
        
        self.lessons = {
            "Deep Learning Basics": DeepLearningBasics(self),
            "PyTorch Fundamentals": PyTorchFundamentals(self),
            "Neural Networks": NeuralNetworks(self),
            "Training & Optimization": TrainingOptimization(self),
            "Projects": Projects(self)
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        self.statusBar = QStatusBar()
        self.statusBar.setStyleSheet(DARK_THEME['status_bar'])
        self.setStatusBar(self.statusBar)
        self.update_status()
        
        main_splitter = QSplitter(Qt.Orientation.Horizontal)
        self.setCentralWidget(main_splitter)
        
        # Navigation panel
        nav_widget = QWidget()
        nav_widget.setMaximumWidth(250)
        nav_layout = QVBoxLayout(nav_widget)
        nav_layout.setSpacing(5)
        nav_layout.setContentsMargins(10, 10, 10, 10)
        
        header = QLabel("Deep Learning\nFundamentals")
        header.setStyleSheet(DARK_THEME['header'])
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nav_layout.addWidget(header)
        
        self.setup_navigation(nav_layout)
        nav_layout.addStretch()
        
        # Content area
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        
        self.content_stack = QStackedWidget()
        for lesson in self.lessons.values():
            self.content_stack.addWidget(lesson)
            
        content_layout.addWidget(self.content_stack)
        
        main_splitter.addWidget(nav_widget)
        main_splitter.addWidget(content_widget)
        main_splitter.setSizes([250, 950])
    
    def setup_navigation(self, layout):
        for text in self.lessons.keys():
            btn = QPushButton(text)
            btn.setStyleSheet(DARK_THEME['nav_button'])
            btn.setFixedHeight(50)
            btn.clicked.connect(lambda checked, t=text: self.show_lesson(t))
            layout.addWidget(btn)
    
    def show_lesson(self, lesson_name):
        if lesson_name in self.lessons:
            lesson_widget = self.lessons[lesson_name]
            self.content_stack.setCurrentWidget(lesson_widget)
    
    def update_status(self):
        env = Environment()
        device = env.get_device()
        self.statusBar.showMessage(f"Running on: {device} | {env.get_requirements()['pytorch']}")
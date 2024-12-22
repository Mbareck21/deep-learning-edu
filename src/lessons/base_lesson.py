from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTextEdit, 
                               QSplitter, QFrame, QPlainTextEdit, QPushButton)
from PyQt6.QtCore import Qt
import re
from ..ui.code_editor import CodeEditor
from ..ui.markdown_viewer import MarkdownViewer
from ..ui.collapsible import CollapsibleSection

class BaseLesson(QWidget):
    def __init__(self, title, content, parent=None):
        super().__init__(parent)
        self.title = title
        self.content = content
        self.setup_ui()
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Horizontal splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Content area (left side)
        content_widget = QFrame()
        content_widget.setFrameStyle(QFrame.Shape.StyledPanel)
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        # Title
        title_label = QLabel(self.title)
        title_label.setStyleSheet("""
            font-size: 24px;
            color: white;
            padding: 10px;
            background-color: #2d2d2d;
            border-radius: 5px;
            margin-bottom: 20px;
        """)
        content_layout.addWidget(title_label)
        
        # Process content and add collapsible solutions
        content_parts = re.split(r'<solution>(.*?)</solution>', self.content, flags=re.DOTALL)
        viewer = MarkdownViewer()
        for i, part in enumerate(content_parts):
            if i % 2 == 0:
                # Regular content
                viewer.append_markdown(part)
            else:
                # Solution
                solution = CollapsibleSection("Solution")
                solution_layout = QVBoxLayout()
                solution_viewer = MarkdownViewer()
                solution_viewer.set_markdown(part)
                solution_layout.addWidget(solution_viewer)
                solution.setContentLayout(solution_layout)
                viewer.append_widget(solution)
        
        content_layout.addWidget(viewer)
        
        # Code area (right side)
        code_widget = QFrame()
        code_widget.setFrameStyle(QFrame.Shape.StyledPanel)
        code_layout = QVBoxLayout(code_widget)
        code_layout.setContentsMargins(20, 20, 20, 20)
        
        code_label = QLabel("Interactive Code")
        code_label.setStyleSheet("""
            font-size: 20px;
            color: white;
            padding: 10px;
            background-color: #2d2d2d;
            border-radius: 5px;
            margin-bottom: 20px;
        """)
        code_layout.addWidget(code_label)
        
        self.code_editor = CodeEditor()
        code_layout.addWidget(self.code_editor)
        
        # Add widgets to splitter
        splitter.addWidget(content_widget)
        splitter.addWidget(code_widget)
        splitter.setSizes([480, 720])
        
        layout.addWidget(splitter)
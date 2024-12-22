from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPlainTextEdit, 
                               QPushButton, QTextEdit)
from PyQt6.QtCore import QProcess, Qt
from PyQt6.QtGui import QTextCursor
import sys
import os
import tempfile

class CodeEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.process = None
        self.temp_dir = tempfile.mkdtemp()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        
        self.editor = QPlainTextEdit()
        self.editor.setStyleSheet("""
            QPlainTextEdit {
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 14px;
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: 1px solid #3c3f41;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("""
            QTextEdit {
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 14px;
                background-color: #1e1e1e;
                color: #00ff00;
                border: 1px solid #3c3f41;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        
        run_button = QPushButton("▶ Run Code")
        run_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        run_button.clicked.connect(self.run_code)
        
        layout.addWidget(self.editor, stretch=2)
        layout.addWidget(run_button)
        layout.addWidget(self.output, stretch=1)
    
    def run_code(self):
        if self.process is not None:
            self.process.kill()
            self.process.waitForFinished()
        
        self.output.clear()
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)
        
        code = self.editor.toPlainText()
        temp_file = os.path.join(self.temp_dir, "temp_code.py")
        with open(temp_file, "w", encoding='utf-8') as f:
            f.write(code)
        
        python_path = sys.executable
        self.process.start(python_path, [temp_file])
    
    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode('utf-8')
        cursor = self.output.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(stdout)
    
    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode('utf-8')
        cursor = self.output.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(f'Error: {stderr}')
    
    def process_finished(self):
        if self.process.exitCode() == 0:
            self.output.append("\nExecution completed successfully!")
        else:
            self.output.append(f"\nProcess exited with code {self.process.exitCode()}")
    
    def closeEvent(self, event):
        if self.process is not None:
            self.process.kill()
            self.process.waitForFinished()
        super().closeEvent(event)
from PyQt6.QtWidgets import QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtGui import QTextCharFormat, QColor, QFont
from PyQt6.QtCore import Qt
import re

class MarkdownViewer(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                border: none;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 14px;
                padding: 10px;
            }
        """)
    
    def set_markdown(self, text):
        self.clear()
        self.append_markdown(text)
    
    def append_markdown(self, text):
        # Headers
        text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.M)
        text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.M)
        text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.M)
        
        # Code blocks
        text = re.sub(r'```python(.*?)```', lambda m: self._format_code(m.group(1)), 
                     text, flags=re.M | re.S)
        
        # Lists
        text = re.sub(r'^- (.*?)$', r'• \1', text, flags=re.M)
        
        # Bold
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        
        # Italic
        text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
        
        # Style headers
        text = text.replace('<h1>', '<h1 style="color: #569CD6; font-size: 24px;">')
        text = text.replace('<h2>', '<h2 style="color: #4EC9B0; font-size: 20px;">')
        text = text.replace('<h3>', '<h3 style="color: #CE9178; font-size: 16px;">')
        
        self.insertHtml(text)
        cursor = self.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.setTextCursor(cursor)
    
    def append_widget(self, widget):
        cursor = self.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.setTextCursor(cursor)
        cursor.insertHtml("<br>")
        
        text_block_format = cursor.blockFormat()
        text_block_format.setAlignment(Qt.AlignmentFlag.AlignLeft)
        cursor.setBlockFormat(text_block_format)
        
        self.insertHtml("<br>")
        cursor = self.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        self.setTextCursor(cursor)
    
    def _format_code(self, code):
        return f'<pre style="background-color: #2d2d2d; padding: 10px; ' \
               f'border-radius: 5px; font-family: Consolas, monospace;">{code}</pre>'
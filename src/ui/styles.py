DARK_THEME = {
    'main_window': """
        QMainWindow {
            background-color: #2b2b2b;
        }
    """,
    'header': """
        QLabel {
            color: #ffffff;
            font-size: 24px;
            margin: 15px;
            padding: 10px;
            background-color: #1e1e1e;
            border-radius: 5px;
        }
    """,
    'nav_button': """
        QPushButton {
            background-color: #3c3f41;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            padding: 10px;
            margin: 5px;
            text-align: left;
            padding-left: 15px;
        }
        QPushButton:hover {
            background-color: #4e5254;
        }
        QPushButton:pressed {
            background-color: #2196F3;
        }
        QPushButton:disabled {
            background-color: #2d2d2d;
            color: #6b6b6b;
        }
    """,
    'code_editor': """
        QPlainTextEdit {
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 12px;
            background-color: #1e1e1e;
            color: #d4d4d4;
            border: 1px solid #3c3f41;
            border-radius: 5px;
            padding: 5px;
        }
    """,
    'output': """
        QTextEdit {
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 12px;
            background-color: #1e1e1e;
            color: #00ff00;
            border: 1px solid #3c3f41;
            border-radius: 5px;
            padding: 5px;
        }
    """,
    'run_button': """
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
        QPushButton:pressed {
            background-color: #0D47A1;
        }
    """,
    'status_bar': """
        QStatusBar {
            background-color: #1e1e1e;
            color: #ffffff;
        }
    """
}
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.highlighting_rules = []

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))
        keyword_format.setFontWeight(QFont.Weight.Bold)
        keywords = [
            "and", "as", "assert", "break", "class", "continue", "def",
            "del", "elif", "else", "except", "False", "finally", "for",
            "from", "global", "if", "import", "in", "is", "lambda", "None",
            "nonlocal", "not", "or", "pass", "raise", "return", "True",
            "try", "while", "with", "yield"
        ]
        self.add_mapping(r'\b(?:' + '|'.join(keywords) + r')\b', keyword_format)

        builtin_format = QTextCharFormat()
        builtin_format.setForeground(QColor("#4EC9B0"))
        builtins = [
            "abs", "all", "any", "bin", "bool", "bytearray", "callable", "chr",
            "classmethod", "compile", "complex", "delattr", "dict", "dir", "divmod",
            "enumerate", "eval", "filter", "float", "format", "frozenset", "getattr",
            "globals", "hasattr", "hash", "help", "hex", "id", "input", "int",
            "isinstance", "issubclass", "iter", "len", "list", "locals", "map", "max",
            "memoryview", "min", "next", "object", "oct", "open", "ord", "pow",
            "print", "property", "range", "repr", "reversed", "round", "set", "setattr",
            "slice", "sorted", "staticmethod", "str", "sum", "super", "tuple", "type",
            "vars", "zip"
        ]
        self.add_mapping(r'\b(?:' + '|'.join(builtins) + r')\b', builtin_format)

        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#CE9178"))
        self.add_mapping(r'"[^"\\]*(\\.[^"\\]*)*"', string_format)
        self.add_mapping(r"'[^'\\]*(\\.[^'\\]*)*'", string_format)

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))
        self.add_mapping(r'#[^\n]*', comment_format)

        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#B5CEA8"))
        self.add_mapping(r'\b\d+\b', number_format)

        decorator_format = QTextCharFormat()
        decorator_format.setForeground(QColor("#D7BA7D"))
        self.add_mapping(r'@\w+', decorator_format)

    def add_mapping(self, pattern, text_format):
        self.highlighting_rules.append((pattern, text_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            matches = Qt.re.finditer(pattern, text)
            for match in matches:
                start = match.start()
                count = match.end() - start
                self.setFormat(start, count, format)
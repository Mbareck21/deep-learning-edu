from .base_lesson import BaseLesson

class Projects(BaseLesson):
    def __init__(self, parent=None):
        content = """# Deep Learning Projects

[Rest of the content remains the same]"""
        super().__init__("Projects", content, parent)
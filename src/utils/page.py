from flask import render_template_string

class Page:
    """store page text"""
    def __init__(self, html_content: str, title: str = "Web App"):
        self.html_content = html_content
        self.title = title
        
    def render(self, **context) -> str:
        """render the content of html,enable to include context vars"""
        return render_template_string(self.html_content,** context)
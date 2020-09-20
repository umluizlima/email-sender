from re import search
from typing import Dict

from jinja2 import Environment, FileSystemLoader, select_autoescape

from app.settings import Settings


class TemplateService:
    def __init__(self, settings: Settings):
        self.env = Environment(
            loader=FileSystemLoader(settings.TEMPLATES_FOLDER),
            autoescape=select_autoescape(["html"]),
        )

    def render_template(self, file_name: str, data: Dict) -> str:
        template = self.env.get_template(file_name)
        return template.render(**data)

    @staticmethod
    def get_title(rendered_template: str) -> str:
        match = search("<title>(.*?)</title>", rendered_template)
        return match.group(1) if match else None

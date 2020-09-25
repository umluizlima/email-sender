from app.core.schemas import EmailSchema, TransactionalSchema
from app.settings import Settings

from .template import TemplateService


class TransactionalService:
    def __init__(self, settings: Settings, template_service: TemplateService):
        self.transactional_templates = settings.TRANSACTIONAL_TEMPLATES
        self.template_service = template_service

    def build_email(self, transactional: TransactionalSchema) -> EmailSchema:
        template = self._get_transactional_template(transactional.transactional_type)
        rendered_template = self.template_service.render_template(
            template, transactional.transactional_data,
        )
        return EmailSchema(
            subject=self.template_service.get_title(rendered_template),
            content=rendered_template,
            **transactional.dict(by_alias=True)
        )

    def _get_transactional_template(self, transactional_type: str) -> str:
        return self.transactional_templates[transactional_type]

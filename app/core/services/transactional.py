from app.core.schemas import EmailSchema, TransactionalSchema, Transactional

from .template import TemplateService


class TransactionalService:
    def __init__(self, template_service: TemplateService):
        self.template_service = template_service

    def build_email(self, transactional: TransactionalSchema) -> EmailSchema:
        rendered_template = self.template_service.render_template(
            Transactional(transactional.transactional_type).template,
            transactional.transactional_data,
        )
        return EmailSchema(
            subject=self.template_service.get_title(rendered_template),
            content=rendered_template,
            **transactional.dict(by_alias=True)
        )

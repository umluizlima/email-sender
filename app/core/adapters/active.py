from pydantic import BaseSettings

from app.settings import EmailService, settings

from . import BaseAdapter, MailjetAdapter, SendgridAdapter

ADAPTERS = {
    EmailService.MAILJET: MailjetAdapter,
    EmailService.SENDGRID: SendgridAdapter,
}


class ActiveAdapter:
    def __init__(self, settings: BaseSettings = settings):
        self.settings = settings

    def __call__(self) -> BaseAdapter:
        return ADAPTERS[self.settings.EMAIL_SERVICE](settings=self.settings)


get_active_adapter = ActiveAdapter()

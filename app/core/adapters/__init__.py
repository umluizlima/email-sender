from app.settings import EmailService, Settings

from .base import BaseAdapter
from .mailjet import MailjetAdapter
from .sendgrid import SendgridAdapter

ADAPTERS = {
    EmailService.MAILJET: MailjetAdapter,
    EmailService.SENDGRID: SendgridAdapter,
}


def get_adapter(settings: Settings) -> BaseAdapter:
    return ADAPTERS[settings.EMAIL_SERVICE](settings=settings)

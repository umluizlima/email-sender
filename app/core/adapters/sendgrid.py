from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

from ..schemas import EmailSchema
from .base import BaseAdapter


class SendgridAdapter(BaseAdapter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = SendGridAPIClient(api_key=self.settings.SENDGRID_API_KEY)

    def send(self, message: EmailSchema):
        try:
            self.client.send(self._prepare_message(message))
        except Exception as error:
            raise Exception(f"Error sending {message}", error)

    @staticmethod
    def _prepare_message(message: EmailSchema) -> Mail:
        from_email = Email(message.from_)
        to_email = To(message.to)
        subject = message.subject
        content = Content(message.content_type, message.content)
        return Mail(from_email, to_email, subject, content)

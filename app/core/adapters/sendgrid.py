from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, Email, Mail, To

from ..schemas import EmailSchema
from .base import BaseAdapter


class SendgridAdapter(BaseAdapter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = SendGridAPIClient(
            api_key=self.settings.SENDGRID_API_KEY.get_secret_value()
        )

    def send(self, message: EmailSchema):
        try:
            self.client.send(self._prepare_message(message))
        except Exception as error:
            raise Exception(f"Error sending {message}", error)

    def _prepare_message(self, message: EmailSchema) -> Mail:
        from_email = Email(message.from_email or self.settings.DEFAULT_EMAIL_ADDRESS)
        to_email = To(message.to_email)
        subject = message.subject
        content = Content(message.content_type, message.content)
        return Mail(from_email, to_email, subject, content)

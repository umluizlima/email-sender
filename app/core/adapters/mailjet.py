from typing import Dict

from mailjet_rest import Client

from ..schemas import EmailSchema
from .base import BaseAdapter


class MailjetAdapter(BaseAdapter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = Client(
            auth=(
                self.settings.MAILJET_API_KEY.get_secret_value(),
                self.settings.MAILJET_API_SECRET.get_secret_value(),
            ),
            version="v3.1",
        )

    def send(self, message: EmailSchema):
        try:
            self.client.send.create(data=self._prepare_message(message))
        except Exception as error:
            raise Exception(f"Error sending {message}", error)

    def _prepare_message(self, message: EmailSchema) -> Dict:
        return {
            "Messages": [
                {
                    "From": {
                        "Email": message.from_ or self.settings.DEFAULT_EMAIL_ADDRESS
                    },
                    "To": [{"Email": message.to}],
                    "Subject": message.subject,
                    MailjetAdapter._get_content_attribute(
                        message.content_type
                    ): message.content,
                }
            ]
        }

    @staticmethod
    def _get_content_attribute(content_type: str) -> str:
        if content_type == "text/plain":
            return "TextPart"
        else:
            return "HTMLPart"

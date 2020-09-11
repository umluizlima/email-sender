from enum import Enum


class EmailService(str, Enum):
    MAILJET = "mailjet"
    SENDGRID = "sendgrid"

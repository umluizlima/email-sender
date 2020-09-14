from abc import ABCMeta, abstractmethod

from app.settings import Settings

from ..schemas import EmailSchema


class BaseAdapter(metaclass=ABCMeta):
    def __init__(self, settings: Settings):
        self.settings = settings

    @abstractmethod
    def send(self, message: EmailSchema):
        ...

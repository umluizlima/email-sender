from abc import ABCMeta, abstractmethod

from pydantic import BaseSettings

from app.settings import settings

from ..schemas import EmailSchema


class BaseAdapter(metaclass=ABCMeta):
    def __init__(self, settings: BaseSettings = settings):
        self.settings = settings

    @abstractmethod
    def send(self, message: EmailSchema):
        ...

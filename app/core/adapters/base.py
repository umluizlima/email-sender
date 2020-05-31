from abc import ABCMeta, abstractmethod

from pydantic import BaseSettings

from ..schemas import EmailSchema


class BaseAdapter(metaclass=ABCMeta):
    def __init__(self, settings: BaseSettings):
        self.settings = settings

    @abstractmethod
    def send(self, message: EmailSchema):
        ...

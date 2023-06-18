from abc import ABCMeta, abstractmethod

from src.models.error import ErrorModel


class DObserver(metaclass=ABCMeta):

    @abstractmethod
    def model_changed(self):
        """
        Метод, который будет вызван у наблюдателя при изменении модели.
        """
        pass

    @abstractmethod
    def error_handler(self, error: ErrorModel):
        """
        Метод, который будет вызван у наблюдателя при возникновении ошибки.
        """
        pass

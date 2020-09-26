from abc import ABC, abstractmethod


class Veggie(ABC):
    @abstractmethod
    def __str__(self):
        pass


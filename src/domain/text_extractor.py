from abc import ABC, abstractmethod

class TextExtractor(ABC):
    @abstractmethod
    def extract(self, text: str):
        pass

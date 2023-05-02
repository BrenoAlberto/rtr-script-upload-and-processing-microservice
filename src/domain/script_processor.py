from abc import ABC, abstractmethod
from .play_script import PlayScript

class ScriptProcessor(ABC):
    @abstractmethod
    def process(self, content: str) -> PlayScript:
        pass

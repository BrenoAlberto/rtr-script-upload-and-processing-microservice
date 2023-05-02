import re
from src.domain.scene_splitter import SceneSplitter


class RegexSceneSplitter(SceneSplitter):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def extract(self, text: str):
        return re.split(self.pattern, text)

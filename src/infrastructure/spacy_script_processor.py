import re
from src.domain.script_processor import ScriptProcessor
from src.domain.play_script import PlayScript
from src.infrastructure.spacy_character_extractor import SpacyCharacterExtractor
from src.infrastructure.regex_scene_splitter import RegexSceneSplitter


class SpacyScriptProcessor(ScriptProcessor):
    def __init__(self):
        self.character_extractor = SpacyCharacterExtractor()
        self.scene_splitter = RegexSceneSplitter(r"\bSCENE\s+\d+\b")

    def preprocess_text(self, text):
        return re.sub(r"\s+", " ", text.strip())

    def process(self, content: str) -> PlayScript:
        content = self.preprocess_text(content)
        characters = self.character_extractor.extract(content)
        scenes = self.scene_splitter.extract(content)
        return PlayScript(content, characters, scenes)

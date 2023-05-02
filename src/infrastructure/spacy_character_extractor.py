import spacy
from src.domain.character_extractor import CharacterExtractor


class SpacyCharacterExtractor(CharacterExtractor):
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract(self, text: str):
        doc = self.nlp(text)
        characters = set()
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                characters.add(ent.text)
        return sorted(list(characters))

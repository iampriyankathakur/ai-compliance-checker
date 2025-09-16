import spacy

def load_model():
    return spacy.load("en_core_web_sm")

def extract_entities(text: str, nlp=None):
    if nlp is None:
        nlp = load_model()
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

import spacy

nlp = spacy.load("en_core_web_sm")

def extract_claim(text: str) -> str:
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences[0] if sentences else text

if __name__ == "__main__":
    print(extract_claim("Einstein invented the telephone."))

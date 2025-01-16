import spacy

if __name__ == "__main__":
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("The Job Application Customizer is working!")
    for token in doc:
        print(f"{token.text} -> {token.pos_}")

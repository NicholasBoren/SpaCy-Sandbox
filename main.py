import spacy

with open ("./data/alice.txt", "r") as f:
    text = f.read()

    chapters = text.split("CHAPTER ")[1:]

NLP = spacy.load("en_core_web_md")

chapter1 = chapters[0]

doc = NLP(chapter1)
sentences = list(doc.sents)
sentence = sentences[2]

chunks = list(doc.noun_chunks)
for chunk in chunks:       
    if "watch" in str(chunks):   
        pass
        print(chunk)

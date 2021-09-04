import spacy
import contextualSpellCheck

with open ("./data/alice.txt", "r") as f:
    text = f.read()

    chapters = text.split("CHAPTER ")[1:]

nlp = spacy.load("en_core_web_md")
nlp.add_pipe("contextual spellchecker")


chapter1 = chapters[0]

doc = nlp(chapter1)
print(doc._.suggestions_spellCheck)
sentences = list(doc.sents)
sentence = sentences[2]

chunks = list(doc.noun_chunks)
for chunk in chunks:       
    if "watch" in str(chunks):   
        pass
        #print(chunk)

import spacy

nlp = spacy.blank("en")

#breaks in spacy 3.x :(
nlp.add_pipe("ner")
nlp.add_label("CONC_CAMP")

nlp.add_pipe("ner", name="conc_camp_ner")

nlp.to_disk("holocaust_ner")

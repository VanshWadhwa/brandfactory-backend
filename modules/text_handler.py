# python -m spacy download en_core_web_sm

import spacy
import re

# Load English tokenizer, tagger, parser, NER and word vectors


# Process whole documents
# text = ("When Sebastian Thrun started working on self-driving cars at "
#         "Google in 2007, few people outside of the company took him "
#         "seriously. “I can tell you very senior CEOs of major American "
#         "car companies would shake my hand and turn away because I wasn’t "
#         "worth talking to,” said Thrun, in an interview with Recode earlier "
#         "this week.")

# text = ("Alibaba loses $60 bn m-cap after China starts anti-monopoly investigation Pilot fired after Taiwan blames him for first local Covid-19 case in 253 days Aurobindo Pharma to make COVAXX's COVID-19 vaccine for India, UNICEF US faces government shutdown as Trump threatens not to sign spending bill")
# text = "Elon Reeve Musk FRS is a business magnate, industrial designer and engineer. He is the founder, CEO, CTO and chief designer of SpaceX; early investor, CEO and product architect of Tesla, Inc.; founder of The Boring Company; co-founder of Neuralink; and co-founder and initial co-chairman of OpenAI."

# text = "Biggest Bangladeshi IPO in a decade surges 50% on debut in Dhaka"
# text = "This Returns a tuple of important words and the index at which they appear"

# Analyze syntax

def importantWords(text):
    """This Returns a tuple of important words and the index at which they appear"""
    # text = repr(text)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
    # print("Pronouns:", [token.lemma_ for token in doc if token.pos_ == "PROPN"])

    # print(" : " , [token.text , token.pos  for token in doc if True])
    my_dict = {}
    for token in doc:
        if token.pos_ == "PROPN":
            
            match = re.search((token.text),text)
            if match != None:
                my_dict[token.text] = (match.start() , match.end())
    # if my_dict == None:
    #     my_dict  = {"":(-1,-1),}
    return my_dict
        # print(token.text , token.pos_)

    # Find named entities, phrases and concepts

    # print("In entity")
    # for entity in doc.ents:
    #     print(entity.text, entity.label_)
    
    


# print(importantWords(text))
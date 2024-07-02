import spacy
from spacy import displacy

# Load default input text
def get_default_input():
  return """When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously. “I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,” said Thrun, now the co-founder and CEO of online higher education startup Udacity, in an interview with Recode earlier this week. A little less than a decade later, dozens of self-driving startups have cropped up while automakers around the world clamor, wallet in hand, to secure their place in the fast-moving world of fully automated transportation.
"""

# Process input text with selected model and its NLP pipeline
def process_text(input_text, model):
  nlp = spacy.load(model)
  nlp.add_pipe(
    "entityfishing",
    config={
      "api_ef_base": "http://nerd.huma-num.fr/nerd/service"
    }
    )
  doc = nlp(input_text)
  return doc

# Render entities using displacy.render function - https://spacy.io/usage/visualizers
def render_entities(doc, selected_options):
  options = {'ents': selected_options, 'colors': get_entity_colors()}
  return displacy.render(doc, style='ent', jupyter=False, options=options)

# Dictionary for entity colors
def get_entity_colors():
  return {
    'CARDINAL': 'LimeGreen',
    'DATE': 'LightSalmon',
    'EVENT': 'Olive',
    'FAC': 'SlateBlue',
    'GPE': 'Teal',
    'LANGUAGE': 'Orange',
    'LAW': 'FireBrick',
    'LOC': 'CadetBlue',
    'MONEY': 'LightSkyBlue',
    'NORP': 'DeepPink',
    'ORDINAL': 'DarkCyan',
    'ORG': 'IndianRed',
    'PERCENT': '#FF0000',
    'PERSON': 'Peru',
    'PRODUCT': 'DarkOrange',
    'QUANTITY': 'RosyBrown',
    'TIME': 'DarkSeaGreen',
    'WORK_OF_ART': 'DodgerBlue',
    'PER': 'Peru',
    'MISC': 'Aqua',
  }
  
def get_entity_label_examples():
  return {
    'CARDINAL': '3.14 - https://www.wikidata.org/wiki/Q167',
    'DATE': 'Christmas Eve - https://www.wikidata.org/wiki/Q106010',
    'EVENT': 'Olympics - https://www.wikidata.org/wiki/Q5389',
    'FAC': 'Golden Gate Bridge - https://www.wikidata.org/wiki/Q44440',
    'GPE': 'Prague - https://www.wikidata.org/wiki/Q1085',
    'LANGUAGE': 'English - https://www.wikidata.org/wiki/Q1860',
    'LAW': 'Consitution - https://www.wikidata.org/wiki/Q11698',
    'LOC': 'Atlantic Ocean - https://www.wikidata.org/wiki/Q97',
    'MONEY': '60,000 - https://www.wikidata.org/wiki/Q3271915',
    'NORP': 'Czech - https://www.wikidata.org/wiki/Q170217',
    'ORDINAL': '**very high ambiguity - hard to link against Wikidata**',
    'ORG': 'Google - https://www.wikidata.org/wiki/Q95',
    'PERCENT': '**very high ambiguity - hard to link against Wikidata**',
    'PERSON': 'Sam Altman - https://www.wikidata.org/wiki/Q7407093',
    'PRODUCT': 'Twitter - https://www.wikidata.org/wiki/Q918',
    'QUANTITY': '**very high ambiguity - hard to link against Wikidata**',
    'TIME': '**very high ambiguity - hard to link against Wikidata**',
    'WORK_OF_ART': 'The Great Gatsby - https://www.wikidata.org/wiki/Q214371',
    'PER': 'Albert Einstein - https://www.wikidata.org/wiki/Q937',
    'MISC': 'Reyes - https://www.wikidata.org/wiki/Q16236481',
  }
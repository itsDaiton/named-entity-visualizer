import spacy
from spacy import displacy

# Load default input text
def get_default_input():
  return """When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously. “I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,” said Thrun, now the co-founder and CEO of online higher education startup Udacity, in an interview with Recode earlier this week. A little less than a decade later, dozens of self-driving startups have cropped up while automakers around the world clamor, wallet in hand, to secure their place in the fast-moving world of fully automated transportation.
"""

# Process input text with selected model and its NLP pipeline
def process_text(input_text, model):
  nlp = spacy.load(model)
  nlp.add_pipe("entityfishing")
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
    'WORK_OF_ART': 'MidnightBlue',
    'PER': 'Peru',
    'MISC': 'Aqua',
    'date': 'LightSalmon',
    'geogName': 'Teal',
    'orgName': 'IndianRed',
    'persName': 'Peru',
    'placeName': 'CadetBlue',
    'time': 'DarkSeaGreen',
  }
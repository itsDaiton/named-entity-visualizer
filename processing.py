import streamlit as st
import spacy
from spacy import displacy

def get_default_input():
  return """When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously. “I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,” said Thrun, now the co-founder and CEO of online higher education startup Udacity, in an interview with Recode earlier this week. A little less than a decade later, dozens of self-driving startups have cropped up while automakers around the world clamor, wallet in hand, to secure their place in the fast-moving world of fully automated transportation.
"""

def process_text(input_text, model):
  nlp = spacy.load(model)
  doc = nlp(input_text)
  return doc

def render_entities(doc):
  return displacy.render(doc, style='ent', jupyter=False)
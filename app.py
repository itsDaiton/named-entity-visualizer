import streamlit as st
import spacy
from spacy import displacy
from layout import load_main, load_sidebar

nlp = spacy.load('en_core_web_md')
nlp = spacy.load('en_core_web_sm')

load_sidebar()
load_main()

input = """When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously. “I can tell you very senior CEOs of major American car companies would shake my hand and turn away because I wasn’t worth talking to,” said Thrun, now the co-founder and CEO of online higher education startup Udacity, in an interview with Recode earlier this week.
A little less than a decade later, dozens of self-driving startups have cropped up while automakers around the world clamor, wallet in hand, to secure their place in the fast-moving world of fully automated transportation.
"""

input_text = st.text_area('Text to analyze:', input)
doc = nlp(input_text)

st.header('Entities found on the Wikidata')
ent_html = displacy.render(doc, style='ent', jupyter=False)
st.markdown(ent_html, unsafe_allow_html=True)
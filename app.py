import streamlit as st
import spacy
from processing import process_text, render_entities, get_default_input, get_entity_colors

# Load models only when necessary - https://docs.streamlit.io/library/advanced-features/caching
@st.cache_resource
def load_model(model):
    return spacy.load(model)

# Load pre-trained models - https://spacy.io/models/
model_en = load_model('en_core_web_sm')
model_fr = load_model('fr_core_news_sm')
model_de = load_model('de_core_news_sm')
model_pl = load_model('pl_core_news_sm')
model_es = load_model('es_core_news_sm')

# Load entity labels and their colors - https://spacy.io/api/language#get_pipe
entity_labels = {
    'en_core_web_sm': model_en.get_pipe('ner').labels,
    'fr_core_news_sm': model_fr.get_pipe('ner').labels,
    'de_core_news_sm': model_de.get_pipe('ner').labels,
    'pl_core_news_sm': model_pl.get_pipe('ner').labels,
    'es_core_news_sm': model_es.get_pipe('ner').labels,
}

entity_colors = get_entity_colors()

# Set default model to session state - https://docs.streamlit.io/library/api-reference/session-state
if 'current_model' not in st.session_state:
    st.session_state.current_model = 'en_core_web_sm'
    
# Set default entities to session state - https://docs.streamlit.io/library/api-reference/session-state
if 'selected_options' not in st.session_state:
    st.session_state.selected_options = entity_labels[st.session_state.current_model]

# Sidebar title
title = '<p style="color: Indigo; font-size: 54px; font-family: Segoe UI;">NERV</p>'
st.sidebar.markdown(title, unsafe_allow_html=True)

# Sidebar description
description = '<p style="font-size: 18px">NERV short for <span style="color: Indigo; font-weight: bold;">Named Entity Recognition Visualizer</span> is a tool to visualize entities found in a input text. Entities are extracted from <span style="color: Indigo; font-weight: bold;">Wikidata</span> knowledge graph using pre-trained models with NLP pipelines.</p>'
st.sidebar.markdown(description, unsafe_allow_html=True)

# Sidebar model selection
model_options = {
  'en_core_web_sm': model_en, 
  'fr_core_news_sm': model_fr, 
  'de_core_news_sm': model_de,
  'pl_core_news_sm': model_pl,
  'es_core_news_sm': model_es,
  }
st.session_state.current_model = st.sidebar.selectbox('Select a model', model_options.keys())

# Sidebar model description
st.sidebar.title('Model description')
selected_model = model_options[st.session_state.current_model]
model_description = selected_model.meta['description']
model_version = selected_model.meta['version']
model_info = f'<p style="font-size: 16px"><b>{st.session_state.current_model}:</b> <code>{model_version}</code>{model_description}</p>'
st.sidebar.markdown(model_info, unsafe_allow_html=True)

# Named entities selection
st.sidebar.title('Named Entities')
container = st.sidebar.container()
all = st.sidebar.checkbox('Select all entities', value=True)

# Select all entities by default, else select only the ones that are already selected
if all:
  st.session_state.selected_options = container.multiselect('Select entities to display', entity_labels[st.session_state.current_model], default=entity_labels[st.session_state.current_model])
else: 
  st.session_state.selected_options = container.multiselect('Select entities to display', entity_labels[st.session_state.current_model])

# Set different colors for each entity
for label, color in entity_colors.items():
  st.sidebar.markdown(
    f"""
    <style>
        span[data-baseweb="tag"]:has(span[title={label}]) {{
            background-color: {color} !important;
        }}
    </style>
    """, unsafe_allow_html=True)
  
# Input text to analyze
input_text = st.text_area('Text to analyze', get_default_input(), height=250)
doc = process_text(input_text, st.session_state.current_model)

# Named Entities - https://spacy.io/usage/visualizers
st.header('Named Entities')
ent_html = render_entities(doc, st.session_state.selected_options)
st.markdown(ent_html, unsafe_allow_html=True)
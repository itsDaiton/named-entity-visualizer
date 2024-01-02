import streamlit as st
import spacy
from processing import process_text, render_entities, get_default_input, get_entity_colors

# Load models only when necessary - https://docs.streamlit.io/library/advanced-features/caching
@st.cache_resource
def load_model(model):
    return spacy.load(model)

# Load English pre-trained models - https://spacy.io/models/en
model_sm = load_model('en_core_web_sm')
model_md = load_model('en_core_web_md')
model_trf = load_model('en_core_web_trf')

# Load labels and their colors - https://spacy.io/api/language#get_pipe
entity_labels = model_sm.get_pipe('ner').labels
entity_colors = get_entity_colors()

# Set default model to session state - https://docs.streamlit.io/library/api-reference/session-state
if 'current_model' not in st.session_state:
    st.session_state.current_model = 'en_core_web_sm'
    
# Set default entities to session state - https://docs.streamlit.io/library/api-reference/session-state
if 'selected_options' not in st.session_state:
    st.session_state.selected_options = entity_labels

# Sidebar title
title = '<p style="color: Indigo; font-size: 54px; font-family: Segoe UI;">NERV</p>'
st.sidebar.markdown(title, unsafe_allow_html=True)

# Sidebar description
description = '<p style="font-size: 18px">NERV short for <span style="color: Indigo; font-weight: bold;">Named Entity Recognition Visualizer</span> is a tool to visualize entities found in a input text. Entities are extracted from <span style="color: Indigo; font-weight: bold;">Wikidata</span> knowledge graph using pre-trained models with NLP pipelines.</p>'
st.sidebar.markdown(description, unsafe_allow_html=True)

# Sidebar model selection
model_options = {'en_core_web_sm': model_sm, 'en_core_web_md': model_md, 'en_core_web_trf': model_trf}
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
  st.session_state.selected_options = container.multiselect('Select entities to display', entity_labels, default=entity_labels)
else: 
  st.session_state.selected_options = container.multiselect('Select entities to display', entity_labels)

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
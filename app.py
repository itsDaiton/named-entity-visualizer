import streamlit as st
import spacy
from processing import process_text, render_entities, get_default_input

# Set default model
if 'current_model' not in st.session_state:
    st.session_state.current_model = 'en_core_web_sm'

# Input text
input_text = st.text_area('Text to analyze', get_default_input(), height=250)
doc = process_text(input_text, st.session_state.current_model)

# Named Entities
st.header('Entities found on the Wikidata')
ent_html = render_entities(doc)
st.markdown(ent_html, unsafe_allow_html=True)

# Sidebar title
title = '<p style="color: Indigo; font-size: 54px; font-family: Segoe UI;">NERV</p>'
st.sidebar.markdown(title, unsafe_allow_html=True)

# Sidebar description
description = '<p style="font-size: 18px">NERV short for <span style="color: Indigo; font-weight: bold;">Named Entity Recognition Visualizer</span> is a tool to visualize entities found in a input text. Entities are extracted from <span style="color: Indigo; font-weight: bold;">Wikidata</span> knowledge graph using pre-trained models with NLP pipelines.</p>'
st.sidebar.markdown(description, unsafe_allow_html=True)

# Sidebar model selection
model_options = ['en_core_web_sm', 'en_core_web_md']
st.session_state.current_model = st.sidebar.selectbox('Select a model', model_options)

# Sidebar model description
st.sidebar.title('Model description')
model_description = spacy.load(st.session_state.current_model).meta['description']
model_version = spacy.load(st.session_state.current_model).meta['version']
model_info = f'<p style="font-size: 16px"><b>{st.session_state.current_model}:</b> <code>{model_version}</code>{model_description}</p>'
st.sidebar.markdown(model_info, unsafe_allow_html=True)

st.sidebar.title('Named Entities')
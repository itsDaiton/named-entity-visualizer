# Named Entity Visualizer

NEV short for Named Entity Visualizer is a tool to visualize entities found in unstructured text. Entities are extracted from input text using Named Entity Recognition (NER) and then linked to concepts on Wikidata knowledge graph using Named Entity Linking (NEL). This process is executed using a pre-trained model with NLP pipeline.

![image](https://github.com/itsDaiton/named-entity-visualizer/assets/72783924/f2059c9d-29dc-4e91-b544-3b4d3caba7da)

## Description
After inputting the input text, the application first performs the Named Entity Recognition (NER) process and visualizes the result according to the appropriate categories. Based on the output from the NER, the Named Entity Linking (NEL) module then takes the recognized entities and tries to link them to the corresponding concepts on the Wikidata knowledge graph. If the linking is successful, this is recorded in the resulting table.

In the application, the user can switch between 5 different models and process text in their corresponding languages. It is also possible to filter categories and edit the visualization of entities. If necessary, it is also possible to look at an aspect of the schema and see which entities are processed in the described process.

Application can serve as a simple tool for analyzing the input text. The tool could then be particularly useful for processing newspaper articles, academic texts and other larger texts. Thanks to this tool, the user will know in advance what terms and concepts are present in the text and will be able to form an opinion about what the text will be about before reading it.

## Available pre-trained pipelines
* en_core_web_sm (English)
* fr_core_news_sm (French)
* de_core_news_sm (German)
* nl_core_news_sm (Dutch)
* es_core_news_sm (Spanish)

## Built With
* Python
* SpaCy
* SpaCy fishing
* Streamlit
* matplotlib
* pandas

## Authors
* David Poslušný

import spacy
import requests
from bs4 import BeautifulSoup

# Load the pre-trained spaCy model
nlp = spacy.load('xx_ent_wiki_sm')  

# Function to extract named entities from text
def extract_named_entities(text):
    doc = nlp(text)
    named_entities = []
    for entity in doc.ents:
        named_entities.append((entity.text, entity.label_))
    return named_entities

# Function to scrape text content from a webpage
def scrape_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text(separator=" ")
    return text

# Function to extract named entities from a webpage
def extract_named_entities_from_url(url):
    text = scrape_text_from_url(url)
    named_entities = extract_named_entities(text)
    return named_entities

# Example usage
url = "https://www.bbc.com/korean/articles/cnejn22xmdyo"  
entities = extract_named_entities_from_url(url)
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")

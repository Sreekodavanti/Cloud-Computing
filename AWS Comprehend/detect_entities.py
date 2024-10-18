from flask import Flask, render_template, request
import boto3
import json
import spacy

app = Flask(__name__, template_folder='.')

# Initialize AWS Comprehend client with the specified region
REGION = 'ca-central-1'  # Specify the AWS region you want to use
comprehend_client = boto3.client('comprehend', region_name=REGION)

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Function for detecting named entities
def detect_entities(text, language_code):
    response = comprehend_client.detect_entities(Text=text, LanguageCode=language_code)
    return response

# Function for detecting key phrases
def detect_key_phrases(text, language_code):
    response = comprehend_client.detect_key_phrases(Text=text, LanguageCode=language_code)
    return response

# Function for analyzing text using spaCy
def analyze(text):
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    named_entities = [(entity.text, entity.label_) for entity in doc.ents]
    return pos_tags, named_entities

@app.route('/')
def trial():
    return render_template("trial.html")

@app.route('/analyze', methods=['POST'])
def analyze_text():
    if request.method == 'POST':
        text = request.form.get("input_text")
        lang = request.form.get("language", "en")
        
        # Perform analysis with AWS Comprehend
        entities_response = detect_entities(text, lang)
        entities = json.dumps(entities_response, sort_keys=True, indent=4)

        key_phrases_response = detect_key_phrases(text, lang)
        key_phrases = json.dumps(key_phrases_response, sort_keys=True, indent=4)

        # Perform analysis with spaCy
        pos_tags, named_entities = analyze(text)
        
        return render_template("trial.html", input_text=text, lang=lang, key_phrases=key_phrases, entities=entities, pos_tags=pos_tags, named_entities=named_entities)

if __name__ == '__main__':
    app.run(debug=True)

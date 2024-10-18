from flask import Flask, render_template, request
from comprehend import ComprehendDetect
import boto3
import os

app = Flask(__name__, template_folder='.')

# Initialize AWS Comprehend client
comprehend_client = boto3.client('comprehend', region_name='ca-central-1')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        text = request.form.get("input_text")
        lang = request.form.get("language", "en")
        comprehend = ComprehendDetect(comprehend_client)
        key_phrases = comprehend.detect_key_phrases(text, lang)
        entities = comprehend.detect_entities(text, lang)
        return render_template("index.html", input_text=text, lang=lang, key_phrases=key_phrases, entities=entities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))

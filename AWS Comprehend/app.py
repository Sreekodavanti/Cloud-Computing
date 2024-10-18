from flask import Flask, render_template, request, jsonify
import boto3

app = Flask(__name__)

region = 'ca-central-1'

# Create a boto3 client for AWS Comprehend with the specified region
comprehend = boto3.client('comprehend', region_name=region)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    # Get text data from the request
    text = request.json['text']

    # Call Amazon Comprehend to analyze sentiment
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')

    # Extract sentiment scores from the response
    sentiment_scores = {
        'positive': response['SentimentScore']['Positive'],
        'negative': response['SentimentScore']['Negative'],
        'neutral': response['SentimentScore']['Neutral'],
        'mixed': response['SentimentScore']['Mixed']
    }

    return jsonify(sentiment_scores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

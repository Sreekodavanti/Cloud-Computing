# Project Description
This project implements a web application for sentiment analysis using AWS Comprehend. The application allows users to input text and returns sentiment scores indicating whether the sentiment is "positive," "negative," or "neutral."

The application is built using Flask for the backend and HTML, CSS, and JavaScript for the frontend. Communication between the frontend and backend is handled via HTTP requests, allowing the Flask app to process user input and interact with AWS Comprehend through the Boto3 SDK.
#### Features
Input text for sentiment analysis
Display of positive, negative, and neutral sentiment scores
Dynamic user interface with real-time results
#### Project Structure
The project consists of the following key files:

index1.html: The frontend HTML file for user interaction.
app.py: The Flask application that handles backend logic and AWS Comprehend integration.

#### Steps for Implementation
Develop HTML Templates: Create the HTML frontend interface with a form for text input.
Create Flask App: Write the Flask application in app.py.
Import Required Modules: Import Flask and Boto3 in your application.
Define Routes: Set up routes for the homepage and sentiment analysis.
Run the Flask App: Ensure the Flask app runs properly in your environment.
Integrate AWS Comprehend: Install the Boto3 library to communicate with AWS Comprehend.
Implement Sentiment Analysis Logic: Extract text input and return sentiment scores.
Update the Frontend: Modify the HTML to display sentiment analysis results.
Test the Application: Verify functionality by submitting text for analysis.
Deploy the Application: Deploy the Flask app to a production server.

#### AWS Setup
Log in to your AWS account.
Create an EC2 instance in the "Central" region.
Ensure the security group allows HTTP (port 80) and SSH (port 22) access.
Set up AWS Cloud9 or your preferred development environment.
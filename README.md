# Cloud-Computing
This repository contains multiple projects demonstrating the use of AWS SageMaker for machine learning tasks. The main focus is on building, training, and deploying machine learning models using SageMaker's services like XGBoost, serverless inference, and hyperparameter optimization (HPO). Each project is designed to showcase different aspects of the SageMaker platform, ranging from fruit quality prediction to direct marketing models.

# Project Files
1. Fruit Quality Prediction Using XGBoost and AWS SageMaker.ipynb
This project predicts the quality of fruits using machine learning. The workflow covers data preprocessing, feature engineering, and training an XGBoost model using AWS SageMaker.

### The steps include:
  a. Downloading and preparing the dataset from AWS S3.
  b. Handling missing data and normalizing the data.
  c. Creating a correlation matrix for better feature selection.
  d. Training an XGBoost model using SageMaker.
  e. Evaluating model performance and saving the model.

2. HPO_hpo_xgboost_direct_marketing_sagemaker_APIs.ipynb
This notebook focuses on using SageMaker for Hyperparameter Optimization (HPO). The project utilizes direct marketing data to optimize an XGBoost model by tuning its hyperparameters through SageMaker's APIs.

### Key steps include:
Data exploration and preprocessing.

Setting up SageMaker's built-in XGBoost algorithm for training.

Defining the hyperparameter ranges and running HPO jobs.

Analyzing the results and selecting the best-performing model.

4. SageMaker_Serverless_Inference.ipynb
This project demonstrates the use of SageMaker's serverless inference to deploy machine learning models without the need to manage infrastructure.

### It covers:

Training a model with SageMaker.
Deploying the trained model using SageMaker's serverless inference.
Running inference tasks in a cost-effective manner.

# 4. README.md
This file provides an overview of the repository, describing each project, its functionality.

# 5. Requirements.txt
Lists the dependencies required for running the notebooks in this repository. Ensure you have all necessary libraries installed before running any project.

## Overview

This repository contains the implementation at AWS Academy, focused on using Amazon SageMaker for deploying machine learning models with Deployment Guardrails and Shadow Testing.

### Tasks Overview
Deployment Guardrails:

Create two models with different configurations.
Simulate successful and failed deployments.
Utilize traffic shifting modes (canary, linear).
Implement automatic rollback on failure.
Shadow Testing:

Compare performance metrics of a new model against a currently deployed model.
Validate changes to model serving stacks without end-user impact.

### Dataset and Algorithm
Dataset Used: The dataset - customer term deposit for churn prediction, used for training the models includes three subsets:
Training Dataset
Validation Dataset
Test Dataset
Algorithms: Utilized algorithms for model training include XGBoost and a selection of hyperparameters optimized through SageMaker Hyperparameter Tuning.

### Model Training
Two models were trained using the dataset, with one model outperforming the other based on evaluation metrics. The trained models are:

Model 1: DEMO-xgb-churn-pred
Model 2: DEMO-xgb-churn-pred2

### Implementation Steps

#### Traffic Shifting Simulation
Run the inference endpoint using the traffic shifting notebook.
Simulate a successful deployment and a failure leading to rollback.
Monitor metrics in CloudWatch.
#### Endpoint Configuration
Create three endpoint configurations, each associated with the trained models:
Endpoint Config 1: DEMO-EpConfig-1
Endpoint Config 2: DEMO-EpConfig-2
Endpoint Config 3: DEMO-EpConfig-3
Test the endpoints by sending the test dataset and analyzing metrics.
#### Update Endpoint
Update the endpoint configuration using the BlueGreenUpdatePolicy.
Invoke the endpoint during the update and monitor for alarm triggers.
#### Automatic Rollback
Implement AutoRollbackConfiguration in the canary deployment configuration to roll back automatically on errors.
#### Successful Deployment
Test a successful deployment by updating the endpoint with Endpoint Config 3.
Verify that no errors trigger alarms, indicating a successful rollout.
SageMaker Shadow Testing
Set up shadow testing to compare the new model against the production variant.
Configure IAM roles, endpoint names, and variants for production and shadow testing.
Invoke the shadow test and analyze the resulting metrics to determine performance.

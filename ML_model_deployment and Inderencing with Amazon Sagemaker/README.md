# Machine Learning Model Deployment and Inferencing with AWS SageMaker
### Problem
The objective of this project was to streamline the deployment of machine learning models using Amazon SageMaker, focusing on both real-time and serverless inference. The goal was to ensure scalability and cost-efficiency for model hosting and predictions while maintaining performance.

### Approach
The entire process, from model training to deployment and inferencing, was handled on Amazon SageMaker-managed servers. 

Two types of inference endpoints were implemented:
Real-Time Inference: To provide immediate predictions with low latency.
Serverless Inference: To reduce costs by utilizing AWS’s serverless architecture for on-demand predictions.

### Dataset
The dataset utilized is the breast cancer diagnosis data which is provided in the folder and uploaded to s3 bucket.

### Technical Tools and Solutions
Model Creation: Using Linear learner model, developed it using Amazon SageMaker's built-in estimators, ensuring proper hyper-parameter tuning and different learning rates to prevent overfitting.
Endpoint Configuration: Deployed two types of inference endpoints—real-time and serverless—based on use-case needs. Both endpoints were configured to optimize performance and response times.
Hosting & Inferencing: SageMaker’s infrastructure was leveraged for model hosting and management, ensuring that all training and predictions occurred outside the Jupyter notebook environment using SageMaker APIs.
Outcome
Successfully built and deployed machine learning models using SageMaker with minimal manual intervention.
Endpoints were effectively managed through the use of SageMaker APIs, ensuring seamless optimization and monitoring of both real-time and serverless predictions.
### Conclusion
This project demonstrated the importance of utilizing AWS SageMaker for scalable and cost-effective machine learning deployments. By balancing performance and resource management, the solution ensured efficient endpoint handling and compliance with best practices, such as deleting endpoints post-inference to manage costs.


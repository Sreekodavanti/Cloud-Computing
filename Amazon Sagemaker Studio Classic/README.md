## Introduction
In this assignment, I utilized a dataset named salaries.csv, which was initially uncleaned. The dataset was uploaded to an S3 bucket in MyApps. The project involved creating a domain in Amazon SageMaker and using SageMaker Studio Classic to perform data analysis through Data Wrangler.

#### Dataset
Dataset Name: salaries.csv
Source: Uploaded to S3 bucket in MyApps
Characteristics: Uncleaned dataset requiring preprocessing and analys

#### Steps Overview
Set Up Environment:

Ensure the AWS region is set to Central.
Verify that all previous instances are deleted or shut down.
Create Domain in Amazon SageMaker:

Access SageMaker Studio Classic for data analysis.
Data Import:

Import the dataset from the S3 bucket into Data Wrangler.
Data Analysis Workflow:

Data Quality and Insights Report (DI)
Data Preprocessing Steps:
Fill missing values.
Drop unnecessary columns.
Sort the dataset by userId in ascending order.
Use describe() to summarize dataset statistics.
Replace the column name "salary" with "Payment".
Save Data Flow:

After completing the analysis, save the processed data flow back to the S3 bucket.
Cleanup:

Delete the Wrangler flow files to maintain organization.
Shut down all running kernels and terminate any active terminals to minimize resource consumption.

Unfortunately due to credits issue, I could not save them but uploaded a pdf file which reports all the detailed explaination of using data wrangler tool.


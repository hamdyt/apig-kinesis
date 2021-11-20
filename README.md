API Gateway to Kinesis Data Streams Integration Pattern

This pattern provides for integration between Amazon API Gateway and Kinesis Data Streams. The pattern uses API Gateway as the front door to ingest data into Kinesis Data Streams using REST API’s, an AWS Lambda function in invoked whenever a record is put into Kinesis and stores the record into DynamoDB table. The API also fetches data from DynamoDB and return the result to the calling client.

This pattern creates an Amazon API Gateway, AWS Kinesis Data Stream, an AWS Lambda function, S3 bucket and DynamoDB table. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

Requirements
•	Create an AWS account if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
•	AWS CLI installed and configured
•	Git Installed
•	AWS Serverless Application Model (AWS SAM) installed

Reference Architecture
The following architecture diagram shows the end to end integration flow.

![image](https://user-images.githubusercontent.com/20010017/142716013-7ec5a221-4c19-40de-a3a6-218b06248781.png)


 

Deployment Instructions
1.	Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
2.	git clone https://github.com/hamdyt/apig-kinesis
3.	Change directory to apig-kinesis directory:
4.	From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
5.	sam deploy --guided
6.	During the prompts:
o   	Enter a stack name
o	    Enter the desired AWS Region
o	    Allow SAM CLI to create IAM roles with the required permissions.
Once you have run sam deploy -guided mode once and saved arguments to a configuration file (samconfig.toml), you can use sam deploy in future to use these defaults.
7.	Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

Front-end deployment
The sam deploy command creates several resources. One of the resources is an S3 bucket you will need to upload the html client to the S3 bucket (Serverless-capstone).
Please follow the instructions found here to upload the client objects
https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html

Testing
Use CloudFront to test the application by going to https://<cloudfront domain name>/index.html. You should see the following screen
	
  ![image](https://user-images.githubusercontent.com/20010017/142715925-709d3b4b-28a2-44a0-8715-def9203810ea.png)

 

This simple web app will allow for ingesting data into Kinesis Data Stream using REST API calls via the Amazon API Gateway. The client will also read data inserted into DynamoDB and display the results.
To test the integration please enter the following
1.	The Kinesis Data Stream name: SoccerPlayersStream
2.	In the Partition Key field enter any key of type string (i.e. Key001)
3.	In the Data field enter any sample data (i.e. Hello World)
4.	Click the Publish button. This will insert the data into Kinesis Data Streams
5.	In the section entitled - Get Records from Kinesis- Click on the Read button. You should see the partition key and the data text you entered along with the creation time. This data is being retrieved from DynamoDB table.

  Cleanup
	Delete the stack 
    aws cloudformation delete-stack --stack-name STACK_NAME
________________________________________


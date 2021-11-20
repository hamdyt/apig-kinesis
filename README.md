# API Gateway to Kinesis Data Streams Integration Pattern

This pattern provides for integration between Amazon API Gateway and Kinesis Data Streams. The pattern uses API Gateway as the front door to ingest data into Kinesis Data Streams using REST API’s, an AWS Lambda function in invoked whenever a record is put into Kinesis and stores the record into DynamoDB table. The API also fetches data from DynamoDB and return the result to the calling client.

This pattern creates an Amazon API Gateway, AWS Kinesis Data Stream, an AWS Lambda function, S3 bucket and DynamoDB table. 

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

# Requirements

- Create an [AWS Account](https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start). if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS  resources.
- AWS [CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) installed and configured
- Code repo [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) Installed
- AWS Serverless Application Model [AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) installed

# Reference Architecture
The following architecture diagram shows the end to end integration flow.
![image](https://user-images.githubusercontent.com/20010017/142718926-6b0647b6-78c7-47fc-8ed5-433e0cf9ff64.png)



 

# Deployment Instructions
-	Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
-	Clone the repo using `git clone` command https://github.com/hamdyt/apig-kinesis
-	Change directory to apig-kinesis directory:
-	From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
          `sam deploy --guided`
-	During the prompts:     
   	Enter a stack name        
         	  Enter the desired AWS Region
		       	   and allow SAM CLI to create IAM roles with the required permissions.
- Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use sam deploy in future to use these defaults.
-	Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

# Front-end deployment
The sam deploy command creates several resources. One of the resources is an S3 bucket you will need to upload the html client to the S3 bucket (Serverless-capstone).
Please follow the instructions found here to [upload the client objects](
https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html)


# Testing
Use CloudFront to test the application by going to `https://cloudfront domain name/index.html`. You should see the following screen
	
  ![image](https://user-images.githubusercontent.com/20010017/142715925-709d3b4b-28a2-44a0-8715-def9203810ea.png)

 

This simple web app will allow for ingesting data into Kinesis Data Stream using REST API calls via the Amazon API Gateway. The client will also read data inserted into DynamoDB and display the results.
To test the integration please enter the following
-	The Kinesis Data Stream name: SoccerPlayersStream
-	In the Partition Key field enter any key of type string (i.e. Key001)
-	In the Data field enter any sample data (i.e. Hello World)
-	Click the Publish button. This will insert the data into Kinesis Data Streams
-	In the section entitled - Get Records from Kinesis- Click on the Read button. You should see the partition key and the data text you entered along with the creation time. This data is being retrieved from DynamoDB table.

# Clean Up
Delete the stack by issuing the following command `aws cloudformation delete-stack --stack-name STACK_NAME`

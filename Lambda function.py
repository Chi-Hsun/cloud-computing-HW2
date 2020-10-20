# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime
import datetime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('HelloWorldDatabase')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    x = datetime.datetime.now()
# extract values from the event object we got from the Lambda service and store in a variable
    Year = event['year']
    Month = event['month']
    Date = event['date']
    birthday = event['year'] +' '+ event['month'] +' '+ event['date']
    if (int(Month)>x.month):
        old = x.year-int(Year)-1
    elif (int(Month)==x.month and int(Date)>x.day):
        old = x.year-int(Year)-1
    else:
        old = x.year-int(Year)
# write name and time to the DynamoDB table using the object we instantiated and save response in a variable
    response = table.put_item(
        Item={
            'ID': birthday,
            'LatestGreetingTime':now
            })
# return a properly formatted JSON object
    if (int(Month) == x.month and int(Date) == x.day):
        return {
            'statusCode': 200,
            'body': json.dumps('Happy birthday!' + ' You are '+str(old) +' years old.')
        }
    else:
        return {
            'statusCode': 200,
            'body': json.dumps('You are '+str(old) +' years old.')
            
        }

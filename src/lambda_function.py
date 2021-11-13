
import json
import base64

print('Loading function')

def lambda_handler(event, context):
                print('------------------------')
                print(event)
                #1. Iterate over each record
                
                #print("test1")
                
                try:
                                for ddbRecord in event['Records']:
                                                #2. Handle event by type
                                                
                                                record = base64.b64decode(ddbRecord["kinesis"]["data"])
                                                record = json.loads(record.decode('utf-8'))
                                                
                                                print('Decoded record: ' + record)

                                print('------------------------')
                                return "Success!"
                except Exception as e: 
                                print(e)
                                print('------------------------')
                                return "Error"
                                

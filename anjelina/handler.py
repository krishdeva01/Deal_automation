import json

def hello(event, context):
  body = {
      "message": "Go Serverless v3.0! Your function executed successfully!",
      "input": event['data'],
  }
  return {"statusCode": 200, "body":body}

def lambda_handler(event, context):
    return {
        "statusCode": 201,
        'body': 'Hello from Lambda!'
    }
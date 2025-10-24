def lambda_handler(event, context):
    # For API Gateway HTTP API queries, query string params usually under event.get('queryStringParameters')
    name = None
    # Try HTTP API v2 format
    if isinstance(event, dict):
        qs = event.get('queryStringParameters') or {}
        name = qs.get('name') if qs else None
    if not name:
        name = "Guest"
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": f"Hello, {name}! Welcome to my first cloud function."
    }

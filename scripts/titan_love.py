"""
Sends love to Amazon Titan for Embeddings 💖
and gets a bunch of numbers in return 🔢
"""

import json
import boto3

# Initialize Bedrock Runtime client
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html
bedrock = boto3.client("bedrock-runtime")

# Call Amazon Titan for Embeddings model on "love"
# https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html
response = bedrock.invoke_model(
    modelId="amazon.titan-embed-text-v1",
    body="{\"inputText\": \"love\"}"
)

# Process the model response and print the final result
body = json.loads(response.get('body').read())
print(body['embedding'])

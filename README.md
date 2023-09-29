# bedrock-worker

The BedrockWorker class provides a client for interacting with the AWS Bedrock service. 

This is a worker that handles bedrock [control plane](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Amazon_Bedrock.html) and [data plane](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Amazon_Bedrock_Runtime.html) communication.

## Getting started

1. Clone the repo.

```bash
git clone https://github.com/labeveryday/bedrock-worker.git
```

2. Create a python virtual environment

```bash
python -m venv venv
```

3. Activate your virtual environment:

```bash
source venv/bin/activate
```

4. Install the requirements

```bash
pip install -r requirements.txt

```

From there you can create a `main.py` file to use the code or enter into the interpreter and try it out for yourself. 

## How the class works

Import the class:

```python
from bedrock_worker import BedrockWorker
```

Initialize the Bedrock client:

```python 
worker = BedrockWorker(
    region_name='us-east-1',
    aws_access_key_id='AKIA...', 
    aws_secret_access_key='abc123...'
)
```
>NOTE: Region is required. Parameters like `aws_access_key_id`, `aws_secret_access_key` etc. are optional. See the boto3 client [documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html#boto3.session.Session.client) for the full list.

Print the BedrockWorker methods:

```python
# Print the control plane methods for bedrock
print(dir(worker.bedrock))

# Print the data plane methods for bedrock
print(dir(worker.bedrock_runtime))
```

List the Foundation models via the Bedrock control plane:

```python
models = worker.bedrock.list_foundation_models()

for model in models['modelSummaries']:
    print(model['modelId'])
``` 

## Example

Here is sample code using the `anthropic.claude-v2` large language foundational model to create your first prompt to Bedrock:

>NOTE: This model has to be enabled in the console. 

```python
from bedrock_worker import BedrockWorker
import json

# Initialize the BedrockWorker client
worker = BedrockWorker(region_name='us-east-1')

# Prompt to send to the model
message = """
Who is the best basketball player in the world?
"""

# Payload that includes the prompt and the model ID
prompt = {
    "modelId": "anthropic.claude-v2",
    "contentType": "application/json",
    "accept": "application/json",
    "body": json.dumps({
        "prompt": f"Human: {message}\nAssistant:",
        "max_tokens_to_sample": 300,
        "temperature": 1,
        "top_k": 250,
        "top_p": 1,
        "stop_sequences":[]
        }
        ),
    }

# Invoke the model
response = worker.bedrock_runtime.invoke_model(**prompt)

# Read the response from the model
response_body = json.loads(response.get('body').read())

# Print the response message
print(response_body['completion'])
```


## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcomed.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

### About me

My passions lie in Network Engineering, Cloud Computing, Automation, and connecting with people. I'm fortunate to weave all these elements together in my role as a Developer Advocate at AWS. On GitHub, I share my ongoing learning journey and the projects I'm building. Don't hesitate to reach out for a friendly hello or to ask any questions!

My hangouts:
- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)
- [YouTube](https://www.youtube.com/@LabEveryday)
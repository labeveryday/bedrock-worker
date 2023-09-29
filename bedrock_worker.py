import boto3
from typing import Any

BEDROCK = "bedrock"
BEDROCK_RUNTIME = "bedrock-runtime"


class BedrockWorker:
    """
    Client for interacting with AWS Bedrock service.

    Handles authentication and provides methods to call Bedrock APIs.
    """
    def __init__(self, region_name: str=None, **kwargs: Any):
        """
        Initialize the BedrockWorker client.

        Args:
        - region_name (str):                    AWS region name

        **kwargs: Additional connection parameters:
            - api_version (str):                Bedrock API version
            - use_ssl (bool):                   Use SSL for connection 
            - verify (str):                     Verify SSL certificate 
            - endpoint_url (str):               Custom endpoint URL
            - aws_access_key_id (str):          AWS access key ID
            - aws_secret_access_key (str):      AWS secret access key
            - access_token (str):               Access token 
            - config (botocore.client.Config):  Botocore config object

        Returns None
        """
        self.region_name = region_name
        self.api_version = kwargs.get("api_version", None)
        self.use_ssl = kwargs.get("use_ssl", True)
        self.verify = kwargs.get("verify", None)
        self.endpoint_url = kwargs.get("endpoint_url", None)
        self.api_version = kwargs.get("api_version", None)
        self.aws_access_key_id = kwargs.get("aws_access_key_id", None) 
        self.aws_secret_access_key = kwargs.get("aws_secret_access_key", None)
        self.access_token = kwargs.get("access_token", None)
        self.config = kwargs.get("config", None)
        self.bedrock = None
        self.bedrock_runtime = None
        self.connect()
    
    def connect(self):
        """
        Establish connections to Bedrock and Bedrock Runtime API clients.

        Uses the parameters provided at initialization to authenticate
        and create API clients. The clients are stored in the `bedrock`
        and `bedrock_runtime` instance attributes.
        """
        api_kwargs = {}
        api_kwargs["region_name"] = self.region_name
        api_kwargs["service_name"] = BEDROCK
        if self.api_version:
            api_kwargs["api_version"] = self.api_version
        if self.use_ssl:
            api_kwargs["use_ssl"] = self.use_ssl
        if self.verify:
            api_kwargs["verify"] = self.verify
        if self.endpoint_url:
            api_kwargs["endpoint_url"] = self.endpoint_url
        if self.aws_access_key_id:
            api_kwargs["aws_access_key_id"] = self.aws_access_key_id
        if self.aws_secret_access_key:
            api_kwargs["aws_secret_access_key"] = self.aws_secret_access_key
        if self.access_token:
            api_kwargs["access_token"] = self.access_token
        if self.config:
            api_kwargs["config"] = self.config

        # Create bedrock client
        self.bedrock = boto3.client(**api_kwargs)

        api_kwargs["service_name"] = BEDROCK_RUNTIME

        # Create bedrock runtime client
        self.bedrock_runtime = boto3.client(**api_kwargs)


if __name__ == '__main__':
    api = BedrockWorker(region_name="us-east-1")

    # Print the data plane methods for bedrock
    print("Control plane methods:")
    for item in dir(api.bedrock_runtime): 
        if not item.startswith("_"): 
            print(item)

    # Print the control plane methods for bedrock
    print("\n")
    print("Data plane methods:")
    for item in dir(api.bedrock): 
        if not item.startswith("_"): 
            print(item)

    print
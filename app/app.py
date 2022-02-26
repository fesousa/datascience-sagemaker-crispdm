import json
import time
import boto3
from botocore.exceptions import ClientError
import datetime
import os
import sys

def lambda_handler(event, context):
    client = boto3.client('sagemaker')
    
    try:
        # parar notebooks
        notebooks = client.list_notebook_instances(StatusEquals='InService')
        for nb in notebooks['NotebookInstances']:
            nb_name = nb['NotebookInstanceName']
            response = client.stop_notebook_instance(NotebookInstanceName=nb_name)

        # remover endpoints
        endpoints = client.list_endpoints(StatusEquals='InService')
        for ep in endpoints['Endpoints']:
            ep_name = ep['EndpointName']
            response = client.delete_endpoint(EndpointName=ep_name)
                        
    except ClientError as e:
        print(f'ERROR: {e}')
        return "Erro"
    else:
        return ("OK")
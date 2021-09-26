"""
Some description of your function.
"""

__author__ = 'Nikolay Grishchenko'
__maintainer = 'Nikolay Grishchenko'
__version__ = "1.00"

import boto3
import datetime
import json
import logging
import os
import re
import sys
import time
from collections import defaultdict

from sosw import Processor as SoswProcessor

try:
    from aws_lambda_powertools import Logger

    logger = Logger()

except ImportError:
    import logging

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)


class Processor(SoswProcessor):
    """
    The main processor of www_commit.
    """

    DEFAULT_CONFIG = {
        'init_clients': ['DynamoDb'],
        'dynamo_db_config': {
            'table_name': 'results',
            'row_mapping': {
                'user_id': 'S',
                'created_at': 'N',
            }
        }
    }


    def __call__(self, event):
        """
        Call the Processor
        """

        logger.info("Called the Processor")
        response = {
            "statusCode": 200,
            "headers": {
                'Access-Control-Allow-Origin': '*',
            },
            "body": {"hello": "world"}
        }

        return response


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Deconstructor.
        """

        pass


processor = None


def lambda_handler(event, context):
    """
    Describe what are you doing.
    """

    logger.info(f"Called {os.environ.get('AWS_LAMBDA_FUNCTION_NAME')} lambda of "
                f"version {os.environ.get('AWS_LAMBDA_FUNCTION_VERSION')} with __name__: {__name__},"
                f"event: {event}, context: {context}")

    global lambda_context
    lambda_context = context

    global processor

    if not processor:
        if os.environ.get('STAGE') in ['test', 'autotest']:
            processor = Processor(custom_config={'test': True})
        else:
            processor = Processor()

    processor.stats['total_invocations'] += 1

    result = processor(event)

    return result

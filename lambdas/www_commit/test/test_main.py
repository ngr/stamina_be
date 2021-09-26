#!/var/app/lambdas3/venv/www_commit/bin/python
__name__ = 'www_commit'

import boto3
import datetime
import logging
import shutil
import unittest
from unittest.mock import patch
import uuid
import os

from collections import defaultdict

os.environ["STAGE"] = "test"
os.environ["autotest"] = "True"
os.environ["AWS_XRAY_SDK_ENABLED"] = "false"

from lambdas.www_commit.app import Processor


logging.getLogger('botocore').setLevel(logging.WARNING)


class www_commit_TestCase(unittest.TestCase):

    def setUp(self):
        """
        setUp TestCase.
        """

        self.get_config_patcher = patch.object(Processor, 'get_config')
        self.get_config_mock = self.get_config_patcher.start()
        self.get_config_mock.return_value = {}

        CONFIG = {
            'custom': 1,
        }
        self.processor = Processor(test=True, custom_config=CONFIG)


    def tearDown(self):
        """
        """

        # We have to kill processor first of all, otherwise it keeps connection alive.
        # If not processor - no problem. :)
        try:
            del self.processor
        except:
            pass


    def test_true(self):
        """
        Sample test.
        """
        self.assertTrue(True)

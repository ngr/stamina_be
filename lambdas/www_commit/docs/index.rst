..  _www_commit:

==================
www_commit
==================

Description
-----------
This Lambda function takes care of saving results received from the Front-End application to DynamoDB.
It identifies the user decrypting and authorizing the JWT.

Interface
---------
Stands behind the API Gateway and accepting the proxied HTTP POST requests.

Authors
-------
* *Nikolay Grishchenko*



Code description of the Lambda
--------------------------------------

..  automodule:: www_commit.app
    :members:

..  autoclass:: www_commit.app.Processor
    :members:

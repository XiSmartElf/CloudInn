from flask import Flask

from boto.dynamodb2.fields import HashKey
from boto.dynamodb2.table import Table
from flask_dynamo import Dynamo

import os

app = Flask(__name__)

os.environ["AWS_ACCESS_KEY_ID"] = "AKIAIIGDRJRYMGHB2O4Q"
os.environ["AWS_SECRET_ACCESS_KEY"] = "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"

app.config['DYNAMO_ENABLE_LOCAL'] = True
app.config['DYNAMO_LOCAL_HOST'] = 'localhost'
app.config['DYNAMO_LOCAL_PORT'] = 8000

dynamo = Dynamo(app)

app.config['DYNAMO_TABLES'] = [
    Table('testPost', schema=[HashKey('postId')])
]

from Site import BlogController, PostController, DBController


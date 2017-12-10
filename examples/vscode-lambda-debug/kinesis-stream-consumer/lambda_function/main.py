import base64
from functools import reduce
import json
import os
import platform

from lambda_function.utils.operators import reducer


def decode_kinesis_payload(event):
    return map(lambda x: json.loads(base64.b64decode(x['kinesis']['data'])), event['Records'])

def handler(event, context):
    print('env={}, python={}'.format(os.environ.get('env'), platform.python_version()))
    total = reduce(reducer, map(lambda x: x['count'], decode_kinesis_payload(event)))
    print('Total count: {}'.format(total))
    return 'Success'

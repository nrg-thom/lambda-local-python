import argparse
import time
import importlib
import json
import sys
import uuid


class LambdaContext(object):
    def __init__(self, function_name, region):
        self.function_name = function_name
        self.function_version = '$LATEST'
        self.invoked_function_arn = 'arn:aws:lambda:{}:123456789012:function:{}'.format(
            region, function_name)
        self.memory_limit_in_mb = '128'
        self.aws_request_id = str(uuid.uuid4())
        self.log_group_name = '/aws/lambda/{}'.format(function_name)
        self.log_stream_name = '{}/[$LATEST]{}'.format(time.strftime(
            '%Y/%m/%d', time.gmtime()), uuid.uuid4().hex)
        self.identity = None
        self.client_context = None


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', type=str, required=True,
        help='Full path of the function, include module path and function name')
    parser.add_argument('-l', '--library', type=str, required=False, help='extra library path')
    parser.add_argument('-t', '--timeout', type=int, required=False, default=300,
        help='Lambda timeout in seconds, default 300')
    parser.add_argument('-r', '--region', type=str, required=False, default='us-west-2',
        help='Region of the lambda function')
    parser.add_argument('-e', '--event', type=str, required=False, default='{}',
        help='JSON formated event, use file version if -E is specified')
    parser.add_argument('-E', '--event_file', type=str, required=False,
        help='File path contains JSON formatted event, use file version if -E is specified')
    return parser.parse_args()


def invoke_function():
    args = parse_args()

    if '.' not in args.function:
        raise Exception(
            'Incorrect function: "{}", e.g. path.to.module.function_name'.format(args.function))

    sys.path.append('.')

    if args.library:
        sys.path.append(args.library)

    module_name, function_name = args.function.rsplit('.', 1)

    module = importlib.import_module('{}'.format(module_name))
    if args.event_file:
        event = json.load(open(args.event_file, 'r'))
    else:
        event = json.loads(args.event)

    getattr(module, function_name)(event, LambdaContext(function_name, args.region))

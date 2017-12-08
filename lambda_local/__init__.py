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
        self.invoked_function_arn = 'arn:aws:lambda:{}:123456789012:function:{}'.format(region, function_name)
        self.memory_limit_in_mb = '128'
        self.aws_request_id = str(uuid.uuid4())
        self.log_group_name = '/aws/lambda/{}'.format(function_name)
        self.log_stream_name = '{}/[$LATEST]{}'.format(time.strftime('%Y/%m/%d', time.gmtime()), uuid.uuid4().hex)
        self.identity = None
        self.client_context = None


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--function', type=str, required=True,
        help='Full path of the function, include directory, module, and function name')
    parser.add_argument('-l', '--library', type=str, required=False, help='extra library path')
    parser.add_argument('-t', '--timeout', type=int, required=False, default=300,
        help='Lambda timeout in seconds, default 300')
    parser.add_argument('-r', '--region', type=str, required=False, default='us-west-2',
        help='Region of the lambda function')
    parser.add_argument('-e', '--event', type=str, required=False, default='{}',
        help='JSON formated event, use file version if -E is specified')
    parser.add_argument('-E', '--event_file', type=str, required=False,
        help='File path contains JSON formatted event, use file version if this option is specified')
    return parser.parse_args()


def invoke_function():
    args = parse_args()

    module_path = args.function

    if '.' not in module_path:
        raise Exception('Incorrect function: "{}", please include dir/module'.format(module_path))

    if args.library:
        sys.path.append(args.library)

    if '/' in module_path:
        path, module_path = module_path.rsplit('/', 1)
        sys.path.append(path)

    module_name, function_name = module_path.rsplit('.', 1)
    module = importlib.import_module(module_name)
    if args.event_file:
        event = json.load(open(args.event_file, 'r'))
    else:
        event = json.loads(args.event)

    getattr(module, function_name)(event, LambdaContext(function_name, args.region))


if __name__ == '__main__':
    invoke_function()

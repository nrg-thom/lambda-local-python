import os

def handler(event, context):
    env = os.environ.get('ENV')
    print('env={}'.format(env))
    for i, it in enumerate(event['data']):
        print('{}: name={}, value={}'.format(i, it['name'], it['value']))
    return 'Success'

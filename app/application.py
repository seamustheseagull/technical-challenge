from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys
import argparse
import random
import os

from solver.solver import solver
from flask import Flask, request
import json
from prometheus_client import Counter, start_wsgi_server as prometheus_server



MAX_VALUE = 1000
PORT = int(os.environ.get('APP_PORT'))
MONITOR = int(os.environ.get('MONITOR_PORT'))


application = Flask(__name__)
application.config.from_object(__name__)
requests_total = Counter('requests_total', 'Total number of requests')


# The root endpoint returns the app value. Some percentage of the time
# (given by app.config['failure_rate']) calls to this endpoint will cause the
# app to crash (exits non-zero).
@application.route('/v1/')
def index():
    input_val = json.loads(request.args.get("input"))
    result = solver(input_val)
    return result

@application.route('/')
def home():
    return ('I am running')

# To help with testing this endpoint will cause the app to crash
# every time it is called
@application.route('/crash')
def crash():
    requests_total.inc()
    request.environ.get('werkzeug.server.shutdown')()
    application.config.update({'crashed': True})
    return "{}"


def main(args):
   
    print('APP PORT is  ', PORT)
    print('APP MONITOR is ', MONITOR)
    
    prometheus_server(MONITOR)

    application.config.update({
        'input': args.input,
        'failure_rate': args.failure_rate,
        'crashed': False
    })
    application.run('0.0.0.0', port=PORT)

    if application.config['crashed']:
        print('app crashed, exiting non-zero')
        sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        type=str,
        required=False,
        help='the input string'
    )
    parser.add_argument(
        '--failure-rate',
        type=float,           
        default=0,
        help='the failure rate'
    )
    return parser.parse_args()


if __name__ == '__main__':
    main(parse_args())

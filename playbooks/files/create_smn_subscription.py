#!/usr/bin/env python3

import openstack
import sys

from otcextensions import sdk

conn = openstack.connect()

sdk.register_otc_extensions(conn)

topic_urn = sys.argv[1]

attrs = {
    'endpoint': sys.argv[2],
    'protocol': 'email',
    'remark': f'apimon {sys.argv[2]}'
}

result = conn.smn.create_subscription(topic_urn, **attrs)

print(result.id)

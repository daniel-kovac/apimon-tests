#!/usr/bin/env python3

import openstack
import sys

from otcextensions import sdk

conn = openstack.connect()

sdk.register_otc_extensions(conn)

topic_urn = sys.argv[1]

for sub in conn.smn.subscriptions(topic_urn):
    print(f"{sub.id}\t{sub.protocol}\t{sub.endpoint}\t{sub.status}")

#!/usr/bin/env python3

import openstack

from otcextensions import sdk

conn = openstack.connect()

sdk.register_otc_extensions(conn)

for sub in conn.smn.subscriptions():
    print(f"{sub.id}\t{sub.protocol}\t{sub.endpoint}\t{sub.status}")

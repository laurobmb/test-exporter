#!/usr/bin/env python

import os
import requests
import time
from prometheus_client import start_http_server, Enum, Histogram

hitl_psql_health_status = Enum("hitl_psql_health_status", "PSQL connection health", states=["healthy", "unhealthy"])
hitl_psql_health_request_time = Histogram('hitl_psql_health_request_time', 'PSQL connection response time (seconds)')

def get_metrics():

    with hitl_psql_health_request_time.time():
        resp = requests.get(url=os.environ['HITL_URL'])
    
    print(resp.status_code)
            
    if not (resp.status_code == 200):
        hitl_psql_health_status.state("unhealthy")
            
if __name__ == '__main__':
    start_http_server(9000)
    while True:
        get_metrics()
        time.sleep(1)
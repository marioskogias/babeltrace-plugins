#!/usr/bin/python

from scribe_client import ScribeClient
from trace import Annotation, Trace, Endpoint

class ZipkinClient(ScribeClient):

    def create_trace(self, event):
        service = event["service_name"]
        trace_id = event["trace_id"]
        span_id = event["span_id"]
        parent_span = event["parent_span_id"]
        if parent_span == 0:
            parent_span = None
        port = event["port_no"]
        trace = Trace(service, trace_id, span_id, parent_span)
        endpoint = Endpoint("0.0.0.0",int(port), service)
        trace.set_endpoint(endpoint)

        return trace

    def create_annotation(self,event):
        pass

    def record(self, trace, annotation):
        print "Record event"

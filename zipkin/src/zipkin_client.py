#!/usr/bin/python

from scribe_client import ScribeClient

class ZipkinClient(ScribeClient):

    def create_trace(self, event):
        pass

    def create_annotation(self,event):
        pass

    def record(self, trace, annotation):
        print "Record event"

#!/usr/bin/python
# babeltrace_zipkin.py

import sys
import getopt
from babeltrace import *
from zipkin_client import ZipkinClient
HELP = "Usage: python babeltrace_zipkin.py path/to/file -s <server> -p <port>"

def main(argv):
    try:
        path = argv[0]
    except:
        raise TypeError(HELP)

    try:
      opts, args = getopt.getopt(argv[1:],"hs:p:")
    except getopt.GetoptError:
        raise TypeError(HELP)

    server = None
    port = None
    for opt, arg in opts:
        if opt == '-h':
            raise TypeError(HELP)
        elif opt == '-s':
            server = arg
        elif opt == '-p':
            port = arg

    if not server:
        server = "localhost"
    if not port:
        port = 1463

    # Open connection with scribe
    zipkin_client = ZipkinClient(port,  server)

    # Create TraceCollection and add trace:
    traces = TraceCollection()
    trace_handle = traces.add_trace(path, "ctf")
    if trace_handle is None:
        raise IOError("Error adding trace")

    for event in traces.events:
        name = event.name
        try:
            provider, kind = name.split(":")
            if provider != "zipkin":
                raise
        except:
            continue

        trace = create_trace(event)


if __name__ == "__main__":
    main(sys.argv[1:])

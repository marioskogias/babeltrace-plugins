#!/usr/bin/python
# babeltrace_zipkin.py

import sys
import getopt
from babeltrace import *

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

    for opt, arg in opts:
        if opt == '-h':
            raise TypeError(HELP)
        elif opt == '-s':
            server = arg
        elif opt == '-p':
            port = arg

    print(path, server, port)

    # Create TraceCollection and add trace:
    traces = TraceCollection()
    trace_handle = traces.add_trace(path, "ctf")
    if trace_handle is None:
        raise IOError("Error adding trace")

#[17:09:17.031519329] block_rq_issue:{ dev = 265289728, sector = 7538520, nr_sector = 8, bytes = 0, rwbs = 33, comm = "lttng-consumerd" }
    # Listing events
    print("--- Event list ---")
    for event_declaration in trace_handle.events:
        if event_declaration.name != "block_rq_issue":
            continue
        print("event : {}".format(event_declaration.name))
    print("--- Done ---")

    print traces.events
    for event in traces.events:
        if event.name != "block_rq_issue":
            continue
        for k,v in event.items():
            print "%s : %s " % (k, v)
            print "type : %s" % CTFTypeId.type_name(event._field(k).type)
        print event.keys()
        break
        print("sector : %s " %  event['sector'])

if __name__ == "__main__":
    main(sys.argv[1:])

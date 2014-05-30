#!/usr/bin/python
# babeltrace_zipkin.py

import sys
import json
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

    #iterate over events
    for event in traces.events:
        data = dict()
        data['name'] = event.name
        data['timestamp'] = event.cycles
        data['cycles'] = event.timestamp

        for k,v in event.items():
            print k
            field_type = event._field(k).type
            data[k] = format_value(field_type, v)

        json_data = json.dumps(data)
        print json_data
        break

def format_value(field_type, value):

    if field_type == 1:
        return int(value)
    elif field_type == 2:
        return float(value)
    elif field_type == 8:
        return [x for x in value]
    else:
        return str(value)

if __name__ == "__main__":
    main(sys.argv[1:])

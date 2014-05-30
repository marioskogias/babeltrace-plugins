#!/usr/bin/env python3
# babeltrace_zipkin.py

import sys
import getopt
#from babeltrace import *

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

if __name__ == "__main__":
    main(sys.argv[1:])

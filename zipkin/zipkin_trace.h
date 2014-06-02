/*
 * Zipkin lttng-ust tracepoint provider. 
 */

#undef TRACEPOINT_PROVIDER
#define TRACEPOINT_PROVIDER zipkin

#undef TRACEPOINT_INCLUDE
#define TRACEPOINT_INCLUDE "./zipkin_trace.h"

#if !defined(_ZIPKIN_H) || defined(TRACEPOINT_HEADER_MULTI_READ)
#define _ZIPKIN_H

#include <lttng/tracepoint.h> 

TRACEPOINT_EVENT(
	zipkin,
	keyval,
	TP_ARGS(char *, service,
            int, port, long, trace, 
            long, span, long, parent_span, 
            long, key, char *, val ),
	
	TP_FIELDS(
		ctf_string(service_name, service)
		ctf_integer(int, port_no, port)
		ctf_integer(long, trace_id, trace)
    	ctf_integer(long, span_id, span)
		ctf_integer(long, parent_span_id, parent_span)
        ctf_integer(long, key, key)
        ctf_string(val, val)
	) 
)
TRACEPOINT_LOGLEVEL(
	zipkin, 
	trace, 
	TRACE_WARNING)


TRACEPOINT_EVENT(
	zipkin,
	timestamp,
	TP_ARGS(char *, service,
            int, port, long, trace, 
            long, span, long, parent_span, 
            long, key, long, time ),
	
	TP_FIELDS(
		ctf_string(service_name, service)
		ctf_integer(int, port_no, port)
		ctf_integer(long, trace_id, trace)
    	ctf_integer(long, span_id, span)
		ctf_integer(long, parent_span_id, parent_span)
        ctf_integer(long, key, key)
        ctf_integer(long, time, time)
	) 
)
TRACEPOINT_LOGLEVEL(
	zipkin, 
	timestamp, 
	TRACE_WARNING)
#endif /* _ZIPKIN_H */

#include <lttng/tracepoint-event.h>

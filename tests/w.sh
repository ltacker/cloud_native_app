#!/bin/bash

# Generate http requests to check w service scalability

# $1 = url
# $2 = start id
# $3 = end id
# ex : time w.sh http://localhost:8090 1 10

for i in $(seq $2 $3)
do
	curl $1/srvw/user/$i &
done

wait
exit 0

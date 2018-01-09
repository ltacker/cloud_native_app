#!/bin/bash

# Generate http requests to check p service scalability

# $0 = url
# $1 = start id
# $2 = end id
# ex : time p.sh http://localhost:8083 1 10

for i in $(seq $1 $3)
do
	curl $0/srvp/user/$i &
done

wait
exit 0

#!/bin/bash

# Generate http requests to check i service scalability

# $1 = url
# $2 = start id
# $3 = end id
# ex : time i.sh http://localhost:8080 1 10

for i in $(seq $2 $3)
do
	curl $1/srvi/user/$i &
done

wait
exit 0

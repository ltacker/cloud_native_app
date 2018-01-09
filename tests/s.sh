#!/bin/bash

# Generate http requests to check s service scalability

# $1 = url
# $2 = start id
# $3 = end id
# ex : time s.sh http://localhost:8081 1 10

for i in $(seq $2 $3)
do
	curl $1/srvs/user/$i &
done

wait
exit 0

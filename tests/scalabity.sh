readonly THRESHOLD=1

timeout $THRESHOLD ./b.sh http://localhost:8082 1 10

if [ $? -gt 0 ]
then
  exit 1
fi

exit 0

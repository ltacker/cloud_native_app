readonly THRESHOLD=100

timeout $THRESHOLD ./tests/b.sh http://localhost:8082 1 10

if [ $? -gt 0 ]
then
  exit 1
fi

exit 0

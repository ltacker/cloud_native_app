readonly THRESHOLD=10

timeout $THRESHOLD ./tests/p.sh http://localhost 1 100


if [ $? -gt 0 ]
then
  exit 1
fi

exit 0

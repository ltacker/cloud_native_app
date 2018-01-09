readonly THRESHOLD=1

timeout $THRESHOLD ./tests/b.sh http://localhost:8082 1 100

if [ $? -gt 0 ]
then
  exit 1
fi

timeout $THRESHOLD ./tests/play.sh http://localhost:8000/index.html 1 100

if [ $? -gt 0 ]
then
  exit 1
fi

exit 0

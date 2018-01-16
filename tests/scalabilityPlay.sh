readonly THRESHOLD=10

timeout $THRESHOLD ./tests/play.sh http://localhost:8000/index.html 1 100

if [ $? -gt 0 ]
then
  exit 1
fi

exit 0

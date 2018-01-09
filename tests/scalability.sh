readonly THRESHOLD=10

timeout $THRESHOLD ./tests/b.sh http://localhost:8082 1 100

if [ $? -gt 0 ]
then
  exit 1
fi

timeout $THRESHOLD ./tests/i.sh http://localhost:8080/index.html 1 100

if [ $? -gt 0 ]
then
  exit 1
fi

timeout $THRESHOLD ./tests/p.sh http://localhost:8083/index.html 1 100

if [ $? -gt 0 ]
then
  exit 1
fi

timeout $THRESHOLD ./tests/s.sh http://localhost:8081/index.html 1 100

if [ $? -gt 0 ]
then
  exit 1
fi

timeout $THRESHOLD ./tests/w.sh http://localhost:8090/index.html 1 100

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

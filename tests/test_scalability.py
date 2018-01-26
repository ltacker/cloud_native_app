from multiprocessing import Pool
import requests
import time
import pytest

PROTOCOL = "http"
HOSTNAME = "localhost"
PORT = 80
NUMBER_OF_ID = 9
CONNECTION_TIMEOUT = 100
TEST_TIMEOUT = 10

def url_list(port, path, ids):
    for i in ids:
        yield PROTOCOL + "://" + HOSTNAME + ":" + str(port) + path + "/" + str(i)

def req(url):
    r = requests.get(url, timeout=CONNECTION_TIMEOUT)
    r.raise_for_status()
    return r

def pool_request(port, path, ids):
    p = Pool()
    return p.map(req, url_list(port, path, ids))

def pool_time(port, path):
    start = time.time()
    p = pool_request(port, path, range(1, NUMBER_OF_ID + 1))
    return time.time() - start

@pytest.mark.parametrize("port,path,timeout", [
    (80, "/srvb/user", TEST_TIMEOUT),
    (80, "/srvi/user", TEST_TIMEOUT),
    (80, "/srvp/user", TEST_TIMEOUT),
    (80, "/srvs/user", TEST_TIMEOUT),
    (8090, "/play", TEST_TIMEOUT)
])
def test_services(port, path, timeout):
    t = pool_time(port, path)
    assert t is not None
    assert t < timeout

from multiprocessing import Pool
import requests
import time
import pytest

PROTOCOL = "http"
HOSTNAME = "localhost"
PORT = 80
NUMBER_OF_ID = 9
CONNECTION_TIMEOUT = 10
TEST_TIMEOUT = 10

def url_list(service, path, ids):
    for i in ids:
        yield PROTOCOL + "://" + HOSTNAME + ":" + str(PORT) + "/srv" + service + path + "/" + str(i)

def req(url):
    r = requests.get(url, timeout=CONNECTION_TIMEOUT)
    r.raise_for_status()
    return r

def pool_request(service, path, ids):
    p = Pool()
    return p.map(req, url_list(service, path, ids))

def pool_time(service, path):
    start = time.time()
    p = pool_request(service, path, range(1, NUMBER_OF_ID + 1))
    return time.time() - start

@pytest.mark.parametrize("service,path,timeout", [
    ("b", "/user", TEST_TIMEOUT),
    ("i", "/user", TEST_TIMEOUT),
    ("p", "/user", TEST_TIMEOUT),
    ("s", "/user", TEST_TIMEOUT),
    ("w", "/play", TEST_TIMEOUT)
])
def test_services(service, path, timeout):
    t = pool_time(service, path)
    assert t is not None
    assert t < timeout

from multiprocessing import Pool
import requests
import time
import pytest

PROTOCOL = "http"
HOSTNAME = "localhost"
PORT = 80
NUMBER_OF_ID = 50
NUMBER_OF_PROCESSES = NUMBER_OF_ID
CONNECTION_TIMEOUT = 100
TEST_TIMEOUT = 10

def url_list(service, ids):
    for i in ids:
        yield PROTOCOL + "://" + HOSTNAME + ":" + str(PORT) + "/srv" + service + "/user/" + str(i)

def req(url):
    r = requests.get(url, timeout=CONNECTION_TIMEOUT)
    r.raise_for_status()
    return r

def pool_request(service, ids):
    p = Pool(processes=NUMBER_OF_PROCESSES)
    return p.map(req, url_list(service, ids))

def pool_time(service):
    start = time.time()
    p = pool_request(service, range(1, NUMBER_OF_ID + 1))
    return time.time() - start

@pytest.mark.parametrize("service,timeout", [
    ("b", TEST_TIMEOUT),
    ("i", TEST_TIMEOUT),
    ("p", TEST_TIMEOUT),
    ("s", TEST_TIMEOUT),
])
def test_services(service, timeout):
    t = pool_time(service)
    assert t is not None
    assert t < timeout

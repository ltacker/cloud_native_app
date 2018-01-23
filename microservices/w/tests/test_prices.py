# coding=utf-8

import pytest
import os

def test_list_prices():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/w/w.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert 'def listprices(path):\n' in flines

def test_response_price():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/w/w.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert '    data = {"price": price, "img": img.decode("ascii")}\n' in flines

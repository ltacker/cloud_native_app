# coding=utf-8

import pytest
import os

def test_list_prices():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/w/w.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert len([l for l in flines if '    cmd = "convert' in l]) != 0

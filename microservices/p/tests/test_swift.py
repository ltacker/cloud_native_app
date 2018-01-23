# coding=utf-8

import pytest
import os

def test_can_use_swift():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/p/p.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert len([l for l in flines if 'swiftclient.Connection' in l]) != 0

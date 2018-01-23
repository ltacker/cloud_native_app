# coding=utf-8

import pytest
import os

def test_can_use_redis():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/p/p.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert len([l for l in flines if 'redis.Redis' in l]) != 0

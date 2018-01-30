# coding=utf-8

import pytest
import os

def test_not_played_status():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/s/s.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert '        data = {"id": id, "status": "not_played"}\n' in flines

def test_check_played():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/s/s.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert '        data = {"id": id, "status": value.decode("utf-8")}\n' in flines

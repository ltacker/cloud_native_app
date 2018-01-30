# coding=utf-8

import pytest
import os

def test_root():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/b/b.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert '@app.route("/", methods=["GET"])\n' in flines

def test_shutdown():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/b/b.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert '@app.route("/shutdown", methods=["POST"])\n' in flines

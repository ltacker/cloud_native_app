# coding=utf-8

import pytest
import os

def test_mailgun_response():
    root = str(pytest.config.rootdir)
    ipath = os.path.join(root, "microservices/w2/w2.py")

    print(ipath)
    with open(ipath, 'r') as f:
        flines = f.readlines()
        assert len([l for l in flines if '        response = mailgun' in l]) != 0

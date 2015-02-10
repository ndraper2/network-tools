# -*- coding: utf-8 -*-
import os


def test_simple_string(capfd):
    os.system("python echo_client.py 'This is the message to send'")
    out, err = capfd.readouterr()
    assert out == "I heard: This is the message to send\n"


def test_unicode_string(capfd):
    msg = u"python echo_client.py 'test character ó'".encode('utf-8')
    os.system(msg)
    out, err = capfd.readouterr()
    assert out == u"I heard: test character ó\n"

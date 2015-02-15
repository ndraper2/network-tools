# -*- coding: utf-8 -*-
from echo_client import echo_client


def test_simple_string():
    response = echo_client('This is the message to send')
    assert response == "This is the message to send"


def test_same_size_as_buffer():
    response = echo_client(u'aaaaaaaabbbbbbbb'.encode('utf-8'))
    assert response.decode('utf-8') == u"aaaaaaaabbbbbbbb"


def test_unicode_string():
    response = echo_client(u'test character ó'.encode('utf-8'))
    assert response.decode('utf-8') == u"test character ó"


def test_unicode_above_255():
    response = echo_client(u'test character ɯ'.encode('utf-8'))
    assert response.decode('utf-8') == u"test character ɯ"

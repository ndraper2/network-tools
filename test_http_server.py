# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from echo_client import echo_client


def test_best_case():
    msg = "GET /path/to/file.txt HTTP/1.1"
    out = msg.encode('utf-8')
    response = echo_client(out)
    if isinstance(response, str):
        in_text = response.decode('utf-8')
    assert "200 OK" in in_text
    assert 'text/plain;' in in_text
    assert 'path/to/file.txt' in in_text


def test_method_post():
    msg = "POST /path/to/file.txt HTTP/1.1"
    out = msg.encode('utf-8')
    response = echo_client(out)
    if isinstance(response, str):
        in_text = response.decode('utf-8')
    assert '405 Method not allowed' in in_text
    assert 'Allow: GET' in in_text


def test_http10():
    msg = 'GET /path/to/file.txt HTTP/1.0'
    out = msg.encode('utf-8')
    response = echo_client(out)
    if isinstance(response, str):
        in_text = response.decode('utf-8')
    assert '505 HTTP Version Not Supported' in in_text


def test_unicode_path():
    msg = 'GET /path/to/fileɯ.png HTTP/1.1'
    out = msg.encode('utf-8')
    response = echo_client(out)
    if isinstance(response, str):
        in_text = response.decode('utf-8')
    assert '200 OK' in in_text
    assert 'image/png' in in_text
    assert 'path/to/fileɯ.png' in in_text

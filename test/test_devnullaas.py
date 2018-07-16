import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

from devnullaas import NullStream
import pytest
import unittest.mock as mock
import requests
import io


@pytest.fixture
def session_mock():
    with mock.patch('requests.Session') as Session:
        yield Session()


def test_happy_path(session_mock):
    stream = NullStream()
    written = stream.write(b'foo bar')
    assert written == 7
    assert session_mock.post.called
    assert session_mock.post.call_args[0][
        0] == 'https://devnull-as-a-service.com/dev/null'


def test_endpoint(session_mock):
    stream = NullStream(endpoint='https://example.net')
    written = stream.write(b'foo bar')
    assert session_mock.post.call_args[0][0] == 'https://example.net'

def test_string(session_mock):
    stream = NullStream()
    written = stream.write('foo bar')
    assert written == 7

def test_offline(session_mock):
    stream = NullStream(endpoint=None)
    written = stream.write(b'foo bar')
    assert written == 7
    assert not session_mock.post.called


def test_close(session_mock):
    stream = NullStream(endpoint=None)
    stream.close()
    assert stream.closed
    assert not stream.writable()
    with pytest.raises(IOError):
        stream.write(b'')


def test_writelines(session_mock):
    stream = NullStream()
    written = stream.writelines([b'foo ', b'bar'])
    assert written == 7
    written = stream.writelines(['foo ', 'bar'])
    assert written == 7


def test_iobase_unsupporteds(session_mock):
    stream = NullStream(endpoint=None)
    with pytest.raises(io.UnsupportedOperation):
        stream.read(0)
    with pytest.raises(io.UnsupportedOperation):
        stream.readline()
    with pytest.raises(io.UnsupportedOperation):
        stream.readlines()
    with pytest.raises(io.UnsupportedOperation):
        stream.readall()
    with pytest.raises(io.UnsupportedOperation):
        stream.seek(0)
    with pytest.raises(io.UnsupportedOperation):
        stream.tell()
    with pytest.raises(io.UnsupportedOperation):
        stream.fileno()


def test_iobase_supporteds(session_mock):
    stream = NullStream(endpoint=None)
    assert stream.writable()
    assert not stream.readable()
    assert not stream.seekable()
    assert not stream.isatty()
    stream.flush()

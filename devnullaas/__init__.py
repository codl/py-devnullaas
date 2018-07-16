from io import RawIOBase, UnsupportedOperation
import requests


class NullStream(RawIOBase):
    def __init__(self,
                 endpoint="https://devnull-as-a-service.com/dev/null",
                 timeout=60):
        self.__closed = False
        self.endpoint = endpoint
        self.timeout = timeout
        if endpoint is not None:
            self.session = requests.Session()
            self.session.headers = {"user-agent": "py-devnullaas v0.0.1"}

    def write(self, data):
        if self.closed:
            raise IOError('Cannot write to a closed stream')
        if self.endpoint is not None:
            try:
                self.session.post(
                    self.endpoint, data=data, timeout=self.timeout)
            except requests.ConnectionError:
                raise IOError('Device not available')
            except requests.RequestException:
                raise IOError('I/O Error')
        return len(data)

    def writelines(self, lines):
        written = 0
        for line in lines:
            written += self.write(line)
        return written

    def close(self):
        self.__closed = True

    @property
    def closed(self):
        return self.__closed

    def writable(self):
        return not self.closed

    def readable(self):
        return False

    def readline(self, size=None):
        raise UnsupportedOperation()

    def readlines(self, hint=None):
        raise UnsupportedOperation()

    def readall(self):
        raise UnsupportedOperation()

    def readinto(self, b):
        raise UnsupportedOperation()

    def fileno(self):
        raise UnsupportedOperation()

    def isatty(self):
        return False

    def flush(self):
        pass

    def seekable(self):
        return False

    def seek(self, offset, whence=None):
        raise UnsupportedOperation()

    def tell(self):
        raise UnsupportedOperation()

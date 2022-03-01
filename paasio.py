import errno
import io
import os
class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._active = False
        self._read = []
        self._wrot = []
    def __enter__(self):
        self._active = True
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        self._active - False
        return exc_val and 'suppress' in str(exc_val)
    def __iter__(self):
        return self
    def __next__(self):
        line = super().readline()
        if not line:
            raise StopIteration
        self._read.append(len(line))
        return line
    def read(self, size=-1):
        if not self._active:
            raise ValueError('I/O operation on closed file.')
        read = super().read(size)
        self._read.append(len(read))
        return read
    @property
    def read_bytes(self):
        return sum(self._read)
    @property
    def read_ops(self):
        return len(self._read)
    def write(self, b):
        if not self._active:
            raise ValueError('I/O operation on closed file.')
        wrot = super().write(b)
        self._wrot.append(wrot)
        return wrot
    @property
    def write_bytes(self):
        return sum(self._wrot)
    @property
    def write_ops(self):
        return len(self._wrot)
class MeteredSocket:
    """Implement using a delegation model."""
    def __init__(self, socket):
        self._socket = socket
        self._active = False
        self._recv = []
        self._send = []
    def __enter__(self):
        self._active = True
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._socket.__exit__(exc_type, exc_val, exc_tb)
        self._active = False
        return exc_val and 'suppress' in str(exc_val)
    def recv(self, bufsize, flags=0):
        if not self._active:
            raise OSError(os.strerror(errno.EBADF))
        buf = self._socket.recv(bufsize, flags)
        self._recv.append(len(buf))
        return buf
    @property
    def recv_bytes(self):
        return sum(self._recv)
    @property
    def recv_ops(self):
        return len(self._recv)
    def send(self, data, flags=0):
        if not self._active:
            raise OSError(os.strerror(errno.EBADF))
        sent = self._socket.send(data, flags)
        self._send.append(sent)
        return sent
    @property
    def send_bytes(self):
        return sum(self._send)
    @property
    def send_ops(self):
        return len(self._send)

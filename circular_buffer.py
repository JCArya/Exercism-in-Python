class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
 
    message: explanation of the error.
 
    """
    def __init__(self, message):
        self.message = message
class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
 
    message: explanation of the error.
 
    """
    def __init__(self, message):
        self.message = message
class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity
    def read(self):
        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        else:
            return self.buffer.pop(0)
    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException("Circular buffer is full")
    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
            self.buffer.append(data)
        else:
            self.buffer.append(data)
    def clear(self):
        self.buffer = []

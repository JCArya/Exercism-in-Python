class Clock:
    def __init__(self, hour=0, minute=0):
        self.minute = (minute + hour * 60) % 1440
    def __str__(self):
        return '%02d:%02d' % divmod(self.minute, 60)
    def __repr__(self):
        return 'Clock(%d, %d)' % divmod(self.minute, 60)
    def __eq__(self, other):
        return repr(self) == repr(other)
    def __add__(self, other):
        return Clock(minute=self.minute + other)
    def __sub__(self, other):
        return self + (-other)
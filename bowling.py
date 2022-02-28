
status_dict = {
    0: 'OPEN_FRAME',
    1: 'SPARE',
    2: 'STRIKE'
}
class BowlingGame:
    class Throw:
        FIRST_THROW = 1
        SECOND_THROW = 2
    class Frame:
        class Status:
            OPEN_FRAME = 0
            SPARE = 1
            STRIKE = 2
        def __init__(self, number):
            self.number = number
            self.score_1 = 0
            self.score_2 = 0
        def status(self):
            if self.score_1 == 10:
                return self.Status.STRIKE
            if self.score_1 + self.score_2 == 10:
                return self.Status.SPARE
            return self.Status.OPEN_FRAME
        def print(self):
            print(f'Frame: {self.number}')
            print(f'Score 1: {self.score_1}')
            print(f'Score 2: {self.score_2}')
            print(f'Status: {status_dict[self.status()]}')
            print('----------------------------------')
    def __init__(self):
        self.throw = self.Throw.FIRST_THROW
        self.frame_index = 0
        self.frames = []
        for i in range(1, 13):
            self.frames.append(self.Frame(i))
    def roll(self, pins):
        if (pins < 0) or (pins >10):
            raise ValueError("Invalid number of points")
        if (self.frame_index == 10) and (self.frames[9].status() == self.Frame.Status.OPEN_FRAME):
            raise IndexError("cannot throw bonus with an open tenth frame")
        if ( ((self.frame_index == 10) and (self.frames[9].status() == self.Frame.Status.SPARE) and (self.throw == self.Throw.SECOND_THROW)) 
            or ((self.frame_index == 11) and ((self.frames[10].status() != self.Frame.Status.STRIKE)))
            or (self.frame_index > 11) ):
            raise ValueError("invalid fill balls")
        if (self.frames[self.frame_index].score_1 + pins > 10) and (self.throw == self.Throw.SECOND_THROW) and (self.frame_index < 10):
            raise ValueError("Invalid sum of points")
        if ( (self.frame_index == 10) and (self.throw == self.Throw.SECOND_THROW) and (self.frames[self.frame_index].score_1 != 10) 
            and (self.frames[self.frame_index].score_1 + pins > 10) ):
            raise ValueError("Invalid sum of bonus points")
        if self.throw == self.Throw.FIRST_THROW:
            self.frames[self.frame_index].score_1 = pins
            if pins != 10:
                self.throw = self.Throw.SECOND_THROW
        else:
            self.frames[self.frame_index].score_2 = pins
            self.throw = self.Throw.FIRST_THROW
        if self.throw == self.Throw.FIRST_THROW:
            self.frame_index = self.frame_index + 1
    def score(self):
        if self.frame_index < 9:
            raise RuntimeError('An incomplete game cannot be scored')
        if ((self.frame_index == 10) and (self.frames[9].status() == self.Frame.Status.SPARE) and (self.throw == self.Throw.FIRST_THROW)):
            raise RuntimeError('An incomplete game cannot be scored')
        if (self.frames[9].status() == self.Frame.Status.STRIKE) and ((self.frame_index == 10)):
            raise RuntimeError('An incomplete game cannot be scored')
        if ((self.frames[9].status() == self.Frame.Status.STRIKE) 
            and (self.frames[10].status() == self.Frame.Status.STRIKE) 
            and (self.frame_index == 11)
            and (self.throw == self.Throw.FIRST_THROW)):
            raise RuntimeError('An incomplete game cannot be scored')
        score = 0
        for i, frame in enumerate(self.frames[:10]):
            score += frame.score_1 + frame.score_2
            if frame.status() == self.Frame.Status.SPARE:
                score += self.frames[i+1].score_1
            if frame.status() == self.Frame.Status.STRIKE:
                score += self.frames[i+1].score_1
                if (self.frames[i+1].score_1 == 10):
                    score += self.frames[i+2].score_1
                else:
                    score += self.frames[i+1].score_2
        return score
    def describe(self):
        print(f'Throw: {self.throw}')
        for frame in self.frames:
            if frame.score_1:
                frame.print()

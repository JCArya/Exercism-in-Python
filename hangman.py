
# Game status categories
# Change the values as you see fit
STATUS_WIN = 0
STATUS_LOSE = 1
STATUS_ONGOING = 2
class Hangman:
    def __init__(self, word):
        self.word = word
        self.mask = [0 for _ in word]
        self.remaining_guesses = 9
        self.found = []
    def guess(self, char):
        if self.remaining_guesses < 0 or self.get_status() == STATUS_WIN:
            raise ValueError("The game has already ended.")
        if char not in self.word or char in self.found:
            self.remaining_guesses -= 1
            return
        self.found.append(char)
        for i, c in enumerate(self.word):
            if c == char:
                self.mask[i] = 1
    def get_masked_word(self):
        return "".join(c if m == 1 else "_" for c, m in zip(self.word, self.mask))
    def get_status(self):
        if self.remaining_guesses <= 0 and self.get_masked_word() != self.word:
            return STATUS_LOSE
        if self.get_masked_word() == self.word:
            return STATUS_WIN
        else:
            return STATUS_ONGOING
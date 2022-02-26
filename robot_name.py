import string
import random
class Robot:
    def __init__(self):
        self.name = ""
        self.name_set = set()
        self.reset()
    def gen_name(self):
        for _ in range(2):
            self.name += random.choice(string.ascii_uppercase)
        for _ in range(3):
            self.name += random.choice(string.digits)
        if self.name in self.name_set:
            self.reset()          
        self.name_set.add(self.name)
    def reset(self):
        self.name = ""
        self.gen_name()
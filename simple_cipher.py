import random
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = dict((cc, i) for i, cc in enumerate(alpha))
def char_at(text, n):
    """Get nth char of given text.
    Automatically fixing n if n < 0 or n >= len(text)
    """
    return text[n % len(text)]
class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = "".join(random.sample(alpha, k=26))
        self.key = key
    def encode(self, text):
        res = []
        for i, cc in enumerate(text):
            shift = alpha_dict.get(char_at(self.key, i))
            res.append(char_at(alpha, alpha_dict[cc] + shift))
        return "".join(res)
    def decode(self, text):
        res = []
        for i, cc in enumerate(text):
            shift = alpha_dict.get(char_at(self.key, i))
            res.append(char_at(alpha, alpha_dict[cc] - shift))
        return "".join(res)
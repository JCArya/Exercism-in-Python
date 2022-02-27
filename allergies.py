class Allergies:
    foods = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
    def __init__(self, score):
        self.score = score
    def allergic_to(self, item):
        return True if (2**self.foods.index(item) & self.score) else False
    @property
    def lst(self):
        return [x for x in self.foods if self.allergic_to(x)]

        

          
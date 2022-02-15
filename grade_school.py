from collections import Counter
class School:
    def __init__(self):
        self.ad=[]
        self.c=[]
        
    def add_student(self, name, grade):
        if name not in [item[0] for item in self.c]:
            self.ad.append(True)
            self.c.append((name,grade))
        else:self.ad.append(False)
    def roster(self):
        return [item[0] for item in sorted(self.c,key=lambda x:(x[1],x[0]))]
    def grade(self, grade_number):
        return [item[0] for item in sorted(self.c) if item[1]==grade_number]
    def added(self):
        return self.ad 

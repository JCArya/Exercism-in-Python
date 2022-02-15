
class Garden:
    def __init__(self, diagram, students=[
            'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        # create a dictionary of students and their plants
        self.students_plants = {}
        self.students = sorted(students)
        # split the diagram into lines
        lines = diagram.split('\n')
        # each student get two plants from top row and two from bottom row
        for i in range(len(self.students)):
            self.students_plants[self.students[i]
                                 ] = lines[0][2*i:2*i+2] + lines[1][2*i:2*i+2]
    def plants(self, student):
        # return the list of plants for a student
        self.plants = {
            'V': 'Violets',
            'R': 'Radishes',
            'C': 'Clover',
            'G': 'Grass'
        }
        # translate the plants to their names
        plant_names = []
        for plant in self.students_plants[student]:
            for i in range(len(plant)):
                plant_names.append(self.plants[plant[i]])
        return plant_names
garden = Garden("VC\nRC", students=['Samantha', 'Patricia'])
print(garden.plants('Patricia'))

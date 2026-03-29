import random

class Student:
    name = None
    surname = None
    mark = None

    def set_data(self, student_name, student_surname, student_mark):
        self.name = student_name
        self.surname = student_surname
        self.mark = student_mark

    def get_data(self):
        print(self.name , self.surname + '.Mark:' + str(self.mark))


def generate_random():

    names = ['Jordan', 'Cristiano', 'Mason', 'Simon', 'Michael']
    surnames = ['Latushynskyi', 'Liutak', 'Yanukovych', 'Shevchenko', 'Antonyshyn']
    marks = [1,2,3,4,5]

    random_names = random.sample(names, 5)
    random_surnames = random.sample(surnames, 5)
    random_marks = random.sample(marks, 5)

    for i in range(5):
        student = Student()
        student.set_data(random_names[i], random_surnames[i], random_marks[i])
        student.get_data()

generate_random()
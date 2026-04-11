class Group:
    def __init__(self , group_id , group_name):
        self.group_name = group_name
        self.group_id = group_id

class Student:
    def __init__(self,student_id , name , surname , mark , group_id):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.mark = mark
        self.group_id = group_id
    def info(self):
        print(f'Student ID: {self.student_id} , Name: {self.name} , Surname: {self.surname} , Mark: {self.mark} , Group ID: {self.group_id}')

class SchoolSystem:
    def __init__(self):
        self.group_list = []
        self.student_list = []

    def add_group(self):

        number_groups = int(input('Enter number of groups you want to add to group list:\n'))
        i = 0
        while i < number_groups:
            while True:
                group_id = input('Group ID:\n').strip().lower()
                exists = False
                for group in self.group_list:
                    if group.group_id == group_id:
                        exists = True
                if exists:
                    print('Group ID already exists,try another one.')
                else:
                    break
            while True:        
                group_name = input('Group name:\n').strip().lower()
                exists = False
                for group in self.group_list:
                    if group.group_name == group_name:
                        exists = True
                if exists:
                    print('This group name exists, try  another one.')
                else:
                    break
            new_group = Group(group_id , group_name)
            self.group_list.append(new_group)
            i += 1
        return self.group_list

    def add_student(self):
        number_students = int(input('How many students you want to add to student list?(in digits):\n'))
        i = 0
        while i < number_students:
            while True:
                student_id = input('Student ID:\n').strip().lower()
                exists = False
                for student in self.student_list:
                    if student.student_id == student_id:
                        exists = True
                if exists:
                    print('This student ID already exists, try another one.')
                else:
                    break
            name = input('Student name:\n').strip().capitalize()
            surname = input('Student surname:\n').strip().capitalize()
            mark = 0
            while True:
                mark = input('Mark(1-6):\n').strip()
                if mark.isdigit():
                    mark = int(mark)
                    if 1 <= mark <= 6:
                        break
                print(f'Invalid mark , enter a number from 1 to 6.')
                
            while True:
                student_group_id = input('Group ID:\n').strip().lower()
                
                found = False
                for group in self.group_list:
                    if group.group_id == student_group_id:  
                        found = True 
                if found:                           
                    new_student = Student(student_id , name , surname , mark , student_group_id)
                    self.student_list.append(new_student)
                    i += 1
                    break
                else:
                    print('Group not found.')
        return self.student_list
    
    def get_all_students(self):
        for student in self.student_list:
            student.info()

    def get_students_by_group_id(self , group_id):
        result = []
        for student in self.student_list:
            if student.group_id == group_id:
                result.append(student)
        return result
    def get_students_by_student_id(self):
        while True:
            found = False
            student_id = input('Student ID:\n').strip().lower()
            for student in self.student_list:
                if student.student_id == student_id:
                    student.info()
                    found = True
            if found:
                break
            else:
                print('No student with such ID found , try again.')

    def get_students_by_name(self):
        while True:
            found = False
            name = input('Name:\n').strip().capitalize()
            for student in self.student_list:
                if student.name == name:
                    student.info()
                    found = True
            if found:
                break
            else:
                print('No students with such name found , try again.')

    def get_students_by_surname(self):
        while True:
            found = False
            surname = input('Surname:\n').strip().capitalize()
            for student in self.student_list:
                if student.surname == surname:
                    student.info()
                    found = True
            if found:
                break
            else:
                print('No student with such surname , try again.')
    def get_students_by_mark(self):
        while True:
            found = False
            mark = input('Mark(in digits):\n').strip()
            for student in self.student_list:
                if student.mark == mark:
                    student.info()
                    found = True
            if found:
                break
            else:
                print('No students with such mark found , try again.')
        
    
    def sort_students_by_mark(self):
        sorted_students = sorted(self.student_list , key = lambda student: student.mark , reverse = True)
        for student in sorted_students:
            student.info()

    def sort_students_by_name(self):
        sorted_students = sorted(self.student_list , key = lambda student: student.name)
        for student in sorted_students:
            student.info()

    def sort_students_by_surname(self):
        sorted_students = sorted(self.student_list , key = lambda student: student.surname)
        for student in sorted_students:
            student.info()

    def get_top_students(self):
        top_number = int(input('How many top students you want to get?:\n'))
        sorted_students = sorted(self.student_list , key = lambda student: student.mark , reverse = True)
        return sorted_students[0:top_number]
    
    def get_statistics(self):
        group_id = input('Group_ID:\n').strip().lower()
        filtered_list = self.get_students_by_group_id(group_id)
        if not filtered_list:
            return None
        total = 0
        for student in filtered_list:
            total += student.mark 
        return total / len(filtered_list)
    


    def main(self):
        print(f'Welcome to you E-SchoolSystem>')
        print(f"To have ability to operate with your classes , you have to enter groups' and students' information.")
        self.add_group()
        self.add_student()
        
        print(f'Thank you for providing information. To choose option below you have to enter digit standing next to your option and press enter.')
        print(f'To close the app write down word "done". ')
        print(f"***Show***\n1 - list of all students.\n2 - students by group ID.\n3 - students by students' ID.\n4 - students by name.\n5 - students by surname.\n6 - students by mark")
        print(f'***Sort students by***\n7 - name.\n8 - surname\n9 - mark')
        print(f'***Get***\n10 - top x studentp,where x is speciafied by you.\n11 - average mark in chosen group.')
        
        while True:
            choice = input('Your choice:\n').strip().lower()
            if choice == '1':
                self.get_all_students()
            elif choice == '2':
                group_id = input('Group ID:\n').strip().lower()
                filtered_list = self.get_students_by_group_id(group_id)
                if filtered_list:
                    for student in filtered_list:
                        student.info()
                else:
                    print(f'No students found for this group')
            elif choice == '3':
                self.get_students_by_student_id()
            elif choice == '4':
                self.get_students_by_name()
            elif choice == '5':
                self.get_students_by_surname()
            elif choice == '6':
                self.get_students_by_mark()
            elif choice == '7':
                self.sort_students_by_name()
            elif choice == '8':
                self.sort_students_by_surname()
            elif choice == '9':
                self.sort_students_by_mark()
            elif choice == '10':
                top_students = self.get_top_students()
                for student in top_students:
                    student.info()
            elif choice == '11':
                average = self.get_statistics()
                if average == None:
                    print(f'No students found in this group.')
                else:            
                    print(f'Average mark for this group : {average}')      
            elif choice == 'done':
                print('See you next time!')
                break
            else:
                print(f'There is no such option, try again')      



school_n4 = SchoolSystem()
school_n4.main()
            






    
            





                
        
    

        






         



    
        


class Student:
    def __init__(self,id,name,department) -> None:
        self.id=id
        self.name=name
        self.department=department
        self.courses=[]

    def enroll_course(self,course):
        if course not in self.courses:
            self.courses.append(course)
            print(f'Enrolled in course {course}')
        else:
            print(f'Already enrolled the courses {course}')

    def drop_coures(self,course):
        if course in self.courses:
            self.courses.remove(course)
            print(f'Dropped course {course}')
        else:
            print(f'Not enroll courses')

    def view_course(self):
        print('Enrolled course: ')
        for course in self.courses:
            print(course)



class Course:
    def __init__(self,code,name,credits,department) -> None:
        self.code=code
        self.name=name
        self.credits=credits
        self.department=department
        self.students=[]


    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
            print(f'Added Student:{student.name} to the course:{student.course}')
        else:
            print(f'Student {student.name} is already enrolled this courese {student.course}')


    def remove_student(self,student):
        if student in self.students:
            self.students.remove(student)
            print(f'Removed Student:{student.name} to the course:{student.course}')
        else:
            print(f'Student:{student.name}not enrolled this course:{student.course}')


    def view_student(self):
        print(f'Enroll student for this course {self.name}')
        for student in self.students:
            print(f'-- {student.name}')



class Department:
    def __init__(self,name) -> None:
        self.name=name
        self.courses=[]

    def add_courses(self,course):
        if course in self.courses:
            self.courses.append(course)
            print(f'Added courses: {course.name} to the department {self.name}')
        else:
            print(f'Courses {course.name} is already added to the department')


    def remove_course(self,course):
        if course in self.courses:
            self.courses.remove(course)
            print(f'Removed courses: {course.name} from the department {self.name}')
        else:
            print(f'Courese {course.name} is not added to the department')


    def view_course(self):
        print(f'Courses offered by the department are {self.name}')
        for course in self.courses:
            print(f'__ {course.name}')



#create object for student
student1=Student(101,'Rahim','Cse')
student2=Student(102,'Fahim','EcE')
student3=Student(103,'Jahdim','EEE')

#create object for courses
course1=Course('CSE101','Introduction to programming language',3,'Computer Science and Engineerin')
course2=Course('EEE101','Electrical Engineerin',3,'Electrical and Electronics Engineerin')
course3=Course('CSE104','Algorithm',3,'Computer Science and Engineerin')


# creae object for department
department1=Department('Electrical Engineerin')
department2=Department('computer Engineerin')
department3=Department('Mechanical Engineerin')
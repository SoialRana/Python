class School:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
        self.teachers={}
        #composition
        self.classrooms={}

    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom

    def add_teacher(self,subject,teacher):
        self.teachers[subject]=teacher

    def student_admission(self, student):
        className=student.classroom.name
        if className in self.classrooms:
            # TODO: set student id, at the time of adding the student
            self.classrooms[className].add_student(student)
        else:
            print(f'No classroom as named{className}')


    @staticmethod
    def calculate_grade(marks):
        if 80<=marks <=100:
            return 'A+'
        elif 70 <= marks <80:
            return 'A'
        elif 60 <= marks <70:
            return 'A-'
        elif 50 <= marks <60:
            return 'B'
        elif 40 <= marks <50:
            return 'C'
        elif 33 <= marks <40:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def grade_to_value(grade):
        grade_map={'A+':5.00, 
                   'A':4.00, 
                   'A-':3.50,
                   'B': 3.00,
                   'C':2.00,
                   'D':1.50,
                   'F':0.00}
        return grade_map[grade]


    @staticmethod
    def value_to_grade(value):
        if 4.5 <=value <=5.00:
            return 'A+'
        elif 3.5 <=value <=4.50:
            return 'A'
        elif 3.0 <=value <=3.5:
            return 'A-'
        elif 2.5 <=value <=3.0:
            return 'B'
        elif 2.0 <=value <=2.5:
            return 'C'
        elif 1.5 <=value <=2.00:
            return 'D'
        else:
            return 'F'

    def __repr__(self) -> str:
        print('------All Classrom-----')
        for key,value in self.classrooms.items():
            print(key)

        print('------Students------')
        eight=self.classrooms['eight']
        for student in eight.students:
            print(student.name)

        print('.........subjects.......')
        for subject in eight.subjects:
            print(subject.name,subject.teacher.name)

        print('---------- Student exam marks------')
        for student in eight.students: 
            for key,value in eight.students[0].marks.item():
                print(student.name,key,value,student.subject_grade[key])
            print('------Student end----')
        return ''


class ClassRoom:
    def __init__(self,name) -> None:
        self.name=name
        #composition
        self.students=[]
        self.subjects=[]

    def add_student(self,student):
        serial_id=f'{self.name}-{len(self.students)+1}'
        student.id=serial_id
        self.students.append(student)

    def add_subject(self,subject):
        self.subjects.append(subject)

    def takde_semester_final(self):
        # take ezam
        for subject in self.subjects:
            subject.exam(self.students)

        # calculate final grade
        for student in self.students:
            student.calculate_final_grade()

    def __str__(self) -> str:
        return f'{self.name}-{len(self.students)}'
    
    # TODO: sort student by grade
    def get_top_students(self):
        pass


class Subject:
    def __init__(self,name,teacher) -> None:
        self.name=name
        self.teacher=teacher
        self.max_marks=200
        self.pass_marks=30

    def exam(self,students):
        for student in students:
            mark= self.teacher.evaluate_exam()
            student.marks[self.name]=mark
            student.subject_grade[self.name]=School.calculate_grade(mark)

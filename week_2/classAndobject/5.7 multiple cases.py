class Student:
    def __init__(self,name,current_class,id):
        self.name=name
        self.id=id
        self.current_class=current_class

    def __repr__(self) -> str: # representation...amra ekta string k return kore dibo 
        # amra kivabe ei class take represent korte chay seta dekhabe 
        return f'student with tname:{self.name},class:{self.current_class}, id:{self.id}'
    

class Teacher:
    def __init__(self,name,subject,id)->None:
        self.name=name
        self.subject=subject
        self.id=id
    
    def __repr__(self) -> str: # amra ekhane teacher k dekhte chay tie ei representation ta 
        return f'Teacher:{self.name}, subjects: {self.subject}'


class school:
    def __init__(self,name) -> None:
        self.name=name
        self.teacher=[]
        self.students=[]

    def add_teacher(self,name,subject):
        id=len(self.teacher)+101 # id ta amra randomly generate kortechi 
        teacher= Teacher(name, subject,id) # teacher class theke name,subject,id niye teacher instance er moddhe add kore dibe 
        self.teacher.append(teacher)

    def enroll(self,name,fee):
        if fee>6500:
            return 'not enough fee'
        else:
            id=len(self.students)+1 # student enroll er jonno ekta id set korlam...jokhon kono student thakbe na tokhon first id hobe 1
            student= Student(name,'c',id)
            self.students.append(student)
            return f'{name} is enrolled with id:{id}, extra money {fee-6500}'

    # student er jonno representations
    def __repr__(self) -> str:
        print('Welcome to ',self.name)
        print('---our teacher---')
        for teacher1 in self.teacher:
            print(teacher1)
        print('---our students---')
        for student in self.students:
            print(student)
        return 'All done for now ' # return na dile ekta error show korbe 

        
# tithi = student('Tithi',9,2)
# forad_sir= Teacher('Forad','algorithm',234)
# print(tithi)
# print(forad_sir)

phitron=school('phitron')
phitron.enroll('alia',4355)
phitron.enroll('rahim', 7655)
phitron.enroll('karim',7000)
phitron.enroll('jony',9000)

phitron.add_teacher('Tomm','Ds')
phitron.add_teacher('rahim','Os')
phitron.add_teacher('karim','Java')

print(phitron)
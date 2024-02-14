from school import School,ClassRoom,Subject
from Persons import Students,Teacher

def main():
    school=School('Nawapara Ideal High School','Nawapara')

    eight=ClassRoom('eight')
    school.add_classroom(eight)
    nine=ClassRoom('nine')
    school.add_classroom(nine)
    ten=ClassRoom('ten')
    school.add_classroom(ten)

    abul= Students('rahim',eight)
    school.student_admission(abul)
    babul= Students('babul',eight)
    school.student_admission(babul)
    kabul= Students('kabul',eight)
    school.student_admission(kabul)

    #subjects
    physics_teacher=Teacher('Shahajahan Tapan')
    physics=Subject('physics',physics_teacher)
    eight.add_student(physics)

    chemistry_teacher=Teacher('haradon sir')
    chemistry=Subject('chemistry',chemistry_teacher)
    eight.add_student(chemistry)

    biology_teacher=Teacher('Gaxi publication')
    biology=Subject('biology',biology_teacher)
    eight.add_student(biology)

    eight.take_semester_final()

    print(school)


if __name__=='__main__':
    main()
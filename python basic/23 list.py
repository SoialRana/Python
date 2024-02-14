subjects= ["c","c++","java","python","toc"]
print(subjects)
print(subjects[0])
print(subjects[2:])
print(subjects[-1])

print("python" in subjects)
print("swift" not in subjects)

print(subjects + ["swift",34])

print(subjects*3)

print(len(subjects))
subjects.append("os")
print(subjects)

subjects.insert(3,"SAD")
print(subjects)

subjects.remove("python")
print(subjects)

subjects.sort()
print(subjects)

subjects.reverse()
print(subjects)

subject1 = [10,20,4,21]
print(subject1)
subject1.reverse()
print(subject1)
subject1.pop()
print(subject1)

pos = subject1.index(20)
print(pos)

subject2=subject1.copy()
print(subject2)

subject1.clear()
print(subject1)
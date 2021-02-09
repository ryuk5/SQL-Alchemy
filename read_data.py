from create_table import *
from sqlalchemy import or_

# 1-Get all data (by querying the student table)
students = session.query(Student)

# now to display individual records we loop through the students variable
for student in students:
    print(student.name, student.age, student.grade)

# 2-Get data in order (in this example the data will be ordered by the students name)
students = session.query(Student).order_by(Student.name)
for student in students:
    print(student.name, student.age, student.grade)

# 3-Get filtred data  (we will just get one student based on condition)
student = session.query(Student).filter(Student.name == 'Hamma').first()
print("********")
print(student.name, student.age)

# filtering the data to get more than one record (here we have multiple consitions)
students = session.query(Student).filter(or_(Student.name == 'Hamma', Student.name == 'Dali'))
# the or_() is a filter operator
print("************")
print("Multiple conditions")
for student in students:
    print(student.name, student.age, student.grade)

# 4-Count the number of results
student_count = session.query(Student).filter(or_(Student.name == 'Hamma', Student.name == 'Dali')).count()
print("The number of students that matches the multiple condition is = ", str(student_count))
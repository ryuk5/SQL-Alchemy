from create_table import *

# 1st step is to create an instance of our model
student1 = Student(name="Hamma", age=22, grade="3rd")

# sec step is to add the data we created to session we already created
# session.add(student1)


# adding multiple records

# Creating multiple objects
student2 = Student(name="Dali", age=28, grade="6TH")
student3 = Student(name="TwoHemi", age=23, grade="7TH")

# calling add all, we pass to it a list containing the objects
session.add_all([student2, student3])


# 3rd step is to commit changes
session.commit()
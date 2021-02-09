from create_table import *

# Updating data consists fo doing these 3 steps

# 1-fetching the data we wanna update or modify
student = session.query(Student).filter(Student.name == 'Hamma').first()

# 2-make the modifications
student.name = 'HammaX'

# 3-commit the changes 
session.commit()
print('New name = ', str(student.name))
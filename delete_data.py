from create_table import *

# Deleting a record consists of doing 3 steps

# 1-bring the record that we want to delete
student = session.query(Student).filter(Student.name == 'Dali').first()

# 2-delete the record
session.delete(student)

# 3-commit the changes
session.commit()
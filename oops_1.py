class Student:
  def __init__(self, fname, lname, cgpa, age):
    self.first_name = fname
    self.last_name = lname
    self.cgpa = cgpa
    self.age = age

  def printFullname(self):
    print(self.first_name, self.last_name)


obj = Student("John", "Doe", 3.8, 30)
obj.printFullname()
obj.first_name = "Jane"
obj.printFullname()
print(obj.cgpa)

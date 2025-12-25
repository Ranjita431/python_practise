student = Student("Emil")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't

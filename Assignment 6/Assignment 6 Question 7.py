class Student:
    pass

class Marks:
    pass

# Create instances of the classes
student_obj = Student()
marks_obj = Marks()

# Check if the instances are instances of the classes
print("Checking instances:")
print(f"student_obj is an instance of Student: {isinstance(student_obj, Student)}")
print(f"student_obj is an instance of Marks: {isinstance(student_obj, Marks)}")
print(f"marks_obj is an instance of Student: {isinstance(marks_obj, Student)}")
print(f"marks_obj is an instance of Marks: {isinstance(marks_obj, Marks)}")

# Check if the classes are subclasses of the object class
print("\nChecking subclasses:")
print(f"Student is a subclass of object: {issubclass(Student, object)}")
print(f"Marks is a subclass of object: {issubclass(Marks, object)}")

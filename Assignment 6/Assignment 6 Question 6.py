def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)

    if student_name is not None:
        print("Student Name:", student_name)
    
    if student_class is not None:
        print("Student Class:", student_class)

# Example usage
student_data(1234)  # Only student_id provided
print("---")
student_data(5678, "John Doe")  # student_id and student_name provided
print("---")
student_data(9876, "Jane Smith", "Grade 10")  # student_id, student_name, and student_class provided

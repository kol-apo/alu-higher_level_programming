 def get_transcript(self):
        transcript = f"Transcript for {self.names} ({self.email}):\n"
        for course_name, grade in self.grades.items():
            transcript += f"{course_name}: {grade}\n"
        transcript += f"GPA: {self.gpa:.2f}\n"
        return transcript

def add_student(students):
    email = input("Enter student's email: ")
    names = input("Enter student's name: ")
    students[email] = Student(email, names)

def add_course(courses):
    name = input("Enter course name: ")
    trimester = input("Enter trimester: ")
    credits = int(input("Enter course credits: "))
    courses[name] = Course(name, trimester, credits)

def register_student_for_course(students, courses):
    email = input("Enter student's email: ")
    course_name = input("Enter course name: ")
    if email in students and course_name in courses:
        students[email].register_course(courses[course_name])
    else:
        print("Student or course not found.")

def add_grade_to_student(students):
    email = input("Enter student's email: ")
    course_name = input("Enter course name: ")
    grade = float(input("Enter grade: "))
    if email in students and course_name in students[email].courses:
        students[email].add_grade(course_name, grade)
    else:
        print("Student or course not found.")

def rank_students(students):
    ranked_students = sorted(students.values(), key=lambda s: s.gpa, reverse=True)
    for rank, student in enumerate(ranked_students, start=1):
        print(f"{rank}. {student.names} - GPA: {student.gpa:.2f}")

def search_students_by_grade(students):
    course_name = input("Enter course name: ")
    grade = float(input("Enter grade: "))
    for student in students.values():
        if student.grades.get(course_name) == grade:
            print(f"{student.names} ({student.email}) - {course_name}: {grade}")

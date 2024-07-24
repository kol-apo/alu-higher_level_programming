#!/usr/bin/python3
class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses = {}
        self.grades = {}
        self.gpa = 0.0

    def register_course(self, course):
        self.courses[course.name] = course

    def add_grade(self, course_name, grade):
        self.grades[course_name] = grade
        self.calculate_gpa()

    def calculate_gpa(self):
        total_points = 0
        total_credits = 0
        for course_name, grade in self.grades.items():
            course = self.courses[course_name]
            total_points += grade * course.credits
            total_credits += course.credits
        if total_credits > 0:
            self.gpa = total_points / total_credits

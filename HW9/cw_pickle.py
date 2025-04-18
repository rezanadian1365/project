class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address


class Student(Person):
    def __init__(
        self,
        name,
        age,
        address,
        student_id: str,
        email: str,
    ):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.email = email

    def change_email(self, new_email: str):
        self.email = new_email

    def display_info(self):
        print(
            f"Student information: \nName: {self.name}, age: {self.age}, address: {self.address}, student id: {self.student_id}, email: {self.email}"
        )


class Teacher(Person):
    def __init__(
        self,
        name,
        age,
        address,
        teacher_id: str,
        subject: str,
    ):
        super().__init__(name, age, address)
        self.teacher_id = teacher_id
        self.subject = subject

    def change_subject(self, new_sub: str):
        self.subject = new_sub

    def display_info(self):
        print(
            f"Teacher information: \nName: {self.name}, age: {self.age}, address: {self.address}, teacher id: {self.teacher_id}, subject: {self.subject}"
        )


class Course:
    def __init__(self, name: str, teacher: Teacher):
        self.name = name
        self.students = []
        self.teacher = teacher

    def add_student(self, student: Student):
        self.students.append(student)
        print("Students name was added")

    def remove_student(self, student: Student):
        self.students.remove(student)
        print("Students name was removed")

    def set_teacher(self, teacher: Teacher):
        self.teacher = teacher
        print("Teacher is set")

    def display_info(self):
        print(
            f"Course information: \nName of the course: {self.name}, name of the teacher: {self.teacher.name}"
        )
        print("List of students:")
        for student in self.students:
            student.display_info()


s1 = Student("Firooz", 30, "Bnd", "303", "firo744@gmail.com")
s2 = Student("Reza", 38, "Bnd", "304", "reza@gmail.com")

t1 = Teacher("Mr taghvazade", 35, "Tehran", "138", "programing")
t2 = Teacher("Mr imami", 30, "Tehran", "139", "mentoring")

course1 = Course("Matktab", t1)
course1.add_student(s1)
course1.add_student(s2)


t1.change_subject("coding")

course1.set_teacher(t2)

course1.display_info()

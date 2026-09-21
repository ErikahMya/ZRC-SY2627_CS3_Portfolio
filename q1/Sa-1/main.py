class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date,
                 is_submitted=False, grade=None, submitted_files=None):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = is_submitted
        self.__grade = grade
        self.__submitted_files = submitted_files if submitted_files is not None else []

    def validate_grade(self, score: float):
        if score < 0 or score > 100:
            raise ValueError("Grade must be between 0 and 100.")
        return True

    def check_submission_status(self):
        return self.__is_submitted

    def is_duplicate(self, filename: str):
        return filename in self.__submitted_files

    def add_file(self, filename: str):
        if self.__is_submitted:
            print("[Warning] Cannot add files. Assignment already graded.")
            return

        if self.is_duplicate(filename):
            print(f"[error] File '{filename}' is already attached!")
        else:
            self.__submitted_files.append(filename)
            print(f"--> [success] {self.student_name} attached '{filename}'. Total files: {len(self.__submitted_files)}")

    def remove_file(self, filename: str):
        if self.__is_submitted:
            print("[Warning] Cannot remove files. Assignment already graded.")
            return

        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print(f"--> [success] {self.student_name} removed '{filename}'. Total files: {len(self.__submitted_files)}")
        else:
            print(f"--> [error] File '{filename}' does not exist in the submission.")

    def assign_grade(self, score: float):
        if not self.__submitted_files:
            print(f"--> [Error] cannot grade. No files submitted for {self.student_name}.")
            return

        try:
            if self.validate_grade(score):
                self.__grade = score
                self.__is_submitted = True
                print(f"--> [success] Grade {score} officially assigned to {self.student_name}")
        except ValueError as e:
            print(f"[Warning] {e}")

    def get_grade(self):
        return self.__grade

    def view_files(self):
        return self.__submitted_files

    def get_status_reprt(self):
        status = "Submitted" if self.__is_submitted else "Missing"
        grade = self.__grade if self.__grade is not None else "Not Graded"

        return (
            f"ID: {self.student_id} | "
            f"NAME: {self.student_name} | "
            f"Status: {status} ({len(self.__submitted_files)} files) | "
            f"Grade: {grade}"
        )

print("--- INITIALIZING DROPBOX FOR ASSIGNMENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-10-01")
student3 = AssignmentSubmission(student_name="Juan dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py") # Should trigger private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing File After Being Graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")  # Blocked by Grading status
print()

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) # Should fail because list is empty

print("--- FINAL STATUS REPORTS ---")
print(student1.get_status_reprt())
print(student2.get_status_reprt())
print(student3.get_status_reprt())      
print(student4.get_status_reprt())
print(student5.get_status_reprt())
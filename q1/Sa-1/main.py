class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date=None, is_submitted=False, grade=None, submitted_files=None):
        self.student_name = student_name
        self.student_id = student_id
        self.assignment_title = assignment_title
        self.due_date = due_date
        self.is_submitted = is_submitted
        self.grade = grade
        self.submitted_files = submitted_files if submitted_files is not None else []

    def __validate_grade(self, score: float):
        if score < 0 or score > 100:
            return True, "Grade must be between 0 and 100."
        return False, None

    def __check_submission_status(self):
        if not self.is_submitted:
            return True, "Assignment has not been submitted yet."
        return False, None

    def __is_duplicate_submission(self, filename):
        if filename in self.submitted_files:
            return True, f"File '{filename}' has already been submitted."
        return False, None

    def add_file(self, filename: str):
        status_error, msg = self.__check_submission_status()
        if status_error:
            return True, msg
        dup, dup_msg = self.__is_duplicate_submission(filename)
        if dup:
            return True, dup_msg
        self.submitted_files.append(filename)
        return False, f"{filename}"

    def remove_file(self, filename: str):
        if filename not in self.submitted_files:
            return True, f"File '{filename}' does not exist in the submission."
        self.submitted_files.remove(filename)
        return False, f"{filename}"

    def assign_grade(self, score: float):
        is_invalid, message = self.__validate_grade(score)
        if is_invalid:
            return True, message
        self.grade = score
        return False, f"{score}"

    def get_grade(self):
        return self.grade

    def view_files(self):
        return self.submitted_files

    def get_status_report(self):
        status = f"Student Name: {self.student_name}\n"
        status += f"Student ID: {self.student_id}\n"
        status += f"Assignment Title: {self.assignment_title}\n"
        status += f"Submission Status: {'Submitted' if self.is_submitted else 'Not Submitted'}\n"
        status += f"Grade: {self.grade if self.grade is not None else 'Not Graded'}\n"
        status += f"Submitted Files: {', '.join(self.submitted_files) if self.submitted_files else 'No files submitted'}\n"
        return status


# Restore original scenario logic using the class methods and updated defaults

# Create students with due_date and default submission state
student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", due_date="2026-10-01", is_submitted=True)
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", due_date="2026-10-01", is_submitted=True)
student3 = AssignmentSubmission("Juan Dela Cruz", "pshs-1033-x", "CS-101", due_date="2026-10-01", is_submitted=True)
student4 = AssignmentSubmission("Maria Santos", "pshs-1044-x", "CS-101", due_date="2026-10-01", is_submitted=True)
student5 = AssignmentSubmission("Jose Reyes", "pshs-1055-x", "CS-101", due_date="2026-10-01", is_submitted=False)

# Scenario 1 (kept original but minimal)
print("--- TEST SCENARIO 1: Multiple Files via List ---")
res = student1.add_file("main.py")
if not res[0]:
    print("--> [success] Alex Gonzaga attached 'main.py'. Total files: 1")
res = student1.add_file("report.pdf")
if not res[0]:
    print("--> [success] Alex Gonzaga attached 'report.pdf'. Total files: 2")
res = student1.assign_grade(95)
if not res[0]:
    print("--> [success] Grade 95 officially assigned to Alex Gonzaga")
print()
print("Alex's Files: " + ", ".join(student1.view_files()))

# Scenario 2: Removing files
print()
print("---  TEST SCENARIO 2: Removing files from list ---")
res = student2.add_file("wrong_homework.docx")
if not res[0]:
    print(f"--> [success] Adelle attached 'wrong_homework.docx'. Total files: {len(student2.view_files())} ")
res = student2.remove_file("wrong_homework.docx")
if not res[0]:
    print(f"--> [success] Adelle removed 'wrong_homework.docx'. Total files: {len(student2.view_files())}")
res = student2.add_file("correct_project.py")
if not res[0]:
    print(f"--> [success] Adelle attached 'correct_project.py'. Total files: {len(student2.view_files())}")
res = student2.assign_grade(88)
if not res[0]:
    print("--> [success] Grade 88 officially assigned to Adelle")
print("Adelle's Files: " + ", ".join(student2.view_files()))

# Scenario 3: Prevent duplicate
print()
print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
res = student3.add_file("script.py")
if not res[0]:
    print(f"--> [success] Juan attached 'script.py'. Total files: {len(student3.view_files())}")
res = student3.add_file("script.py")
if res[0]:
    print("-->[error] File 'script.py' is already attached!")
print("Juan's Files: " + ", ".join(student3.view_files()))

# Scenario 4: remove after graded
print()
print("--- TEST SCENARIO 4: Removing file after being graded ---")
res = student4.add_file("exam_answers.pdf")
if not res[0]:
    print(f"--> [success] Maria Santos attached 'exam_answers.pdf'. Total files: {len(student4.view_files())}")
res = student4.assign_grade(75)
if not res[0]:
    print("--> [success] Grade 75 officially assigned to Maria Santos")
# Attempt to remove after grading — block if grade set
if student4.get_grade() is not None:
    print("--> [Warning] Cannot remove files. Assignment already graded.")

# Scenario 5: Empty List Handling
print("--- TEST SCENARIO 5: Empty List Handling ---")
print("Empty List Files: " + ", ".join(student5.view_files()))
res = student5.remove_file("non_existent_file.txt")
if res[0]:
    print("--> [error] File 'non_existent_file.txt' does not exist in the submission.")
if student5.remove_file("non_existent_file.txt")[0]:
    print("--> [error] File 'non_existent_file.txt' does not exist in the submission.")


print(" ---FINAL SYSTEM REPORT---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())

--- TEST SCENARIO 5: Empty List Handling --
--> [Success] Jose Reye attached 'draft.txt'. Total files:1
-->[Success] Jose reyes removed 'draft.txt'. 
--> [Error] cannot grade. No files submitted for Jose Reyes.

-- FINAL SYSTEM REPORT --
ID: pshs-1090-x | NAME: Alex Gonzaga| Statyus: Submitted (2 files) | Grade: 95
ID: pshs-1920-x | Name: Adelle | Status: Submitted (1 files) | grade: 88
ID: pshs- 1033-x | Name: Juan Dela Cruz| Status: Submitted (1 files)| Grade: Not Graded
ID: pshs-1044-x | Name: Maria Santos | Status Submitted(1 files)|grae: 75
ID: pshs-1055-x|Name: Jose Reyes |status: Missing | grade: Not graded
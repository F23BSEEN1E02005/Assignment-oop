class Teacher:
    def _init_(self, teacher_id, name, subjects, contact_info):
        self.teacher_id = teacher_id
        self.name = name
        self.subjects = subjects
        self.contact_info = contact_info

    def _str_(self):
        return f"{self.name}, ID: {self.teacher_id}, Subjects: {', '.join(self.subjects)}, Contact: {self.contact_info}"

class UserManagement:
    def _init_(self):
        self.teachers = {}

    def add_teacher(self, teacher_id, name, subjects, contact_info):
        """Add a new teacher to the system."""
        if teacher_id not in self.teachers:
            new_teacher = Teacher(teacher_id, name, subjects, contact_info)
            self.teachers[teacher_id] = new_teacher
            print(f"Teacher {name} has been added with ID {teacher_id}.")
        else:
            print(f"Teacher with ID {teacher_id} already exists.")

    def remove_teacher(self, teacher_id):
        """Remove a teacher from the system."""
        if teacher_id in self.teachers:
            del self.teachers[teacher_id]
            print(f"Teacher with ID {teacher_id} has been removed.")
        else:
            print(f"Teacher with ID {teacher_id} not found.")

    def display_teachers(self):
        """Display all teachers."""
        print("List of Teachers:")
        for teacher in self.teachers.values():
            print(teacher)

# Example usage:
user_mgmt = UserManagement()
user_mgmt.add_teacher('T001', 'Alice', ['Math', 'Physics'], 'alice@example.com')
user_mgmt.add_teacher('T002', 'Bob', ['History', 'Literature'], 'bob@example.com')
user_mgmt.display_teachers()
user_mgmt.remove_teacher('T001')
user_mgmt.display_teachers()
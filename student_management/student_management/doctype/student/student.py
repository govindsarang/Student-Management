# Copyright (c) 2026, Govind and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):

    def validate(self):

        total = len(self.attendance)

        if total == 0:
            self.attendance_percentage = 0
            return

        present_count = 0

        for row in self.attendance:
            if row.status == "Present":
                present_count += 1

        self.attendance_percentage = (present_count / total) * 100


@frappe.whitelist()
def get_student_summary(student_name):

    student = frappe.get_doc("Student", student_name)

    return {
        "student_name": student.student_name,
        "course": student.course,
        "attendance_percentage": student.attendance_percentage
    }


@frappe.whitelist()
def get_all_students():

    students = frappe.get_all(
        "Student",
        fields=["name", "student_name", "course", "attendance_percentage"]
    )

    return students

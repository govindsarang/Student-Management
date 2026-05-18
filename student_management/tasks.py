import frappe


def check_fee_status():

    students = frappe.get_all(
        "Student",
        fields=["name", "student_name", "fee_status"]
    )

    print("\n")
    print("RUNNING SCHEDULED TASK")
    print("\n")

    for student in students:

        print(
            student.student_name,
            "-",
            student.fee_status
        )

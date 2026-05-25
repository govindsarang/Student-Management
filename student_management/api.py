import frappe
import requests
def student_created(doc, method):

    print("\n\n")
    print("NEW STUDENT CREATED")
    print("Student Name:", doc.student_name)
    print("\n\n")


@frappe.whitelist()
def pay_fees(student_name, amount):

    amount = int(amount)

    # CREATE FEE RECORD

    fee = frappe.get_doc({
        "doctype": "Fee Record",
        "student": student_name,
        "amount": amount,
        "payment_status": "Paid"
    })

    fee.insert(ignore_permissions=True)

    # FETCH STUDENT OBJECT

    student = frappe.get_doc("Student", student_name)

    # UPDATE FEES PAID

    current_paid = student.fees_paid or 0

    student.fees_paid = current_paid + amount

    # CALCULATE STATUS

    total_fees = student.total_fees or 0

    if student.fees_paid == 0:
        student.fee_status = "Pending"

    elif student.fees_paid < total_fees:
        student.fee_status = "Partial"

    else:
        student.fee_status = "Paid"

    # SAVE STUDENT

    student.save(ignore_permissions=True)

    frappe.db.commit()

    return {
        "message": "Fees Paid Successfully",
        "fees_paid": student.fees_paid,
        "fee_status": student.fee_status
    }
#creating a student api 
@frappe.whitelist()
def create_student(student_name, age, total_fees=0):

    student = frappe.get_doc({
        "doctype": "Student",
        "student_name": student_name,
        "age": int(age),
        "total_fees": float(total_fees)
    })

    student.insert(ignore_permissions=True)

    frappe.db.commit()

    return {
        "message": "Student Created Successfully",
        "student_id": student.name
    }
#fetching student details ,create api for fetching the same 
@frappe.whitelist(allow_guest=True)
def get_student(student_name):

    student = frappe.get_doc("Student", student_name)

    return {
        "student_name": student.student_name,
        "age": student.age,
        "course": student.course,
        "total_fees": student.total_fees,
        "fees_paid": student.fees_paid,
        "fee_status": student.fee_status
    }
#updating student fees
@frappe.whitelist()
def update_student_fees(student_name, new_total_fees):

    student = frappe.get_doc("Student", student_name)

    student.total_fees = float(new_total_fees)

    student.save(ignore_permissions=True)

    frappe.db.commit()

    return {
        "message": "Fees Updated Successfully",
        "updated_total_fees": student.total_fees
    }
@frappe.whitelist(allow_guest=True)
def create_student_post():

    data = frappe.request.json

    student = frappe.get_doc({
        "doctype": "Student",
        "student_name": data.get("student_name"),
        "age": int(data.get("age")),
        "total_fees": float(data.get("total_fees", 0))
    })

    student.insert(ignore_permissions=True)

    frappe.db.commit()

    return {
        "message": "Student Created",
        "student_id": student.name
    }
import frappe
import requests

@frappe.whitelist()
def sync_employee(employee_name):

    try:
        employee = frappe.get_doc("Employee", employee_name)

        payload = {
            "employee_name": employee.employee_name,
            "department": employee.department,
            "company": employee.company
        }

        response = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=payload
        )

        return {
            "success": True,
            "status_code": response.status_code,
            "response": response.json()
        }

    except Exception as e:

        frappe.log_error(frappe.get_traceback(), "Employee Sync Error")

        return {
            "success": False,
            "error": str(e)
        }
def auto_sync_employee(doc, method):

    payload = {
        "employee_name": doc.employee_name,
        "department": doc.department,
        "company": doc.company
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=payload
    )

    frappe.log_error(
        title="Auto Sync Response",
        message=str(response.json())
    )
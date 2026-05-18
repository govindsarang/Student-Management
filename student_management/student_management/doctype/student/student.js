// Copyright (c) 2026, Govind and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Student", {

    refresh(frm) {

        frm.add_custom_button("Show Student Summary", function() {

            frappe.call({

                method: "student_management.student_management.doctype.student.student.get_student_summary",

                args: {
                    student_name: frm.doc.name
                },

                callback: function(r) {

                    frappe.msgprint(
                        "Course: " + r.message.course +
                        "<br>" +
                        "Attendance: " + r.message.attendance_percentage
                    );

                }

            });

        });

        frm.add_custom_button("Pay Fees", function() {

            frappe.call({

                method: "student_management.api.pay_fees",

                args: {
                    student_name: frm.doc.name,
                    amount: 5000
                },

                callback: function(r) {

                    frappe.msgprint(r.message.message);

                }

            });

        });

    }

});
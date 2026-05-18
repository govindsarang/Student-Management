# Copyright (c) 2026, Govind and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class FeeRecord(Document):

    def validate(self):

        if self.amount and self.amount < 0:
            frappe.throw("Fee amount cannot be negative")

        if not self.payment_status:
            self.payment_status = "Pending"
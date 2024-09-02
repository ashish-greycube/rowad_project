# Copyright (c) 2024, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import get_link_to_form
from frappe.model.document import Document


class PriceDeterminationFormRM(Document):
	def validate(self):
		if self.competition_status == "Won":
			project_doc = frappe.new_doc("Project")
			project_doc.project_name = self.rm_project_name
			project_doc.save(ignore_permissions = True)
			frappe.msgprint(_("Project is created {0}".format(get_link_to_form("Project",project_doc.name))),alert=True)

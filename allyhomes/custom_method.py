from __future__ import unicode_literals
import frappe, json
import frappe.desk.form.meta
import frappe.desk.form.load

from frappe import _

@frappe.whitelist()
def add_interaction(doc):
	"""allow any logged user to post a comment"""
	doc = frappe.get_doc(json.loads(doc))

	if doc.doctype != "Interaction Master":
		frappe.throw(_("This method can only be used to create a Interaction Master"), frappe.PermissionError)

	doc.insert(ignore_permissions = True)

	return doc.as_dict()

@frappe.whitelist()
def create_todo(owner, assigned_by, description, date,reference_name,reference_type):
	"""allow any logged user to post toDo via interaction master"""
	todo = frappe.new_doc("ToDo")
	todo.owner = owner
	todo.assigned_by = assigned_by
	todo.description = description
	todo.date = date
	todo.reference_type = reference_type
	todo.reference_name = reference_name
	todo.insert(ignore_permissions=True)



@frappe.whitelist()
def create_project(self, method):

	project = frappe.new_doc("Project")
	
	project.project_name = self.customer + " - "+ self.name
	project.owner = self.owner
	project.expected_start_date = self.transaction_date
	project.expected_end_date = self.delivery_date 
	project.customer = self.customer
	project.sales_order = self.name
	
	soitem = []

	# frappe.msgprint(frappe.__islocal)
	for value in self.get("items"):
			
			task = frappe.new_doc("Task")
			task.subject = value.item_code
			
			frappe.msgprint(value.item_code)
	project.insert(ignore_permissions=True)
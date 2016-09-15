# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint

def get_context(context):
#	return { "doc": frappe.get_doc("About Us Settings", "About Us Settings") }
	
	
#		kdemail = frappe.db.get_value("Events",{"first_name":kd_name},"email")	
#		kd_warehouse = frappe.db.get_value("Warehouse",{"owner":kdemail},"name")
	context.so_list = frappe.db.sql(""" select name,customer,rounded_total as Total,delivery_date from `tabSales Order` order by delivery_date asc""",as_dict=1)
	context.subs = frappe.db.sql(""" select name from `tabSupplier` """,as_dict=1)
	
	
		
@frappe.whitelist(allow_guest=False)  # By Rakhi
def get_events(start,end):	
#	kdemail = frappe.db.get_value("Events",{"first_name":kd_name},"email")	
#	kd_warehouse = frappe.db.get_value("Warehouse",{"owner":kdemail},"name")
	event_list = frappe.db.sql("""select description as title, starts_on as start from `tabEvent` where starts_on=%s and ends_on=%s""",format(start,end),as_dict=1)
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print start
	print end
	frappe.msgprint(_(start))
	return event_list



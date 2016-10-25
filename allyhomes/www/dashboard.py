# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint

def get_context(context):
	context.no_cache = True
#	context.sub = frappe.db.sql("""select name, status as date from `tabSupplier` """,as_dict=1)
	context.so_list = frappe.db.sql(""" select name,customer,rounded_total as Total,delivery_date from `tabSales Order` order by delivery_date asc""",as_dict=1)
	context.sub = frappe.db.sql("""select s.name as name,t.exp_end_date as date from `tabSupplier` s left join `tabTask` t on s.name=t.supplier and t.status !='Closed' order by exp_end_date asc""",as_dict=1)
	
	print context.sub
	
	
@frappe.whitelist(allow_guest=False)
def get_events(start,end):	
	no_cache = True
	event_list = frappe.db.sql("""select description as title, starts_on as start from `tabEvent` where starts_on=%s and ends_on=%s""",format(start,end),as_dict=1)
	return event_list



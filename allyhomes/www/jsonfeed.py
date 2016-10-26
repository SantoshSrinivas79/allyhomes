# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe

from frappe import msgprint, _
from frappe.utils import getdate, cint, add_months, date_diff, add_days, nowdate, get_datetime_str, cstr
from frappe.model.document import Document
from frappe.utils.user import get_enabled_system_users
import json



@frappe.whitelist()
def get_events(start, end, filters=None):
	'''data = {
	   'title' : 'ammmittthhhhhhhhaaaaaaa',
	   'start' : '2016-09-11'
	}'''
	
	condition = ''
#	values = {
#		"start_date": get_datetime_str(start),
#		"end_date": get_datetime_str(end)
#	} 

	#frappe.throw(_(get_datetime_str(end)))
	'''data = frappe.db.sql("""select hlist.name, h.holiday_date, h.description
		from `tabHoliday List` hlist, tabHoliday h
		where h.parent = hlist.name
		and h.holiday_date is not null
		{condition}""".format(condition=condition),
		as_dict=True, update={"allDay": 1})'''
	
	data = frappe.db.sql("""select ev.name, ev.starts_on as start, ev.description as title
		from `tabEvent` ev
		where ev.starts_on is not null 
		{condition}""".format(condition=condition),
		as_dict=True, update={"allDay": 1})
		
	#event_list = frappe.db.sql("""select description as title, starts_on as start from `tabEvent` where starts_on=%s and ends_on=%s""",format(start,end),as_dict=1)
	#json_str = json.dumps(data)
	#data = json.loads(json_str)
	return data

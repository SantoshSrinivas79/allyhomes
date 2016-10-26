#from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Sales Pipeline"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Lead",
					"description": _("Database of potential customers."),
				},
				{
					"type": "doctype",
					"name": "Opportunity",
					"description": _("Potential opportunities for selling."),
				},
				{
					"type": "doctype",
					"name": "Quotation",
					"description": _("Quotes to Leads or Customers."),
				},
				{
					"type": "doctype",
					"name": "Sales Order",
					"description": _("Confirmed orders from Customers."),
				},
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database."),
				},
				{
					"type": "doctype",
					"name": "Contact",
					"description": _("All Contacts."),
				},
			]
		},
		{
			"label": _("Billing"),
			"items": [
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"description": _("Bills raised to Customers.")
				},
				{
					"type": "doctype",
					"name": "Purchase Invoice",
					"description": _("Bills raised by Suppliers.")
				},
			]
		},
		{
			"label": _("Supplier / Subcontractor"),
			"items": [
				{
					"type": "doctype",
					"name": "Supplier",
					"description": _("Supplier database."),
				},
				{
					"type": "doctype",
					"name": "Supplier Type",
					"description": _("Supplier Type master.")
				},
				{
					"type": "doctype",
					"name": "Contact",
					"description": _("All Contacts."),
				},
				{
					"type": "doctype",
					"name": "Address",
					"description": _("All Addresses."),
				},

			]
		},
		{
			"label": _("Products or Services"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"description": _("All Products or Services."),
				},
			]
		},
		{
			"label": _("Projects"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Project",
					"description": _("Project master."),
				},
				{
					"type": "doctype",
					"name": "Task",
					"description": _("Project activity / task."),
				},
				{
					"type": "report",
					"route": "Gantt/Task",
					"doctype": "Task",
					"name": "Gantt Chart",
					"description": _("Gantt chart of all tasks.")
				},
			]
		},
		{
			"label": _("Expense Claims"),
			"items": [
				{
					"type": "doctype",
					"name": "Expense Claim",
					"description": _("Claims for company expense."),
				},
				{
					"type": "doctype",
					"name": "Expense Claim Type",
					"description": _("Types of Expense Claim.")
				},
			]
		},
		{
			"label": _("Setup"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Campaign",
					"description": _("Sales campaigns."),
				},
				{
					"type": "doctype",
					"name": "Completion Certificates",
					"description": _("Completion Certificate."),
				},
			]
		}		
	]

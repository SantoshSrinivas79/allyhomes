# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "allyhomes"
app_title = "Allyhomes"
app_publisher = "ECIT"
app_description = "Services of Allyhomes"
app_icon = "icon-adn"
app_color = "red"
app_email = "info@ergonomicscit.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/allyhomes/css/allyhomes.css"
# app_include_js = "/assets/allyhomes/js/allyhomes.js"

# include js, css files in header of web template
#web_include_css = [
#	"/assets/allyhomes/css/fullcalendar.css",
#	"/assets/allyhomes/css/fullcalendar.print.css"
#]
#web_include_js = [
#	"/assets/allyhomes/js/fullcalendar.min.js",
#	"/assets/allyhomes/js/jquery.min.js",
#	"/assets/allyhomes/js/moment.min.js"
#]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "allyhomes.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "allyhomes.install.before_install"
# after_install = "allyhomes.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "allyhomes.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	"Sales Order": {
		"on_submit": "allyhomes.custom_method.create_project"
				
	}
}
#doc_events = {
#	"Sales Order": {
#		"validate": "erpnext.selling.doctype.sales_order.sales_order.make_amount_constant",
#		"on_submit": "erpnext.selling.doctype.sales_order.sales_order.make_amount_constant"
#		"on_cancel": "erpnext.stock.doctype.material_request.material_request.update_completed_and_requested_qty"
#	}
#}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"allyhomes.tasks.all"
# 	],
# 	"daily": [
# 		"allyhomes.tasks.daily"
# 	],
# 	"hourly": [
# 		"allyhomes.tasks.hourly"
# 	],
# 	"weekly": [
# 		"allyhomes.tasks.weekly"
# 	]
# 	"monthly": [
# 		"allyhomes.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "allyhomes.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "allyhomes.event.get_events"
# }


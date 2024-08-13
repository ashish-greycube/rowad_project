# Copyright (c) 2024, GreyCube Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import msgprint, _

def execute(filters=None):
	columns, data = [], []

	columns = get_columns(filters)
	data = get_data(filters)

	if not data:
		msgprint(_("No records found"))
		return columns, data
	
	return columns, data

def get_columns(filters):
	columns = [
		{
			"fieldname": "project_name",
			"fieldtype": "Link",
			"label": _("Project Name"),
			"options": "Price Determination Form RM",
			# "hidden":1,
			"width": 150
		},
		{
			"fieldname": "activity",
			"fieldtype": "Select",
			"label": _("Activity"),
			"options": "\nRoad\nAir\nRail\nShip",
			"width": 200,
		},
		{
			"fieldname": "client_name",
			"fieldtype": "Data",
			"label": _("Client Name"),
			"width": 200,
		},
		{
			"fieldname": "contractor_name",
			"fieldtype": "Data",
			"label": _("Contractor Name"),
			"width": 200,
		},
		{
			"fieldname": "project_duration",
			"fieldtype": "Data",
			"label": _("Project Duration"),
			"width": 150,
		},
		{
			"fieldname": "competition_status",
			"fieldtype": "Data",
			"label": _("Competition status"),
			"width": 150,
		},
		{
			"fieldname": "reason_for_excluding",
			"fieldtype": "Data",
			"label": _("Reason for excluding the offer, if any"),
			"width": 150,
		},
		{
			"fieldname": "number_of_participants",
			"fieldtype": "Int",
			"label": _("Number of participants in the competition"),
			"width": 150,
		},
		{
			"fieldname": "sort_by_lowest_price",
			"fieldtype": "Data",
			"label": _("Sort by lowest price"),
			"width": 150,
		},
		{
			"fieldname": "bid_value",
			"fieldtype": "Data",
			"label": _("Bid value"),
			"width": 150,
		},
		]
	return columns

def get_conditions(filters):
	conditions = ""

	if filters.competition_status:
		conditions += " competition_status = %(competition_status)s"

	return conditions

def get_data(filters):
	conditions = get_conditions(filters)
	print(conditions, '---conditions')

	data = frappe.db.sql(""" SELECT project_name,  client_name, contractor_name,
					  project_duration,competition_status,number_of_participants,bid_value
					  FROM `tabPrice Determination Form RM`
					  WHERE {0} """.format(conditions), filters, as_dict=1)


	# 	"activity"
	# 	"reason_for_excluding",
	# 	"sort_by_lowest_price",

	return data
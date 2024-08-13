// Copyright (c) 2024, GreyCube Technologies and contributors
// For license information, please see license.txt

frappe.query_reports["Etimad"] = {
	"filters": [
		{
			"fieldname": "competition_status",
			"label":__("Competition status"),
			"fieldtype": "Select",
            "options": ['Open','Won','Lost'],
		}
	]
};

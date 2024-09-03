import frappe

def update_dashboard_link_for_core_doctype(doctype,link_doctype,link_fieldname,group=None):
    print(doctype,link_doctype,link_fieldname,group)
    try:
        d = frappe.get_doc("Customize Form")
        if doctype:
            d.doc_type = doctype
        d.run_method("fetch_to_customize")
        for link in d.get('links'):
            if link.link_doctype==link_doctype and link.link_fieldname==link_fieldname:
                # found so just return
                return
        d.append('links', dict(link_doctype=link_doctype, link_fieldname=link_fieldname,table_fieldname=None,group=group))
        d.run_method("save_customization")
        frappe.clear_cache()
    except Exception:
        frappe.log_error(frappe.get_traceback())


def after_migrate():
    update_dashboard_link_for_core_doctype(doctype='Project',link_doctype='Final Resource Identification Form RM',link_fieldname='rm_project_name',group="Rowad")	
    update_dashboard_link_for_core_doctype(doctype='Project',link_doctype='Project Plan RM',link_fieldname='rm_project_name',group="Rowad")	
    update_dashboard_link_for_core_doctype(doctype='Project',link_doctype='Project Plan Closure Form RM',link_fieldname='rm_project_name',group="Rowad")	
    update_dashboard_link_for_core_doctype(doctype='Project',link_doctype='Project Closure Form RM',link_fieldname='rm_project_name',group="Rowad")	

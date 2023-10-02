import frappe
from frappe import _

@frappe.whitelist()
def get_themes():
	themes=[{"name":"light","label":_("Light")},{"name":"dark","label":_("Dark")}]
	db_themes=frappe.db.get_all("Theme",filters={"disabled":0})
	for t in db_themes:
		themes.append({"name":t["name"].lower(),"label":_(t["name"])})
	return(themes)


@frappe.whitelist()
def switch_theme(theme):
	frappe.db.set_value("User", frappe.session.user, "desk_theme", theme)

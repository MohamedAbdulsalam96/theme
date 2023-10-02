# Copyright (c) 2023, baha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Theme(Document):
	def before_insert(self):
		self.change_css()
	def on_update(self):
		self.change_css()


	def change_css(self):
		css=open("assets/theme/css/theme.css","w")
		themes=frappe.db.get_all("Theme",filters={"disabled":0},fields=["*"])
		doc=frappe.get_doc("DocType","Theme").fields
		fields=[]
		for i in doc:
			if i.fieldtype=="Color":
				fields.append(i.fieldname)
		for t in themes:
			css.write("[data-theme={}]".format(t["name"].lower()))
			css.write("{")
			css.write("\n")
			for f in fields:
				if t[f]:
					css.write(f.replace("_","-")+":"+t[f]+";\n")
			css.write("--primary-color:"+t["__primary"]+";\n")
			css.write("}\n")
		css.close()

"""CRM plugin — search leads, contacts, and deals via the AI Help chat."""

from frappe_assistant_core.plugins.base_plugin import BasePlugin


class CRMPlugin(BasePlugin):
	def get_info(self):
		return {
			"name": "crm",
			"display_name": "CRM",
			"description": "Search and retrieve leads, contacts, deals, and call logs from Frappe CRM",
			"version": "1.0.0",
			"dependencies": [],
			"requires_restart": False,
		}

	def get_tools(self):
		return ["search_leads", "get_lead", "search_contacts", "get_deals", "vmator_help"]

	def validate_environment(self):
		try:
			import frappe
			frappe.get_meta("CRM Lead")
			return True, None
		except Exception:
			return False, "CRM app is not installed or CRM Lead doctype is missing"

"""Search CRM contacts by name, email, or phone."""

import frappe
from frappe_assistant_core.core.base_tool import BaseTool


class SearchContacts(BaseTool):
	def __init__(self):
		super().__init__()
		self.name = "search_contacts"
		self.description = (
			"Search CRM contacts by name, email, or phone number. "
			"Returns a list of matching contacts with key details."
		)
		self.category = "CRM"
		self.source_app = "frappe_assistant_core"
		self.requires_permission = "Contact"
		self.inputSchema = {
			"type": "object",
			"properties": {
				"query": {
					"type": "string",
					"description": "Search text matched against contact name, email, or phone",
				},
				"limit": {
					"type": "integer",
					"description": "Maximum number of results to return (default 10, max 50)",
					"default": 10,
				},
			},
			"required": [],
		}

	def execute(self, arguments):
		query = arguments.get("query", "").strip()
		limit = min(int(arguments.get("limit", 10)), 50)

		if query:
			contacts = frappe.get_list(
				"Contact",
				or_filters=[
					["full_name", "like", f"%{query}%"],
					["email_id", "like", f"%{query}%"],
					["mobile_no", "like", f"%{query}%"],
					["phone", "like", f"%{query}%"],
				],
				fields=["name", "full_name", "email_id", "mobile_no", "phone", "company_name", "modified"],
				limit=limit,
				order_by="modified desc",
			)
		else:
			contacts = frappe.get_list(
				"Contact",
				fields=["name", "full_name", "email_id", "mobile_no", "phone", "company_name", "modified"],
				limit=limit,
				order_by="modified desc",
			)

		return {"contacts": contacts, "count": len(contacts), "query": query or None}

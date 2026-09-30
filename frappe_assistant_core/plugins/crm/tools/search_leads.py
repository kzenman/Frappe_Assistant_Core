"""Search CRM leads by name, email, phone, or status."""

import frappe
from frappe_assistant_core.core.base_tool import BaseTool


class SearchLeads(BaseTool):
	def __init__(self):
		super().__init__()
		self.name = "search_leads"
		self.description = (
			"Search CRM leads by name, email, phone number, or status. "
			"Returns a list of matching leads with key details."
		)
		self.category = "CRM"
		self.source_app = "frappe_assistant_core"
		self.requires_permission = "CRM Lead"
		self.inputSchema = {
			"type": "object",
			"properties": {
				"query": {
					"type": "string",
					"description": "Search text matched against lead name, email, or phone",
				},
				"status": {
					"type": "string",
					"description": "Filter by lead status (e.g. New, Contacted, Qualified, Lost)",
				},
				"lead_owner": {
					"type": "string",
					"description": "Filter by assigned user email",
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
		status = arguments.get("status", "")
		lead_owner = arguments.get("lead_owner", "")
		limit = min(int(arguments.get("limit", 10)), 50)

		filters = []
		if status:
			filters.append(["status", "=", status])
		if lead_owner:
			filters.append(["lead_owner", "=", lead_owner])
		if query:
			or_filters = [
				["lead_name", "like", f"%{query}%"],
				["email", "like", f"%{query}%"],
				["mobile_no", "like", f"%{query}%"],
				["phone", "like", f"%{query}%"],
			]
			# Use frappe.get_list with or_filters
			leads = frappe.get_list(
				"CRM Lead",
				filters=filters,
				or_filters=or_filters,
				fields=["name", "lead_name", "email", "mobile_no", "status", "lead_owner", "creation", "modified"],
				limit=limit,
				order_by="modified desc",
			)
		else:
			leads = frappe.get_list(
				"CRM Lead",
				filters=filters,
				fields=["name", "lead_name", "email", "mobile_no", "status", "lead_owner", "creation", "modified"],
				limit=limit,
				order_by="modified desc",
			)

		return {"leads": leads, "count": len(leads), "query": query or None, "status_filter": status or None}

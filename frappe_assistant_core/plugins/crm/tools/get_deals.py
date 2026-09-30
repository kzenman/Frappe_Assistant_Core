"""Get CRM deals with optional status and owner filters."""

import frappe
from frappe_assistant_core.core.base_tool import BaseTool


class GetDeals(BaseTool):
	def __init__(self):
		super().__init__()
		self.name = "get_deals"
		self.description = (
			"Get CRM deals with optional filtering by status, owner, or search query. "
			"Returns deal pipeline data including stage, value, and owner."
		)
		self.category = "CRM"
		self.source_app = "frappe_assistant_core"
		self.requires_permission = "CRM Deal"
		self.inputSchema = {
			"type": "object",
			"properties": {
				"query": {
					"type": "string",
					"description": "Search text matched against deal name",
				},
				"status": {
					"type": "string",
					"description": "Filter by deal status/stage",
				},
				"deal_owner": {
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
		deal_owner = arguments.get("deal_owner", "")
		limit = min(int(arguments.get("limit", 10)), 50)

		filters = []
		if status:
			filters.append(["status", "=", status])
		if deal_owner:
			filters.append(["deal_owner", "=", deal_owner])

		or_filters = []
		if query:
			or_filters = [["name", "like", f"%{query}%"]]

		deals = frappe.get_list(
			"CRM Deal",
			filters=filters,
			or_filters=or_filters or None,
			fields=["name", "status", "deal_owner", "annual_revenue", "currency", "modified", "creation"],
			limit=limit,
			order_by="modified desc",
		)

		return {"deals": deals, "count": len(deals), "query": query or None, "status_filter": status or None}

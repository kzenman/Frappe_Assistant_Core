"""Get full details for a specific CRM lead."""

import frappe
from frappe_assistant_core.core.base_tool import BaseTool


class GetLead(BaseTool):
	def __init__(self):
		super().__init__()
		self.name = "get_lead"
		self.description = (
			"Get full details for a specific CRM lead by its ID or name. "
			"Returns all key fields including contact info, status, notes, and activity."
		)
		self.category = "CRM"
		self.source_app = "frappe_assistant_core"
		self.requires_permission = "CRM Lead"
		self.inputSchema = {
			"type": "object",
			"properties": {
				"lead_id": {
					"type": "string",
					"description": "The CRM Lead document name (e.g. CRM-LEAD-2024-00001)",
				},
			},
			"required": ["lead_id"],
		}

	def execute(self, arguments):
		lead_id = arguments["lead_id"]

		if not frappe.db.exists("CRM Lead", lead_id):
			return {"error": f"Lead '{lead_id}' not found", "found": False}

		lead = frappe.get_doc("CRM Lead", lead_id)

		return {
			"found": True,
			"lead": {
				"name": lead.name,
				"lead_name": lead.lead_name,
				"email": lead.email,
				"mobile_no": getattr(lead, "mobile_no", None),
				"phone": getattr(lead, "phone", None),
				"status": lead.status,
				"lead_owner": lead.lead_owner,
				"source": getattr(lead, "source", None),
				"company_name": getattr(lead, "company_name", None),
				"city": getattr(lead, "city", None),
				"state": getattr(lead, "state", None),
				"creation": str(lead.creation),
				"modified": str(lead.modified),
				"website": getattr(lead, "website", None),
				"notes": getattr(lead, "notes", None),
			},
		}

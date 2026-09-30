"""
Vmator site knowledge base — answers how-to questions about using the platform.
"""

from frappe_assistant_core.core.base_tool import BaseTool


KNOWLEDGE_BASE = {
	"curbside_estimate": {
		"title": "How to Do a Curbside Estimate",
		"steps": [
			"Go to <strong>Estimating → Estimates</strong> in the left sidebar.",
			"Click <strong>New Estimate</strong> (top right).",
			"Fill in the customer's name, phone number, and email.",
			"Select <strong>Curbside</strong> as the Estimate Type.",
			"Upload damage photos — at minimum: all four sides of the vehicle and close-ups of each damaged area.",
			"Click <strong>Submit</strong>. The AI will analyze the photos and generate a preliminary parts and labor estimate.",
			"Review the AI-generated estimate, adjust line items if needed, then click <strong>Send to Customer</strong> to email or SMS it.",
		],
		"tips": [
			"Better photos = better estimates. Natural daylight and clean panels help the AI detect damage accurately.",
			"You can upload up to 20 photos per estimate.",
			"If the AI misses a panel, add it manually in the Parts section.",
		],
	},
	"add_lead": {
		"title": "How to Add a New Lead",
		"steps": [
			"Go to <strong>Customers → Leads</strong> in the sidebar.",
			"Click <strong>New Lead</strong>.",
			"Enter the customer's name, phone, and email.",
			"Set the <strong>Status</strong> (defaults to New Lead).",
			"Assign a <strong>Lead Owner</strong> (the rep responsible).",
			"Click <strong>Save</strong>.",
		],
		"tips": [
			"Leads from the website estimator widget are created automatically.",
			"You can convert a Lead to a full Estimate from the lead detail page.",
		],
	},
	"book_appointment": {
		"title": "How to Book an Appointment",
		"steps": [
			"Go to <strong>Customers → Appointments</strong> in the sidebar.",
			"Click <strong>New Appointment</strong>.",
			"Select the customer (link to an existing Lead or Contact).",
			"Choose the appointment date and time.",
			"Select the <strong>Location</strong> (shop).",
			"Add any notes, then click <strong>Save</strong>.",
		],
		"tips": [
			"You can also book an appointment directly from a Lead's detail page using the 'Book Estimate' button.",
			"Appointments appear on the calendar view at Customers → Appointments.",
		],
	},
	"call_logs": {
		"title": "How to View and Use Call Logs",
		"steps": [
			"Go to <strong>Customers → Call Logs</strong> in the sidebar.",
			"Each row shows the caller, date/time, duration, and recording link.",
			"Click a row to see the full call detail including any AI transcription.",
			"Missed calls appear in <strong>Missed Call Log</strong> and can trigger automatic SMS follow-ups.",
		],
		"tips": [
			"Call logs are created automatically when calls come through the AI Receptionist.",
			"You can link a call log to an existing Lead from the detail page.",
		],
	},
	"settings": {
		"title": "How to Configure Vmator Settings",
		"steps": [
			"Go to <strong>Settings → Settings</strong> in the sidebar.",
			"The Settings page has tabs: General, Integrations, Users, Telephony, AI, and Branding.",
			"<strong>General</strong>: Shop name, address, business hours.",
			"<strong>Integrations</strong>: Connect Google Drive, Chatwoot, GoHighLevel.",
			"<strong>Users</strong>: Add or remove team members and set their roles.",
			"<strong>Telephony</strong>: Configure your Twilio or Exotel phone number for the AI Receptionist.",
			"<strong>AI</strong>: Choose the AI model (GPT-4o, Claude, Gemini) and set the temperature.",
		],
	},
	"estimates": {
		"title": "How to Manage Estimates",
		"steps": [
			"Go to <strong>Estimating → Estimates</strong> to see all estimates.",
			"Filter by status: Draft, Sent, Approved, or Completed.",
			"Click any estimate to open the detail view.",
			"From the detail view you can: edit line items, add photos, send to customer, or mark as approved.",
			"The <strong>AI Report</strong> tab shows the AI's damage analysis.",
		],
		"tips": [
			"Estimates are created from leads automatically when the customer submits a photo estimate through your website widget.",
		],
	},
	"vehicles": {
		"title": "How to Look Up Vehicles",
		"steps": [
			"Go to <strong>Estimating → Vehicles</strong> in the sidebar.",
			"You can search by VIN, license plate, make, model, or year.",
			"Click a vehicle to see all associated estimates.",
			"From the Estimates detail page, use the <strong>VIN Lookup</strong> button to auto-fill vehicle specs.",
		],
	},
	"damage_photos": {
		"title": "How to Manage Damage Photos",
		"steps": [
			"Go to <strong>Estimating → Damage Photos</strong> to see all uploaded photos.",
			"Photos are grouped by estimate/lead.",
			"Click any photo to open the full-size view.",
			"From an Estimate's detail page, use the <strong>Photos</strong> tab to upload or delete photos.",
		],
	},
	"ai_receptionist": {
		"title": "How the AI Receptionist Works",
		"steps": [
			"The AI Receptionist answers inbound calls to your Twilio/Exotel phone number automatically.",
			"It collects caller name, reason for calling, and books appointments.",
			"After hours, it takes a voicemail message and transcribes it automatically.",
			"All calls are logged in <strong>Customers → Call Logs</strong>.",
			"Missed calls trigger an automatic SMS follow-up to the caller.",
		],
		"tips": [
			"Configure the receptionist script in <strong>Settings → Telephony</strong>.",
			"You can set business hours so after-hours calls get a different message.",
		],
	},
	"leads_pipeline": {
		"title": "How the Lead Pipeline Works",
		"steps": [
			"Leads move through stages: New Lead → Contacted → Estimate Sent → Booked Repair → Completed.",
			"Use the Kanban view (Leads → Kanban) to drag leads between stages.",
			"Each stage change is logged in the lead's activity feed.",
			"Set up automations in Settings → Integrations to notify your team on stage changes.",
		],
	},
}

# Keyword → topic mapping for automatic matching
TOPIC_KEYWORDS = {
	"curbside_estimate": ["curbside", "curb side", "curb-side", "photo estimate", "drive-by", "driveby"],
	"add_lead": ["add lead", "new lead", "create lead", "add customer", "new customer"],
	"book_appointment": ["book", "appointment", "schedule", "calendar"],
	"call_logs": ["call log", "call logs", "calls", "missed call", "voicemail", "recording"],
	"settings": ["settings", "configure", "configuration", "setup", "set up"],
	"estimates": ["estimate", "estimates", "quote", "quotes"],
	"vehicles": ["vehicle", "vehicles", "vin", "license plate", "car", "truck"],
	"damage_photos": ["photo", "photos", "image", "images", "damage photo"],
	"ai_receptionist": ["receptionist", "ai phone", "auto answer", "after hours", "phone system"],
	"leads_pipeline": ["pipeline", "stages", "kanban", "lead stage", "workflow"],
}


class VmatorHelp(BaseTool):
	def __init__(self):
		super().__init__()
		self.name = "vmator_help"
		self.description = (
			"Answer how-to questions about using Vmator. Use this when the user asks how to do something "
			"on the site — like how to create an estimate, how to book an appointment, how to do a curbside "
			"estimate, how to configure settings, how to use call logs, how to manage vehicles, or how the "
			"AI receptionist works. Also useful when no other tool is appropriate."
		)
		self.category = "CRM"
		self.source_app = "frappe_assistant_core"
		self.inputSchema = {
			"type": "object",
			"properties": {
				"topic": {
					"type": "string",
					"description": (
						"The feature or task the user needs help with. "
						"One of: curbside_estimate, add_lead, book_appointment, call_logs, settings, "
						"estimates, vehicles, damage_photos, ai_receptionist, leads_pipeline. "
						"If unsure, pass the user's raw question as 'query' instead."
					),
				},
				"query": {
					"type": "string",
					"description": "The user's raw question if no specific topic applies.",
				},
			},
			"required": [],
		}

	def execute(self, arguments):
		topic = arguments.get("topic", "").lower().strip()
		query = arguments.get("query", "").lower().strip()

		# Try direct topic lookup first
		if topic and topic in KNOWLEDGE_BASE:
			return {"found": True, "topic": topic, "content": KNOWLEDGE_BASE[topic]}

		# Keyword match against query or topic string
		search_text = query or topic
		if search_text:
			for kb_topic, keywords in TOPIC_KEYWORDS.items():
				if any(kw in search_text for kw in keywords):
					return {"found": True, "topic": kb_topic, "content": KNOWLEDGE_BASE[kb_topic]}

		# Return full index if nothing matches
		return {
			"found": True,
			"topic": "index",
			"content": {
				"title": "Vmator Help — What can I help you with?",
				"topics": [
					{"key": k, "title": v["title"]}
					for k, v in KNOWLEDGE_BASE.items()
				],
			},
		}

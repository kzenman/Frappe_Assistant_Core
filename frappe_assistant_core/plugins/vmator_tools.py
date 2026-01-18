from frappe_assistant_core.plugins import register_tool

@register_tool("Upload Vehicle Images", group="Vmator Tools")
def upload_vehicle_images(company, files):
    """Uploads images to Google Drive."""
    from vmator.api.google_drive_upload import upload_vehicle_images
    return upload_vehicle_images(company, files)

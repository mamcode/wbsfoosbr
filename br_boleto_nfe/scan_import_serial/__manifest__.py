{
    "name": "Scan Serial Number Import",
    "version": "11.0.1.0.0",
    "category": "Generic Modules",
    "author": "",
    "description": "",
    "website": "",
    "depends": [
        "stock",
    ],
    "data": [
		#"security/scan_import_security.xml",
		"security/ir.model.access.csv",
        "views/scan_serial_view.xml",
		"wizard/wizard_generate_report_view.xml",
		"report/serial_report_view.xml",
		"report/report_menu.xml",
		"views/serial_menu.xml",
    ],
    "installable": True,
}

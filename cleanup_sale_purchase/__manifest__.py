{
    'name': 'Database content cleanup - Sales',
    'summary': 'Remove all sales and purchases related content from the database',
    'version': '11.0',
    'author': "Udoo",
    'depends': [
		'purchase',
        'sale',
		'base',
		'sales_team',
    ],
    'category': 'Tools',
    'data': [
		'view/purge_wizard.xml',
        'view/menu.xml',
	],
    'installable': True,
    'auto_install': False,
}

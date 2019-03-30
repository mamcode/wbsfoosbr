# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sales Delay',
    'category': 'Website',
    'description': """
    Inform Customers about availability of products
""",
    'depends': [
        'website_sale',
        
    ],
    'auto_install': True,
    'data': [
        'views/website_sales_delay.xml',
		'views/end_sales_delay.xml',
    ]
}

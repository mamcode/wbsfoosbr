# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Import Serial Numbers on Delivery Orders',
    'version': '1.1',
    'author': '',
    'website': '',
    'category': 'Inventory',
    'depends' : ['base','stock'],
    'description': """
          Product Serial Numbers Import on Delivery Orders and create serial number if missing
    """,
    'data': [
		'views/delivery_serial_import_view.xml',
		'views/stock_production_lot_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application':True
}
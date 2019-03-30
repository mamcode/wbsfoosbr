# -*- coding: utf-8 -*-

{
    'name': "SOC",
    'summary': 'Odoo module for consignment control in client facitilies (example: a publisher controls his books in bookshops',
    'description': 'Odoo module for consignment control in client facitilies (example: a publisher controls his books in bookshops. It was designed for a publishing house.',
    'author': "Udoo",
    'website': "www.udoo.com.br",
    'category': 'General',
    'version': '12.0',
    'depends': ['base', 'sale', 'stock', 'product'],

    'data': [
        'views/res_view.xml',
        'views/sale_view.xml',
        'views/stock.xml',
        'views/import_wizard_product_adj.xml',
        # 'views/consignment_view.xml',
    ],
    'application':True,
    # only loaded in demonstration mode
    #'demo': [
        # 'demo.xml',
    #],
}

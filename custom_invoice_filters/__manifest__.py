# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Invoice Filters',
    'summary': """Custom Invoice filters""",
    'description': """This module will add new custom filters to invoice search.""",
    'version': '11.0.1.0.0',
    'category': 'Localization',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'base', 'account',
    ],
    'data': [
        'views/account_invoice_view.xml',
    ],
}

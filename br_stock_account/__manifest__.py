# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Odoo Brasil - WMS Accounting',
    'summary': """Realiza o link entre faturas e o estoque e logistica""",
    'description': 'Odoo Brasil - WMS Accounting',
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'stock_account', 'br_account', 'br_account_einvoice'
    ],
    'data': [
        'views/account_invoice.xml',
        'reports/account_invoice.xml',
    ],
    'auto_install': True,
}

# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Contas a Pagar e Receber',
    'summary': """Facilita a visualização de parcelas a pagar e receber
    no Odoo""",
    'description': """Facilita a visualização de parcelas a pagar e receber
    no Odoo""",
    'version': '11.0.1.0.0',
    'category': 'Invoicing & Payments',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'br_account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_invoice.xml',
        'views/br_account_payment.xml',
        'views/payment_mode.xml',
        'views/account_payment.xml',
        'views/account_journal.xml',
        'views/account_move.xml',
        'security/account_security.xml',
    ],
    'installable': True,
    'application': True,
}

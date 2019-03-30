# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Udoo - Brazilian electronic invoice 4.0',
    'summary': """udoo - Brazilian electronic invoice 4.0""",
    'description': """Base Module for the Brazilian Invoice Eletronic""",
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'contributors': [
        'Fernando H vinha <dev@udoo.com.br>'
    ],
    'depends': [
        'l10n_br',
        'br_base',
        'l10n_br_reports',
        'document',
        'br_coa',
        'br_account',
        'br_data_account',
        'br_account_einvoice',
        'br_account_payment',
        'br_coa_simple',
        'br_data_account_product',
        'br_data_base',
        'br_nfe',
        'br_sale',
        'br_sale_payment',
        'br_sale_stock',
        'br_zip',
    ],
    'data': [],
    'installable': True
}

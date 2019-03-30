# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Account E-Invoice',
    'summary': """Base Module for the Brazilian Invoice Eletronic""",
    'description': """Base Module for the Brazilian Invoice Eletronic""",
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'document',
        'br_base',
        'br_account',
        'br_data_account',
    ],
    'data': [
        'data/nfe_cron.xml',
        'data/br_account_einvoice.xml',
        'security/ir.model.access.csv',
        'views/invoice_eletronic.xml',
        'views/account_invoice.xml',
        'views/account_config_settings.xml',
        'views/res_company.xml',
        'wizard/invoice_eletronic_selection_wizard_view.xml',
    ],
    'installable': True
}

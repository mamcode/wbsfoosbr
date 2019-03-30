# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{
    'name': 'Invoice Account Multiselect',
    'summary': """Custom Invoice Account Multiselect""",
    'description': """This module will add new custom field to partner which allow to select multiple account and these accounts will reflect in account_id in invoice.""",
    'version': '11.0.1.0.0',
    'category': 'Localization',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'base', 'account',
    ],
    'data': [
        'views/res_partner_view.xml',
    ],
}

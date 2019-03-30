# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{  # pylint: disable=C8101,C8103
    'name': 'Cash Flow Report - Base Account',
    'description': "Cash Flow Report and Graph",
    'summary': """Base for the cash flow""",
    'version': '11.0.1.0.0',
    'category': 'Tools',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'account', 'br_account_payment'
    ],
    'data': [
        'views/cash_flow_view.xml',
        'wizard/cash_flow.xml',
        'reports/account_cash_flow.xml',
    ],
}

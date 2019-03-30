# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{  # pylint: disable=C8101,C8103
    'name': 'Tax Accounting',
    'summary': """Executes a monthly tax accouting
    - Maintained by Trustcode""",
    'description': """Executes a monthly tax accouting""",
    'version': '11.0.1.0.0',
    'category': 'Localization',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'account_voucher', 'br_account'
    ],
    'data': [
        'wizard/account_close.xml',
    ],
    'application': True,
}

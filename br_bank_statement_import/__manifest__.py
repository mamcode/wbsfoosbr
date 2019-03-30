# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Importação de extratos bancários',
    'summary': """Importação de extratos bancários nos formatos OFX e
    Cnab 240""",
    'description': 'Import Cnab Files',
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'account_bank_statement_import'
    ],
    'external_dependencies': {
        'python': [
            'ofxparse'
        ],
    },
    'data': [
        'views/account_bank_statement_import.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
}

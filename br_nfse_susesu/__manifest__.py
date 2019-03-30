# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Envio de NFS-e - Susesu',
    'summary': """Permite o envio de NFS-e Susesu através das faturas do Odoo""",
    'description': 'Envio de NFS-e - Susesy',
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'br_nfse',
    ],
    'data': [
        'views/invoice_eletronic.xml',
        'views/res_company.xml',
    ],
    'installable': True,
    'application': True,
}

# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Brazilian Localisation ZIP Codes',
    'description': 'Brazilian Localisation ZIP Codes',
    'license': 'AGPL-3',
    'author': 'Udoo',
    'version': '11.0.1.0.0',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'br_base',
    ],
    'data': [
        'views/br_zip_view.xml',
        'views/res_partner_view.xml',
        'views/res_bank_view.xml',
        'wizard/br_zip_search_view.xml',
        'security/ir.model.access.csv',
    ],
    'test': ['test/zip_demo.yml'],
    'category': 'Localization',
    'installable': True,
}

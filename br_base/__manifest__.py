# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Odoo Brasil - Módulo Base',
    'description': 'Brazilian Localization Base',
    'version': '11.0.1.0.0',
    'category': 'Localisation',
    'license': 'AGPL-3',
    'author': 'Udoo',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'base', 'web',
    ],
    'external_dependencies': {
        'python': [
            'pytrustnfe.nfe', 'pytrustnfe.certificado'
        ],
    },
    'data': [
        'views/br_base.xml',
        'views/ir_module.xml',
        'views/br_base_view.xml',
        'views/res_country_view.xml',
        'views/res_partner_view.xml',
        'views/res_bank_view.xml',
        'views/res_company_view.xml',
        'views/base_assets.xml',
        'security/ir.model.access.csv',
    ],
    'test': [
        'test/base_inscr_est_valid.yml',
        'test/base_inscr_est_invalid.yml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'post_init_hook': 'post_init',
    'installable': True,
    'auto_install': True,
}

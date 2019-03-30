# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Brazilian Localization CRM',
    'description': 'Brazilian Localization for CRM module',
    'category': 'Localisation',
    'license': 'AGPL-3',
    'author': 'Udoo',
    'website': 'http://www.udoo.com.br',
    'version': '11.0.1.0.0',
    'depends': [
        'br_base',
        'crm',
    ],
    'data': [
        'views/crm_lead_view.xml',
        'views/crm_opportunity_view.xml',
    ],
    'demo': [],
    'installable': True,
}

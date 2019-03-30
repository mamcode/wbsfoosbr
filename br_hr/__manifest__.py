# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Brazilian Localization HR',
    'description': """Brazilian Localization HR with informations
        refered to the national context of HR""",
    'category': 'Localization',
    'author': 'Udoo',
    'sequence': 45,
    'maintainer': 'Udoo',
    'website': 'http://www.udoo.com.br',
    'version': '11.0.1.0.0',
    'depends': ['hr', 'br_base'],
    'data': [
        'data/br_hr.cbo.csv',
        'security/ir.model.access.csv',
        'view/br_hr_cbo_view.xml',
        'view/hr_employee_view.xml',
        'view/hr_job_view.xml',
    ],
    'post_init_hook': 'post_init',
    'installable': True,
    'license': 'AGPL-3',
}

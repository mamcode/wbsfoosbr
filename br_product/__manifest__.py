# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{  # pylint: disable=C8101,C8103
    'name': 'Brazilian Localization for Product',
    'summary': """Brazilian Localization for Product""",
    'description': """Brazilian Localization for Product""",
    'version': '11.0.1.0.0',
    'category': 'Localization',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'product', 'br_base',
    ],
    'data': [
        'views/product_pricelist.xml',
        'views/product_category.xml',
        'views/product_template.xml',
    ],
}

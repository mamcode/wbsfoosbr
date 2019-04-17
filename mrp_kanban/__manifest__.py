# -*- coding: utf-8 -*-

{
    'name': "Add Stages to MRP order",
    'summary': '',
    'description': 'This module add stages on kanban view of Manufacturing order.',
    'author': "Udoo",
    'website': "www.udoo.com.br",
    'category': 'MRP',
    'version': '12.0',
    'depends': ['base', 'mrp'],

    'data': [
        'views/mrp_view.xml',
    ],
    'application':True,
    # only loaded in demonstration mode
    #'demo': [
        # 'demo.xml',
    #],
}

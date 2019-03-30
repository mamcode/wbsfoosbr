# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Vinculo entre boleto e NFe',
    'summary': """Vinculo entre boleto e NFe, permite enviar os dois
        via e-mail juntamente""",
    'description': """Vinculo entre boleto e NFe""",
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'br_boleto', 'br_account_einvoice'
    ],
    'data': [
        'views/res_config_settings.xml',
    ],
    'auto_install': True,
}

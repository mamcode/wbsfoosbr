# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{  # pylint: disable=C8101,C8103
    'name': 'Módulo base para envio de NFS-e',
    'summary': """Permite o envio de NFS-e através das faturas do Odoo""",
    'description': 'Módulo base para envio de NFS-e',
    'version': '11.0.1.0.0',
    'category': 'account',
    'author': 'Udoo',
    'license': 'AGPL-3',
    'website': 'http://www.udoo.com.br',
    'depends': [
        'br_account_einvoice',
    ],
    'external_dependencies': {
        'python': [
            'pytrustnfe.certificado'
        ],
    },
    'data': [
        'views/account_invoice.xml',
        'views/invoice_eletronic.xml',
        'wizard/cancel_nfse.xml',
    ],
    'installable': True,
}

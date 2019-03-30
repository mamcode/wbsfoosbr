# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    product_id = fields.Many2one('product.product', related='invoice_line_ids.product_id', string='Product')

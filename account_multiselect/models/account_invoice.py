# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import fields, models, api

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    product_id = fields.Many2one('product.product', related='invoice_line_ids.product_id', string='Product')

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id(self):
        res = super(AccountInvoice, self)._onchange_partner_id()
        if self.partner_id and self.partner_id.account_ids:
        	if res.get('domain', False):
        		res['domain'].update({'account_id': [('id', 'in', self.partner_id.account_ids.ids)]})
        	else:
        		res['domain'] = {'account_id': [('id', 'in', self.partner_id.account_ids.ids)]}
        return res

class ResPartner(models.Model):
    _inherit = 'res.partner'

    account_ids = fields.Many2many('account.account', 'account_account_invoice_rel', 'partner_id', 'account_id', domain="[('internal_type', '=', 'payable'), ('deprecated', '=', False)]", string='Accounts')


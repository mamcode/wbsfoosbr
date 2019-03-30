# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
	_inherit = 'account.invoice'
	
	# @api.multi
	# def action_invoice_open(self):
	# 	super(AccountInvoice, self).action_invoice_open()
	# 	# return 1/0

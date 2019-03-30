# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2018-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
#################################################################################
from odoo import models, fields, api, _

class account_invoice(models.Model):
	_inherit = "account.invoice"

	wk_website_id = fields.Many2one(
        comodel_name="website",
        string="Website",
        help="website for which this invoice belongs to."
        )


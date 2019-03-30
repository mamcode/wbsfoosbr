# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################

from odoo import api, fields, models
class ResPartner(models.Model):
	_inherit = 'res.partner'

	website_ids = fields.Many2many(
	'website',
	'partner_id',
	'website_id',
	'partner_website_rel',
	string="Websites",
	)
	default_website = fields.Many2one(
		comodel_name="website",
		string="Default Website",
		help="Original Website from  which the customer actually came."
	)
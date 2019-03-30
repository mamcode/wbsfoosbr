# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)
class StockPicking(models.Model):
	_inherit = "stock.picking"

	
	wk_website_id = fields.Many2one(
		comodel_name="website",
		string="Website",
		help="Website from which the order actually came"
		)

class StockMove(models.Model):
	_inherit = "stock.move"

	def _get_new_picking_values(self):
		res = super(StockMove, self)._get_new_picking_values()
		order_id = self.env['sale.order'].sudo().search([('name','=',self.origin)], limit=1)
		if order_id and order_id.wk_website_id:
			res['wk_website_id'] = order_id.wk_website_id.id
		return res

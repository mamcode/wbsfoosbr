# -*- coding: utf-8 -*-
from odoo import api, fields, models,tools
from odoo.exceptions import UserError
from odoo.tools.translate import _

class StockMove(models.Model):   
	_inherit = "stock.move"
	
	converted_uom_qty = fields.Float('Initial Demand(UOM)', compute="_compute_uom_convert")
	
	@api.one
	@api.depends('product_uom_qty','product_uom')
	def _compute_uom_convert(self):
		if self.product_uom:
			uom = self.product_uom.name
			if uom == 'g' or uom == 'ml':
				self.converted_uom_qty = self.product_uom_qty / 1000
			else:
				self.converted_uom_qty = self.product_uom_qty
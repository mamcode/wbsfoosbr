# -*- coding: utf-8 -*-
from odoo import api, fields, models,tools
from odoo.exceptions import UserError
from odoo.tools.translate import _

class StockPicking(models.Model):   
	_inherit = "stock.production.lot"
	
	origin = fields.Char()
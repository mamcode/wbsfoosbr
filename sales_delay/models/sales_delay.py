# Sales Delay Model.py

from odoo import models, fields, _

class ProductTemplate(models.Model):
	_inherit = "product.template"
		
	sales_delay = fields.Float('Sales Delay', required=True)
		
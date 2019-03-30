# -*- coding: utf-8 -*-

import time
from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class ReportSerialLoan(models.AbstractModel):
	_name = "report.stock_count.report_stock_count_seria"
		
	
	def _get_stock_count(self):
		products = self.env['product.product'].search([('qty_available', '=', 0)])
		line = []
		
		for product in products:
			serials = self.env['stock.production.lot'].search([('product_id', '=', product.id)]).mapped('name')
			line.append({
				'product': product,
				'qty': product.qty_available,
				'serials': ','.join(serials)
			})
		
	@api.model
	def get_report_values(self, docids, data=None):
		model = self.env.context.get('active_model')
		docs = self.env['wizard.generate.stock.report'].browse(docids)
			
		docargs = {
			'doc_ids': self.ids,
			'doc_model': model,
			'data': data['form'],
			'docs': docs,
			'time': time,
			'lines': self._get_stock_count(),
		}
		return docargs

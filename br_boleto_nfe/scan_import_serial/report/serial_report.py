# -*- coding: utf-8 -*-

import time
from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class ReportSerialLoan(models.AbstractModel):
	_name = "report.scan_import_serial.report_scan_wiz_serial"
		
	
	def _get_serial_line(self, type):
		if type == '001':
			serials = self.env['scan.serial.item'].search([('matched', '=', True)]).mapped('serial')
			return self.env['stock.production.lot'].search([('name', 'in', serials)], order='product_id')
		elif type == '002':
			return self.env['scan.serial.item'].search([('not_matched', '=', True)]).mapped('serial')
		elif type == '003':
			scanned_serial = self.env['scan.serial.item'].search([('matched', '=', True)]).mapped('serial')
			inventory_serial = self.env['stock.production.lot'].search([('name', 'not in', scanned_serial)], order='origin')
			return inventory_serial
		return None
		
	@api.model
	def get_report_values(self, docids, data=None):
		if not data.get('form') or not self.env.context.get('active_model') or not self.env.context.get('active_id'):
			raise UserError(_("Form content is missing, this report cannot be printed."))
		
		model = self.env.context.get('active_model')
		docs = self.env['wizard.generate.report'].browse(data['ids'])
			
		docargs = {
			'doc_ids': self.ids,
			'doc_model': model,
			'data': data['form'],
			'docs': docs,
			'time': time,
			'lines': self._get_serial_line(data['form'].get('type')),
		}
		return docargs

from odoo import api, fields, models
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class WizardStockSerial(models.TransientModel):
	_name = 'wizard.generate.stock.report'
	_description = 'Generate Stock Count Report'
	
	
	@api.multi
	def report_serial_print(self):
		data = {}
		return self.env.ref('stock_report.report_stock_serial_standing_list').report_action(self, data=data)
		
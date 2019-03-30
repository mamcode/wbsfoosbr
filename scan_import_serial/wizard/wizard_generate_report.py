from odoo import api, fields, models
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class WizardAddSerial(models.TransientModel):
	_name = 'wizard.generate.report'
	_description = 'Generate Serial Report'

	type = fields.Selection([('001', 'Serial Numbers that were scanned and have match on inventory'),('002','Serial Numbers that were scanned and dont have match on inventory'),('003', 'Serial numbers that were not scanned')], required=True, string='Report Type:')
	
	@api.multi
	def report_serial_print(self):
		data = {}
		wiz_rec = self.read()
		data.update(form=wiz_rec[0], ids=self.id)
		return self.env.ref('scan_import_serial.report_serial_standing_list').report_action(self, data=data)
		
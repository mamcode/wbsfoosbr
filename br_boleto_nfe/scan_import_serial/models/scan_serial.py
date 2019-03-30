from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ScanSerial(models.Model):
	_name = 'scan.serial'
	_rec_name = 'date'
	
	date = fields.Date(string='Date Recieved', required=True, default=fields.Date.today())
	picking_id = fields.Many2one('stock.picking')
	serial_item_id = fields.One2many('scan.serial.item', 'serial_id')
	#notscanned_serial_id = fields.One2many('unscan.serial.item', 'serial_id')
	state = fields.Selection([('draft', 'Draft'),('complete', 'Scanning Done')], default='draft', copy=False)
		
	@api.multi
	def action_complete(self):
		self.state = 'complete'
		
	@api.multi
	def reset_draft(self):
		self.state = 'draft'
		
	@api.multi
	def unlink(self):
		result = self.filtered(lambda line: line.state == 'complete')
		if result:
			raise UserError("Cannot deleted completed record")
		super(ScanSerial, self).unlink()


class ScanSerialItem(models.Model):
	_name = "scan.serial.item"
	
	serial = fields.Char('Serial Number')
	product_id = fields.Many2one('product.product', compute="_process_serials", store=True)
	matched = fields.Boolean('Product Found', default=False, compute="_process_serials", store=True)
	not_matched = fields.Boolean('No matched', compute="_process_serials", store=True)
	serial_id = fields.Many2one('scan.serial')
	state = fields.Selection([('draft', 'Draft'),('done', 'Done')], default='draft', copy=False)
	
	@api.depends('serial')
	def _process_serials(self):
		for rec in self:
			serial = rec.serial
			if serial:
				found = self.env['stock.production.lot'].search([]).filtered(lambda line: line.name == rec.serial.strip())
				if found:
					rec.matched = True
					rec.not_matched = False
					rec.product_id = found[0].product_id.id
				else:
					rec.not_matched = True
	
	@api.multi
	def unlink(self):
		result = self.filtered(lambda line: line.state == 'done')
		if result:
			raise UserError("Cannot deleted completed record")
		super(ScanSerialItem, self).unlink()
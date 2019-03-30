from odoo import api, fields, models
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class WizardProductSerial(models.TransientModel):
	_name = 'wizard.scan.dev.serial'
	_description = 'Scan ProductSerial'

	serial = fields.Char(required=True)
	picking_id = fields.Many2one('stock.picking')
	
	@api.multi
	def save_next(self):
		#search for serial in stock.production.lot
		lot = self.env['stock.production.lot'].search([('name', '=', self.serial)], limit=1)
		move_line = self.picking_id.move_lines.filtered(lambda r: r.product_id.id == lot.product_id.id)
		if move_line:
			#filter for already scanned serial
			if self.picking_id.move_line_ids.filtered(lambda r: r.lot_id.id == lot.id):
				raise UserError("Todos os produtos ja foram escaneados")
			vals = {
				'move_line_ids': [(0,0,{
					'product_id': lot.product_id.id,
					'lot_id':lot.id,
					'lot_name': lot.name,
					'qty_done': 1,
					'product_uom_qty' : 0,
					'product_uom_id' : move_line.product_uom.id,
					'location_id' : move_line.location_id.id,
					'location_dest_id': move_line.location_dest_id.id,
					'picking_id': self.picking_id.id})]
				}
			move_line.write(vals)
			#self.picking_id.write(vals)
		else:
			raise UserError("Producto nao encontrado no pedido")
		#referesh 
		self.serial = ''
		return {"type": "ir.actions.do_nothing"}
		
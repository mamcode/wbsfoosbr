from odoo import api, fields, models
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class WizardProductSerial(models.TransientModel):
	_name = 'wizard.scan.dev.serial'
	_description = 'Scan ProductSerial'

	serial = fields.Char(required=True)
	picking_id = fields.Many2one('stock.picking')
	
	@api.onchange('serial')
	def onchange_serial(self):
		if self.serial:
			#search for serial in stock.production.lot
			lot = self.env['stock.production.lot'].search([('name', '=', self.serial.strip())])
			move_line = self.picking_id.move_lines.filtered(lambda r: r.product_id.id == lot.product_id.id)
			if move_line:
				#filter for already scanned serial
				if self.picking_id.move_line_ids.filtered(lambda r: r.lot_id.id == lot.id and r.qty_done > 0):
					raise UserError("Todos os produtos ja foram escaneados")
				move_lines = self.picking_id.move_line_ids.filtered(lambda r: r.lot_id.id == lot.id and r.product_id.id == lot.product_id.id)
				if move_lines:
					move_lines[0].write({
						'qty_done': 1,
						'lot_id': lot.id,
						'lot_name': lot.name,
					})
				else:
					for line in move_line.filtered(lambda r: r.product_uom_qty  <= r.quanity_done)
						vals = {
							'move_line_ids': [(0,0,{
								'product_id': lot.product_id.id,
								'lot_id':lot.id,
								'lot_name': lot.name,
								'qty_done': 1,
								'product_uom_qty' : 1,
								'product_uom_id' : line.product_uom.id,
								'location_id' : line.location_id.id,
								'location_dest_id': line.location_dest_id.id,
								'picking_id': self.picking_id.id})]
							}
						line.write(vals)
						break
			else:
				raise UserError("Producto nao encontrado no pedido")
			#referesh 
			self.serial = ''
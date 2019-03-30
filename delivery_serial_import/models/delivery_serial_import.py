# -*- coding: utf-8 -*-
from odoo import api, fields, models,tools
from odoo.exceptions import UserError
from odoo.tools.translate import _
from datetime import datetime, date
import base64
import os
import logging
import csv
from tempfile import TemporaryFile

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):   
	_inherit = "stock.picking"
	
	file_import = fields.Binary("Import File", help="*Import a list of lot/serial numbers from a csv file \n *Only csv files is allowed \n *The csv file must contain a row header namely 'Serial Number'")
	file_name = fields.Char("Filename")
	
	#mporting "csv" file and finding the product plus setting the serials.
	@api.multi
	def input_file(self):
		self.ensure_one()
		if self.file_import:
			#file_value = self.file_import.decode("utf-8")
			filename,FileExtension = os.path.splitext(self.file_name)
			if FileExtension.lower() != '.csv':
				raise UserError("Invalid File! Please import the 'csv' file")
				
			#reader = csv.DictReader(base64.b64decode(self.file_import).decode("utf-8").split("\n"))
			fileobj = TemporaryFile('w+')
			try:
				fileobj.write(base64.b64decode(self.file_import).decode("utf-8"))
			except:
				raise UserError('Please convert file to utf-8 encoding or remove foreign characters eg ã')
			fileobj.seek(0)
			reader = csv.reader(fileobj, delimiter=';', quotechar="'")
			next(reader)
			file_data = reader
			
			check = False
			product_data_list = {}
			for line in file_data:
				if not line:
					continue
				if not check:
					check = self.check_header(line)
				
				#find product.
				product = self.env['product.product'].search([('name', '=', line[1].strip()),('default_code', '=', line[0].strip())], limit=1) or self.env['product.product'].search([('default_code', '=', line[0].strip())], limit=1)
				
				if not product:
					raise UserError('Product ' + line[1]  + ' [' + line[0] + '] missing in the system!')
					
				if not product_data_list.get(product.id):
					product_data_list[product.id] = []
					
				lot = self.env['stock.production.lot'].search([('product_id','=', product.id),('name','=', line[4])])
				#write some value to lot if exist
				l_val = {}
				if lot:
					#raise UserError('Lot ' + lot.name + ' already exist!')
					if not lot.origin:
						l_val['origin'] = self.origin
					if not lot.life_date:
						l_val['life_date'] = datetime.strptime(line[3], '%d/%m/%Y').date()
					lot.write(l_val)
				if not lot or product != lot.product_id :
					lot = self.env['stock.production.lot'].create({
						'name': line[4],
						'product_id': product.id,
						'ref': line[2],
						'origin': self.origin,
						'life_date': datetime.strptime(line[3], '%d/%m/%Y').date(),
					})
				
				
				#find stock move for the current product in the stock picking
				move_line = self.env['stock.move'].search([('picking_id', '=', self.id),('product_id', '=', product.id)], limit=1)
				if not move_line:
					raise UserError('No Delivery Order for Product ' + line[1]  + ' [' + line[0] + '] !!!!')
				
				if  move_line.product_qty == move_line.quantity_done and move_line.move_line_nosuggest_ids.mapped('lot_id'):
					raise UserError(_('Serial Number Already Attached to Delivery Order of ' + move_line.product_id.name + " !!!"))
					
				product_data_list.get(product.id).append((0,0,{
					'product_id': product.id,
					'lot_name': line[4],
					'lot_id': lot.id,
					'qty_done': 1,
					'product_uom_qty' : 1,
					'product_uom_qty' : 1,
					'product_uom_id' : move_line.product_uom.id,
					'location_id' : move_line.location_id.id,
					'location_dest_id': move_line.location_dest_id.id,
					'picking_id': self.id,
				}))
				
			for move in self.move_lines:
				move.move_line_ids = product_data_list.get(move.product_id.id)
				#self.move_line_ids = product_data_list.get(move.product_id.id)
				
			move.move_line_ids.filtered(lambda line: line.qty_done == 0).unlink()
					 
		else :
			raise UserError("Invalid File! Please import the 'csv' file")
		
	def check_header(self, line):
		if len(line) == 5:
			return True
		raise UserError('Incomplete Header')
	
class ProductUoM(models.Model):
	_inherit = 'product.uom'
	
	#ref: product unit of measure
	@api.multi
	def _compute_quantity(self, qty, to_unit, round=True, rounding_method='UP'):
		if not self:
			return qty
		self.ensure_one()
		amount = qty / self.factor
		if to_unit:
			amount = amount * to_unit.factor
			if round:
				amount = tools.float_round(amount, precision_rounding=to_unit.rounding, rounding_method=rounding_method)
		return amount
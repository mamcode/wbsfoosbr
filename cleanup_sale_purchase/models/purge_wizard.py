from odoo import api, models

class PurgeWizard(models.TransientModel):
	""" Main wizard for cleaning up model content """
	_name = 'cleanup.wizard'

	@api.model
	def get_model_list(self):
		"""
		Returns a list of models whose content should be removed.
		"""
		res = [
			'stock_inventory',
			'stock_inventory_line',
			# 'stock_picking',
			# 'stock_move_line',
			# 'stock_move',
			# 'stock_quant',
			# 'stock_production_lot',
			# 'sale_order_line',
			# 'sale_order',
			# 'purchase_order_line',
			# 'purchase_order',
		]
		return res

	@api.multi
	def purge_all(self):
		list_model = self.get_model_list()
		
		for list in list_model:
			self.env.cr.execute("DELETE FROM " + list)

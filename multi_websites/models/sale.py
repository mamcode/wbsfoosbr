# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################
from odoo.http import request
from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
	_inherit = 'sale.order'
	
	wk_website_id = fields.Many2one(
		comodel_name="website",
		string="Website",
		help="Website from which order came"
	)

	@api.onchange('partner_id')
	def onchange_partner_id_website(self):
		if self.partner_id and self.partner_id.default_website:
			self.wk_website_id = self.partner_id.default_website.id
		else:
			self.wk_website_id = False

	@api.model
	def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
		if request.httprequest.path == '/website/fetch_dashboard_data':
			if request.session.get('wk_multi_website_id'):
				domain.append(('wk_website_id','=', int(request.session.get('wk_multi_website_id'))))
		return super(SaleOrder, self).read_group(domain, fields, groupby, offset, limit, orderby, lazy)
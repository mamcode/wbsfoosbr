# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#    You should have received a copy of the License along with this program.
#    If not, see <https://store.webkul.com/license.html/>
#################################################################################
from odoo.addons.website.controllers.backend import WebsiteBackend
from odoo.http import request
from odoo import http
import logging
_logger = logging.getLogger(__name__)

class WebsiteSaleBackend(WebsiteBackend):

	@http.route()
	def fetch_dashboard_data(self, date_from, date_to):
		results = super(WebsiteSaleBackend, self).fetch_dashboard_data(date_from, date_to)
		website_ids = request.env['website'].search([])
		values = []
		for website in website_ids:
			selected_website = website.id
			if request.session.get('wk_multi_website_id'):
				selected_website = request.session['wk_multi_website_id']
			values.append({'id':website.id,'name':website.name,'selected_website':int(selected_website)})
		results['dashboards']['wk_websites'] = values
		return results

	@http.route('/set/multiwebsite/id', type="json", auth='user')
	def set_multi_website_id(self, website_id=False):
		if website_id:
			request.session['wk_multi_website_id'] = website_id
		return True